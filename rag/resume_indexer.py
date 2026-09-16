from rag.embeddings import EmbeddingService
from rag.vector_store import VectorStore


class ResumeIndexer:

    def __init__(self):

        print("\nInitializing Resume Indexer...")

        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStore()

        print("Resume Indexer initialized successfully.")

    def split_text(self, text, chunk_size=500):

        if not text:
            return []

        words = text.split()

        chunks = []

        for i in range(0, len(words), chunk_size):

            chunk = " ".join(
                words[i:i + chunk_size]
            )

            if chunk.strip():
                chunks.append(chunk)

        return chunks

    def index_resume(self, resume_text):

        if not resume_text:
            print("No resume text available.")
            return 0

        print("\nIndexing resume into RAG...")

        chunks = self.split_text(resume_text)

        if not chunks:
            print("No resume chunks created.")
            return 0

        print("Resume chunks created:", len(chunks))

        embeddings = (
            self.embedding_service
            .create_embeddings(chunks)
        )

        document_ids = []

        metadatas = []

        for index in range(len(chunks)):

            document_ids.append(
                f"resume_chunk_{index}"
            )

            metadatas.append({
                "source": "uploaded_resume",
                "chunk": index
            })

        self.vector_store.add_documents(
            document_ids,
            chunks,
            embeddings,
            metadatas
        )

        print(
            f"Resume indexed successfully: {len(chunks)} chunks"
        )

        return len(chunks)