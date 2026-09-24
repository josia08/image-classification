import torch
from torchvision import models, transforms
from PIL import Image


# 1. Charger ResNet50
weights = models.ResNet50_Weights.DEFAULT
model = models.resnet50(weights=weights)

# 2. Retirer la dernière couche de classification
model.fc = torch.nn.Identity()

model.eval()


# 3. Préparation de l'image
preprocess = weights.transforms()

image = Image.open("chat.jpg").convert("RGB")
image = preprocess(image)

# Ajouter la dimension batch
image = image.unsqueeze(0)


# 4. Générer l'embedding
with torch.no_grad():
    embedding = model(image)


print("Shape :", embedding.shape)
print("Embedding :", embedding)