import torch
import faiss
from torchvision import models, datasets
from PIL import Image
import matplotlib.pyplot as plt
from pathlib import Path


# =========================
# 1. Dataset
# =========================

dataset = datasets.OxfordIIITPet(
    root="../../data",
    split="trainval",
    download=False
)

print(dataset.classes)

# =========================
# 2. Modèle
# =========================

weights = models.ResNet50_Weights.DEFAULT

model = models.resnet50(weights=weights)
model.fc = torch.nn.Identity()
model.eval()


# =========================
# 3. Charger FAISS
# =========================

BASE_DIR = Path(__file__).resolve().parents[2]

index = faiss.read_index(
    str(BASE_DIR / "indexes" / "pets_cosine.index")
)

# =========================
# 4. Image recherchée
# =========================

image = Image.open("../../chat.jpg").convert("RGB")

preprocess = weights.transforms()

input_tensor = preprocess(image).unsqueeze(0)


# =========================
# 5. Embedding
# =========================

with torch.no_grad():
    embedding = model(input_tensor)

embedding = embedding.numpy().astype("float32")
faiss.normalize_L2(embedding)


# =========================
# 6. Recherche
# =========================

distances, indices = index.search(embedding, 5)


# =========================
# 7. Affichage
# =========================

print("\nRésultats :")

for rank, (index_image, similarity) in enumerate(
    zip(indices[0], distances[0]),
    start=1
):

    result_image, label = dataset[index_image]

    race = dataset.classes[label]

    print(
        f"{rank}. "
        f"Index={index_image} | "
        f"Race={race} | "
        f"Similarité={similarity:.4f}"
    )

    plt.figure()
    plt.imshow(result_image)
    plt.title(
        f"Résultat {rank} - {race}\n"
        f"Similarité : {similarity:.4f}"
    )
    plt.axis("off")
    plt.show()