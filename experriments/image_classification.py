import torch
from torchvision import models

print("PyTorch :", torch.__version__)

model = models.resnet50(
    weights=models.ResNet50_Weights.DEFAULT
)

model.eval()

print("ResNet50 chargé avec succès !")