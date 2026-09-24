from fastapi import FastAPI
from api.routes.search import router as search_router
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="AI Image Search API")

app.mount(
    "/images",
    StaticFiles(directory="data/oxford-iiit-pet/images"),
    name="images"
)  

@app.get("/")
def root():
    return {
        "message": "AI Image Search API",
        "status": "running"
    }


app.include_router(search_router)