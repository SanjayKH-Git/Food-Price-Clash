import time
import googlesearch
from playwright.sync_api import sync_playwright
from xvfbwrapper import Xvfb


location = "Bangalore"
search_food_rest = "Krishnam Veg"


# Zomato Scrape
zomato_search_query = f"Zomato {search_food_rest} {location}"

zomato_resturant_link = f"{next(googlesearch.search(zomato_search_query, num=5, stop=2, pause=2))}/order"
print(zomato_resturant_link)

vdisplay = Xvfb()
vdisplay.start()

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

    print(food_items)
    browser.close()
vdisplay.stop()