import uvicorn
import socket
from fastapi import FastAPI, request

app = FastAPI()

@app.get("/")
async def root():
    return "This is an example wsgi app served from {} to {}".format(socket.gethostname(), request.remote_addr)