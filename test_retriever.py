from rag.retriever import ResumeRetriever


print("\n==============================")
print("RETRIEVER TEST")
print("==============================")


retriever = ResumeRetriever()


query = """
I am looking for a Python
machine learning internship.
"""


results = retriever.retrieve(
    query,
    top_k=2
)


print("\n==============================")
print("RETRIEVED INFORMATION")
print("==============================")


for index, result in enumerate(
    results,
    start=1
):

    print(f"\nResult {index}:")

    print(
        "Content:",
        result["content"]
    )

    print(
        "Distance:",
        result["distance"]
    )


print("\n==============================")
print("RETRIEVER TEST COMPLETED")
print("==============================")