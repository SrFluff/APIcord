from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def root():
    return "Fuhh you"

@app.get("/image")
def root():
    return FileResponse("image.png",media_type="image/png")
