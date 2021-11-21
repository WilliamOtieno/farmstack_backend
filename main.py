from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import fetch_one_todo, fetch_all_todos, create_todo, update_todo, remove_todo
from models import Todo

app = FastAPI()

origins = ['http://localhost:3000']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


@app.get("/")
async def read_root():
    return {"Ping": "Pong"}


@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response


@app.get("/api/todo/{title}", response_model=Todo)
async def get_todo_by_title(title):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f"There is not TODO item with the title {title}")


@app.delete("/api/todo/{id}")
async def delete_todo_by_id(id):
    return 1


@app.post("/api/todo", response_model=Todo)
async def post_todo(todo):
    return 1


@app.put("/api/todo/{id}")
async def update_todo_by_id(id, data):
    return 1


