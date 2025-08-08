from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import os
import random

fuck = len(os.listdir("memes"))

app = FastAPI()

@app.get("/memes/{guh}",response_class=FileResponse)
def root(guh: str):
    if os.path.exists("memes/" + guh):
        return FileResponse("memes/" + guh)
    else:
        return "Fuck you"

@app.get("/",response_class=FileResponse)
def root():
    shit = random.randint(0,fuck-1)
    return FileResponse("memes/" + os.listdir("memes")[shit])