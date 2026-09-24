import torch
import faiss
from torch.utils.data import DataLoader
from torchvision import datasets, models


# Dataset
weights = models.ResNet50_Weights.DEFAULT

dataset = datasets.OxfordIIITPet(
    root="./data",
    split="trainval",
    download=False,
    transform=weights.transforms()
)


# Modèle
model = models.resnet50(weights=weights)
model.fc = torch.nn.Identity()
model.eval()


# Index cosine
index = faiss.read_index("pets_cosine.index")


# Évaluer 100 images
loader = DataLoader(
    dataset,
    batch_size=1,
    shuffle=False
)

total_precision = 0
count = 0

with torch.no_grad():

    for image, label in loader:

        embedding = model(image)
        embedding = embedding.numpy().astype("float32")

        faiss.normalize_L2(embedding)

        similarities, indices = index.search(embedding, 6)

        # Le premier résultat est généralement l'image elle-même
        results = indices[0][1:6]

        relevant = 0

        for result_index in results:

            _, result_label = dataset[result_index]

            if result_label == label.item():
                relevant += 1

        precision = relevant / 5

        total_precision += precision
        count += 1

        if count % 20 == 0:
            print(f"Images évaluées : {count}")


        if count == 100:
            break


precision_at_5 = total_precision / count

print()
print("===== ÉVALUATION =====")
print(f"Images évaluées : {count}")
print(f"Precision@5 : {precision_at_5:.4f}")
print(f"Pourcentage : {precision_at_5 * 100:.2f}%")