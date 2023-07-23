from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

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

    response_data = {"message": f"Hi {location}"}
    return JSONResponse(content=response_data)
