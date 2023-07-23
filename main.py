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
    return {"message": "Hello World!"}

@app.get("/{location}")
async def say_hi(location: str):
    print(f"Received location: {location}")
    response_data = {"message": f"Hi {location}"}
    return JSONResponse(content=response_data)
