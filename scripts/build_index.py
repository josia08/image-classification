import torch
import faiss
import numpy as np


# Charger les embeddings
embeddings = torch.load("embeddings.pt")

embeddings = embeddings.numpy().astype("float32")


# Normaliser les vecteurs
faiss.normalize_L2(embeddings)


# Index basé sur le produit scalaire
index = faiss.IndexFlatIP(2048)

index.add(embeddings)


print("Nombre de vecteurs :", index.ntotal)


faiss.write_index(index, "pets_cosine.index")

print("Index cosine sauvegardé !")