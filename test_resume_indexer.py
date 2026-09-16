from rag.resume_indexer import ResumeIndexer


print("\n==============================")
print("RESUME INDEXER TEST")
print("==============================")


sample_resume = """
Python developer with experience in Flask,
SQL, machine learning and data analysis.

Education:
B.Tech Computer Science Engineering.

Projects:
Built an AI based internship discovery system
using Python, Flask, Gemini, RAG and ChromaDB.

Technical Skills:
Python, Flask, SQL, Machine Learning,
Git, GitHub, HTML, CSS.
"""


indexer = ResumeIndexer()


count = indexer.index_resume(
    sample_resume
)


print("\n==============================")
print("INDEXING RESULT")
print("==============================")

print(
    "Chunks indexed:",
    count
)

print("\n==============================")
print("RESUME INDEXER TEST COMPLETED")
print("==============================")