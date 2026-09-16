import chromadb


class VectorStore:

    def __init__(self):

        print("Initializing ChromaDB...")

        self.client = chromadb.PersistentClient(
            path="data/chroma_db"
        )

        self.collection = (
            self.client.get_or_create_collection(
                name="resume_knowledge"
            )
        )

        print(
            "ChromaDB initialized successfully."
        )

    def add_document(
        self,
        document_id,
        text,
        embedding,
        metadata=None
    ):

        if not metadata:
            metadata = {
                "source": "resume"
            }

        self.collection.upsert(
            ids=[document_id],
            documents=[text],
            embeddings=[embedding],
            metadatas=[metadata]
        )

        print(
            f"Document added: {document_id}"
        )

    def add_documents(
        self,
        document_ids,
        texts,
        embeddings,
        metadatas=None
    ):

        if not metadatas:
            metadatas = [
                {
                    "source": "resume"
                }
                for _ in texts
            ]

        self.collection.upsert(
            ids=document_ids,
            documents=texts,
            embeddings=embeddings,
            metadatas=metadatas
        )

        print(
            f"{len(texts)} documents added."
        )

    def search(
        self,
        query_embedding,
        top_k=3
    ):

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        return results

    def get_document_count(self):

        return self.collection.count()