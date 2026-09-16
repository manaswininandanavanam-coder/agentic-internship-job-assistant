from sentence_transformers import SentenceTransformer


class EmbeddingService:

    def __init__(self):

        print("Loading embedding model...")

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        print("Embedding model loaded successfully.")

    def create_embedding(self, text):

        if not text:
            return []

        embedding = self.model.encode(
            text
        )

        return embedding.tolist()

    def create_embeddings(self, texts):

        if not texts:
            return []

        embeddings = self.model.encode(
            texts
        )

        return embeddings.tolist()