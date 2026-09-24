import torch
from torchvision import datasets, models
from PIL import Image


# Dataset
dataset = datasets.OxfordIIITPet(
    root="./data",
    split="trainval",
    download=False
)


# ResNet50 pré-entraîné
weights = models.ResNet50_Weights.DEFAULT

model = models.resnet50(weights=weights)

# On enlève la classification finale
model.fc = torch.nn.Identity()

model.eval()


# Récupérer une image du dataset
image, label = dataset[0]

print("Taille originale :", image.size)
print("Label :", label)


# Prétraitement adapté à ResNet50
preprocess = weights.transforms()

image = preprocess(image)

# [3, H, W] -> [1, 3, H, W]
image = image.unsqueeze(0)


# Générer l'embedding
with torch.no_grad():
    embedding = model(image)


print("Shape embedding :", embedding.shape)