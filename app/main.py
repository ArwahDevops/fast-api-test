import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def client_data(request: Request):
    client_host = request.client.host
    client_port = request.client.port
    
    return {"client_host": client_host, "client_port": client_port}