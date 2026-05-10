
import os, pdfplumber
import faiss, pickle, re

from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Extract text from PDF
def extract_text_from_pdf(pdf_path):

    text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text

# Extract text from PDF
def extract_text_from_pdf(pdf_path):

    text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


# Clean extracted text
def clean_text(text):

    # Remove weird cid patterns
    text = re.sub(r'\(cid:\d+\)', '', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    return text

# Chunk text using LangChain
def chunk_text(text):

   text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

   chunks = text_splitter.split_text(text)

   return chunks

# Store all chunks
all_chunks = []

# Knowledge base folder
knowledge_path = "knowledge_base"

# Read all PDFs
for file in os.listdir(knowledge_path):

    if file.endswith(".pdf"):

        pdf_path = os.path.join(knowledge_path, file)
        print(f"Processing: {file}")

        text = extract_text_from_pdf(pdf_path)
        
        text = clean_text(text)

        chunks = chunk_text(text)

        all_chunks.extend(chunks)


print(f"Total chunks created: {len(all_chunks)}")

# Generate embeddings
print("Generating embeddings...")
# Generate embeddings
embeddings = model.encode(all_chunks)

# Create FAISS index
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

# Create vectorstore folder if not exists
os.makedirs("vectorstore", exist_ok=True)

# Save index
faiss.write_index(index, "vectorstore/faiss_index.index")

# Save chunks
with open("vectorstore/chunks.pkl", "wb") as f:
    pickle.dump(all_chunks, f)

print("RAG ingestion completed successfully")

