from torchvision import datasets

dataset = datasets.OxfordIIITPet(
    root="./data",
    split="trainval",
    download=True
)

print("Nombre d'images :", len(dataset))
print("Taille de la première image :", dataset[0][0].size)
print("Classe :", dataset[0][1])