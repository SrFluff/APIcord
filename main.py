from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse

app = FastAPI()

@app.get("/",response_class=FileResponse)
def root():
    return FileResponse("kitty.gif")
