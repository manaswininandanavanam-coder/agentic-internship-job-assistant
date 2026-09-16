from rag.embeddings import EmbeddingService
from rag.vector_store import VectorStore


class ResumeRetriever:

    def __init__(self):

        print("Initializing Resume Retriever...")

        self.embedding_service = (
            EmbeddingService()
        )

        self.vector_store = (
            VectorStore()
        )

        print(
            "Resume Retriever initialized successfully."
        )

    def retrieve(
        self,
        query,
        top_k=3
    ):

        if not query:
            return []

        print(
            f"\nRetrieving information for: {query}"
        )

        query_embedding = (
            self.embedding_service
            .create_embedding(query)
        )

        results = (
            self.vector_store.search(
                query_embedding,
                top_k=top_k
            )
        )

        retrieved_documents = []

        documents = results.get(
            "documents",
            [[]]
        )[0]

        distances = results.get(
            "distances",
            [[]]
        )[0]

        for index, document in enumerate(
            documents
        ):

            distance = (
                distances[index]
                if index < len(distances)
                else None
            )

            retrieved_documents.append({

                "content": document,

                "distance": distance
            })

        return retrieved_documents

    def retrieve_context(
        self,
        query,
        top_k=3
    ):

        results = self.retrieve(
            query,
            top_k
        )

        if not results:
            return ""

        context_parts = []

        for result in results:

            context_parts.append(
                result["content"]
            )

        return "\n\n".join(
            context_parts
        )