from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://sanjaykh-git-sturdy-succotash-vrqv95pgv74275g-8000.preview.app.github.dev/Home"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to the Food-Price-Clash API"}

# @app.get("/api/todo")
# def get_todo():
#     return 1

# @app.get("/api/todo{id}")
# def get_todo_by_id(id):
#     return 1

# @app.post("/api/todo")
# def post_todo_by_id(todo):
#     return 1


@app.get("/location")
def get_location(location: str):
    # Here you can implement the logic to handle the location data
    # and return the desired response
    # print(location)
    # print(f"Location received: {location}")
    
    return {"location": location}

def getNotes():
    return "Here is some data"

