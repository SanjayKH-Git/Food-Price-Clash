import time
start = time.time()

from concurrent.futures import ProcessPoolExecutor
from scraper import swiggyScraper, zomatoScraper

location = "Bangalore"
search_food_rest = "Krishnam Veg"

def scrape(scraper_function, location, search_food_rest):
    df = scraper_function(location, search_food_rest)
    return df

with ProcessPoolExecutor() as executor:
    futures = []
    futures.append(executor.submit(scrape, swiggyScraper, location, search_food_rest))
    futures.append(executor.submit(scrape, zomatoScraper, location, search_food_rest))

    swiggy_df, zomato_df = tuple(future.result() for future in futures)

print(swiggy_df, zomato_df)
print("Total time: ", time.time() - start)
