
import faiss, pickle

from sentence_transformers import SentenceTransformer


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# Load FAISS index
index = faiss.read_index("vectorstore/faiss_index.index")


# Load stored chunks
with open("vectorstore/chunks.pkl", "rb") as f:
    chunks = pickle.load(f)


def retrieve_context(query, top_k=5):

    # Convert query into embedding
    query_embedding = model.encode([query])

    # Search similar chunks
    distances, indices = index.search(query_embedding, top_k)

    retrieved_chunks = []

    for idx in indices[0]:
        retrieved_chunks.append(chunks[idx])

    return retrieved_chunks

query = "Machine learning interview questions about regression"

results = retrieve_context(query)

for i, chunk in enumerate(results):

    print(f"\n--- Result {i+1} ---\n")

    print(chunk)