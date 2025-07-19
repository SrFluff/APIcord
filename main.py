from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import os

app = FastAPI()

@app.get("/memes/{guh}",response_class=FileResponse)
def root(guh: str):
    if os.path.exists("memes/" + guh):
        return FileResponse("memes/" + guh)
    else:
        return "Fuck you"
