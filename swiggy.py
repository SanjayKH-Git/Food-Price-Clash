import time
import re
import concurrent.futures
import requests
from bs4 import BeautifulSoup as Bs
from urllib.request import Request, urlopen
import googlesearch 

location = "Bangalore"
search_food_rest = "Krishnam Veg"

# Swiggy Scrape
zomato_search_query = f"Swiggy {search_food_rest} {location}"

swiggy_resturant_link = f"{next(googlesearch.search(zomato_search_query, num=5, stop=2, pause=2))}"
print(swiggy_resturant_link)

req = Request(swiggy_resturant_link , headers={'User-Agent': 'Mozilla/5.0'})
soup = Bs(urlopen(req), "html.parser")
food_items = dict()
for food in soup.find_all(class_="styles_detailsContainer__22vh8"):
    food_name_par = food.find('h3', class_='styles_itemNameText__3ZmZZ').text.strip()
    food_name = re.sub(r'\((.*?)\)', '', food_name_par).strip()
    food_price = food.find('span', class_='rupee').text.strip()
    food_items[food_name] = food_price
    
print(food_items)



