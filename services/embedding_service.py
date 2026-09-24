import torch
from torchvision import models


class EmbeddingService:

    def __init__(self):
        weights = models.ResNet50_Weights.DEFAULT

        self.model = models.resnet50(weights=weights)
        self.model.fc = torch.nn.Identity()
        self.model.eval()

        self.transform = weights.transforms()

    def get_embedding(self, image):
        image = self.transform(image).unsqueeze(0)

        with torch.no_grad():
            embedding = self.model(image)

        return embedding.numpy()