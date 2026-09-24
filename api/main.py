from fastapi import FastAPI
from api.routes.search import router as search_router

app = FastAPI(title="AI Image Search API")


@app.get("/")
def root():
    return {
        "message": "AI Image Search API",
        "status": "running"
    }


app.include_router(search_router)