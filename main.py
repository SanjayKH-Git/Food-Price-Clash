from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from parellizer import food_json


app = FastAPI()

# Allow requests from all origins during development (adjust as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:3000", "*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Please Enter Correct Details!"}


@app.get("/{location}/{resturant}")
async def say_hi(location: str, resturant: str):
    print(f"Received location: {location}")
    print(f"Resturant: {resturant}")

    # Food Price Clash Scraping and Analysis Logic
    # response_data = {"message": f"Hi {location}"}
    # food_details = food_json(location, resturant)
    food_details = {"swiggy": {"2 Idli 1 Vada": "90", "Rava Idli": "62",
                               "Curd Vada": "60", "Idli": "50", "Vada": "46", "Set Dosa": "85"},
                    "zomato": {"Mini Tiffin": "140", "Ghee Rice Combo": "180", "Jeera Rice Combo": "180",
                               "Chinese Combo": "229", "Kadhai Paneer With 2 Laccha Paratha Combo": "280"}
                    }

    response_data = {"message": f"{food_details}"}

    print(response_data)
    return JSONResponse(content=response_data)
