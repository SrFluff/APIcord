from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse

app = FastAPI()

@app.get("/meme/{guh}",response_class=FileResponse)
def root(guh: str):
    return FileResponse(guh)
