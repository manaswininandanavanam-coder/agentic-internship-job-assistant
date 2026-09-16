from rag.embeddings import EmbeddingService
from rag.vector_store import VectorStore


print("\n==============================")
print("VECTOR STORE TEST")
print("==============================")


# Create embedding service
embedding_service = EmbeddingService()


# Create vector store
vector_store = VectorStore()


# Sample resume information
documents = [
    "Python developer with experience in Flask and SQL.",
    "Machine learning student with experience in Python and scikit-learn.",
    "Frontend developer with React, JavaScript and HTML."
]


print("\nCreating embeddings...")

embeddings = (
    embedding_service.create_embeddings(
        documents
    )
)


# Store documents
document_ids = [
    "resume_1",
    "resume_2",
    "resume_3"
]


vector_store.add_documents(
    document_ids,
    documents,
    embeddings
)


print(
    "\nDocuments stored:",
    vector_store.get_document_count()
)


# Search
query = """
Python machine learning internship
"""


print("\nSearching for:")

print(query)


query_embedding = (
    embedding_service.create_embedding(
        query
    )
)


results = vector_store.search(
    query_embedding,
    top_k=2
)


print("\n==============================")
print("SEARCH RESULTS")
print("==============================")


for i, document in enumerate(
    results["documents"][0],
    start=1
):

    print(f"\nResult {i}:")
    print(document)


print("\n==============================")
print("VECTOR STORE TEST COMPLETED")
print("==============================")