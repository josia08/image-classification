from fastapi import APIRouter, UploadFile, File
from PIL import Image
import io
from torchvision import datasets

from services.embedding_service import EmbeddingService
from services.search_service import SearchService


router = APIRouter()

embedding_service = EmbeddingService()
search_service = SearchService()

dataset = datasets.OxfordIIITPet(
    root="./data",
    split="trainval",
    download=False
)


@router.post("/search")
async def search_image(file: UploadFile = File(...)):

    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    embedding = embedding_service.get_embedding(image)

    indices, similarities = search_service.search(
        embedding,
        k=5
    )

    results = []

    for index, similarity in zip(indices, similarities):

        label_id = dataset[int(index)][1]
        label_name = dataset.classes[label_id]

        results.append({
            "index": int(index),
            "label": label_name,
            "similarity": float(similarity)
        })

    return {
        "results": results
    }