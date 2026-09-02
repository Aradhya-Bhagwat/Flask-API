from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def greet():
    return ("Welcome to my first Flask API using uvicorn server")