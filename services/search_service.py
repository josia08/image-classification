from pathlib import Path
import faiss


class SearchService:

    def __init__(self):
        base_dir = Path(__file__).resolve().parents[1]

        index_path = base_dir / "indexes" / "pets_cosine.index"

        self.index = faiss.read_index(str(index_path))

    def search(self, embedding, k=5):
        faiss.normalize_L2(embedding)

        similarities, indices = self.index.search(embedding, k)

        return indices[0], similarities[0]