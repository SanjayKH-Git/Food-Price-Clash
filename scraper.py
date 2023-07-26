import time
import re
import concurrent.futures
import googlesearch
from bs4 import BeautifulSoup as Bs
from urllib.request import Request, urlopen
from playwright.sync_api import sync_playwright


def swiggyScraper(location, search_food_rest):
    # Swiggy Scrape
    zomato_search_query = f"Swiggy {search_food_rest} {location}"

    swiggy_resturant_link = f"{next(googlesearch.search(zomato_search_query, num=5, stop=2, pause=2))}"
    print(swiggy_resturant_link)

    req = Request(swiggy_resturant_link, headers={'User-Agent': 'Mozilla/5.0'})
    soup = Bs(urlopen(req), "html.parser")
    food_items = dict()
    for food in soup.find_all(class_="styles_detailsContainer__22vh8"):
        food_name_par = food.find(
            'h3', class_='styles_itemNameText__3ZmZZ').text.strip()
        food_name = re.sub(r'\((.*?)\)', '', food_name_par).strip()
        food_price = food.find('span', class_='rupee').text.strip()
        food_items[food_name] = food_price

    # print(food_items)
    return food_items


# Zomato Scrape
def zomatoScraper(location, search_food_rest):
    zomato_search_query = f"Zomato {search_food_rest} {location}"

    zomato_resturant_link = f"{next(googlesearch.search(zomato_search_query, num=5, stop=2, pause=2))}/order"
    print(zomato_resturant_link)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(zomato_resturant_link, wait_until="load")

        food_items = dict()
        for food in page.query_selector_all("//div[@class='sc-1s0saks-10 cYSFTJ']"):
            food_name = food.query_selector("h4").inner_text()
            food_price = food.query_selector(".sc-17hyc2s-1.cCiQWA").inner_text()
            food_items[food_name] = food_price.replace("₹", "")

        browser.close()
            
    # print(food_items)
    return food_items
