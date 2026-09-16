from rag.embeddings import EmbeddingService


print("\n==============================")
print("EMBEDDING TEST")
print("==============================")

embedding_service = EmbeddingService()

text = """
Python developer with experience in
machine learning, SQL and Flask.
"""

embedding = embedding_service.create_embedding(
    text
)

print("\nEmbedding created successfully.")

print("Embedding length:", len(embedding))

print(
    "First 5 values:",
    embedding[:5]
)

print("\n==============================")
print("EMBEDDING TEST COMPLETED")
print("==============================")