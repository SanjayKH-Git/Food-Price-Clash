from scraper import swiggyScraper, zomatoScraper
from concurrent.futures import ProcessPoolExecutor
import time

# location = "Bangalore"
# search_food_rest = "Krishnam Veg"

start = time.time()
def food_json(location, search_food_rest):
    
    def scrape(scraper_function, location, search_food_rest):
        df = scraper_function(location, search_food_rest)
        return df


    with ProcessPoolExecutor() as executor:
        futures = []
        futures.append(executor.submit(
            scrape, swiggyScraper, location, search_food_rest))
        futures.append(executor.submit(
            scrape, zomatoScraper, location, search_food_rest))

        swiggy_df, zomato_df = tuple(future.result() for future in futures)

    food_json = {"swiggy": swiggy_df,
                 "zomato": zomato_df}
    print(swiggy_df, zomato_df)
    print("Total time: ", time.time() - start)
    
    return food_json
