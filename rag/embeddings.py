import hashlib
import math
import re


class EmbeddingService:

    def __init__(self):
        print("Initializing lightweight embedding service...")
        print("Using TF-IDF style local embeddings.")
        print("No PyTorch or Sentence Transformers required.")

    def _tokenize(self, text):
        if not text:
            return []

        text = text.lower()

        # Keep words and common technical terms
        tokens = re.findall(r"[a-zA-Z0-9+#.]+", text)

        return tokens

    def _hash_index(self, token, dimensions):
        digest = hashlib.md5(
            token.encode("utf-8")
        ).hexdigest()

        number = int(digest, 16)

        return number % dimensions

    def create_embedding(self, text):

        if not text:
            return []

        dimensions = 384

        tokens = self._tokenize(text)

        if not tokens:
            return [0.0] * dimensions

        vector = [0.0] * dimensions

        for token in tokens:

            index = self._hash_index(
                token,
                dimensions
            )

            vector[index] += 1.0

        # Normalize vector
        magnitude = math.sqrt(
            sum(value * value for value in vector)
        )

        if magnitude > 0:

            vector = [
                value / magnitude
                for value in vector
            ]

        return vector

    def create_embeddings(self, texts):

        if not texts:
            return []

        return [
            self.create_embedding(text)
            for text in texts
        ]