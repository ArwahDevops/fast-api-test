import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def home(request: Request):
    client_host = request.client.host
    return {"client_host": client_host}