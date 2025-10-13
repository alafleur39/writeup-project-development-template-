# Tool / Skill Research Report

---

## Basic Information

| Field | Details |
|-------|----------|
| **Name** | _Andy Lafleur_ |
| **Project** | AI Knowledge Management Agent |
| **Role** |  Backend Developer |
| **Tool / Skill** |  FastAPI |
| **Date** | 12 October 2025  |
| **Links / Sources** | [Official Docs](https://fastapi.tiangolo.com/#recap) · [GitHub Repo](https://github.com/fastapi/fastapi) · [YouTube Tutorial](https://www.youtube.com/watch?v=iWS9ogMPOI0) |
---

## 1. Overview  

> _Example:_ 
> **FastApi** is a fast python web framework designed to make building APIs easier. It is intended for Restful apis.

---

## 2. Core Features & Capabilities  

> _Example:_  
> - **Automatic request validation / parsing:** Using pydantic models, FastAPI makes sures you're data is correct, clean and safe before you're program uses it.  
> - **Interactive API docs:** FastApi automatically generates documentation we can actually use and not just read. This will help us debug and make teamwork easier..  
> - **Async Support and Concurrency:** Fast API can handle many tasks at once and supports asynchronous code this allows us to use server resources more efficiently.
> - **High Performance and Simplicity:** Fast API is one of the best performing python frameworks on par with Node.js and Go and it is designed to be easy to use

---

## 3. Role in Our Project    
> FastAPI's role in our project can be used to set up a backend interface for our Ai agent. FastAPI can handle http requests, http routing and error logging.
> FastAPI's concurrency allows the project to scale for more users as it can handle multiple tasks and requests.
> An example of potential endpoints for our Ai knowledge Agent could be POST /query -> "Asks the agent a question" POST/ ingest ->Upload text/PDF/URL to store in the vector DB


---

## 4. Installation / Setup Guide  
To install FastApi go into your virtual environment for python and type the following commands 
Uvicorn is a fast lightweight python server used with FastAPI to run your Api server
```bash
# Example setup
pip install fastapi
pip install uvicorn
```
The following is an example of how to create a FastApi Server:
```python
from fastapi import FastAPI #app/main.py

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}
```
To run the server:
```bash
uvicorn app.main:app --reload --port 8000


