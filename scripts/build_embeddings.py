import torch
from torch.utils.data import DataLoader
from torchvision import datasets, models


# Dataset
dataset = datasets.OxfordIIITPet(
    root="./data",
    split="trainval",
    download=False,
    transform=models.ResNet50_Weights.DEFAULT.transforms()
)


# DataLoader
loader = DataLoader(
    dataset,
    batch_size=32,
    shuffle=False
)


# ResNet50 pré-entraîné
weights = models.ResNet50_Weights.DEFAULT

model = models.resnet50(weights=weights)

# Garder uniquement la partie qui produit l'embedding
model.fc = torch.nn.Identity()

model.eval()


# Stockage
all_embeddings = []
all_labels = []


# Extraction
with torch.no_grad():

    for images, labels in loader:

        embeddings = model(images)

        all_embeddings.append(embeddings)
        all_labels.append(labels)

        print(f"Images traitées : {len(all_labels) * 32}")


# Fusionner
embeddings = torch.cat(all_embeddings)
labels = torch.cat(all_labels)


print("\nTerminé !")
print("Embeddings :", embeddings.shape)
print("Labels :", labels.shape)


# Sauvegarder
torch.save(embeddings, "embeddings.pt")
torch.save(labels, "labels.pt")