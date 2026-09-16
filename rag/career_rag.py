from rag.retriever import ResumeRetriever


class CareerRAG:

    def __init__(self):
        print("\nInitializing Career RAG...")
        self.retriever = ResumeRetriever()
        print("Career RAG initialized successfully.")

    def retrieve_resume_context(self, query, top_k=3):

        if not query:
            return ""

        print("\n================================")
        print("RAG RETRIEVAL")
        print("================================")

        print("Query:", query)

        context = self.retriever.retrieve_context(
            query,
            top_k=top_k
        )

        if context:
            print("Resume context retrieved successfully.")
        else:
            print("No resume context found.")

        return context