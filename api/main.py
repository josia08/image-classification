from fastapi import FastAPI
from api.routes.search import router as search_router
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Image Search API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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