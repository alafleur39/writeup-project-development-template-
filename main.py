# I am creating a demo to show how FastAPI works
# you have to create a virtual environment and install fastapi and uvicorn
# pip install fastapi uvicorn
# how to create a virtual environment
# python -m venv env
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def read_root():  #this is the root endpoint # means this endpoint listens for GET requests at the root URL
    return {"message": "Hello from FastAPI "} # this will return a JSON response with a message

@app.get("/items/{item_id}") # this endpoint listens for GET requests at /items/{item_id}
def read_item(item_id: int, q: str = None): # this endpoint takes an item_id as a path parameter and an optional query parameter q
    return {"item_id": item_id, "query": q} # this will return a JSON response with the item_id and the query parameter

# FastAPI will be used to connect our AI agent with the frontend interface and 
# other backend tools like LangChain, ChromaDB, and the OpenAI API.

#FastAPI will be the API layer that connects the frontend interface with the AI agent and other backend tools.