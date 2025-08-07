import os
import chromadb
from dotenv import load_dotenv
from datetime import datetime
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import chromadb.utils.embedding_functions as embedding_functions

# Load environment variables
load_dotenv()

# Initialize Chroma Cloud client
client = chromadb.CloudClient(
    api_key=os.getenv("CHROMADB_API_KEY"),
    tenant=os.getenv("CHOROMAD_TENANT_ID"),
    database=os.getenv("CHROMADB_DATABASE")
)

# Load PDFs from folder
loader = DirectoryLoader(
    path="ScrapingwithCrwalai/dataPacks/",
    glob="**/*.pdf",
    loader_cls=PyPDFLoader
)

documents = loader.load()
print(f"Loaded {len(documents)} documents")

# Create chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(documents)
print(f"Split into {len(chunks)} chunks")

# Use Google Generative AI embeddings
google_ef = embedding_functions.GoogleGenerativeAiEmbeddingFunction(
    api_key=os.getenv("CHROMA_GOOGLE_GENAI_API_KEY") 
)

# Create or get collection
collection = client.get_or_create_collection(
    name="Uiu_agent",
    embedding_function=google_ef,
    metadata={
        "description": "pushing academid results to ChromaDB",
        "created": str(datetime.now())
    }
)

# Add documents to Chroma
collection.add(
    documents=[doc.page_content for doc in chunks],
    metadatas=[doc.metadata for doc in chunks],
    ids=[f"doc_{i}" for i in range(len(chunks))]
)

# Search / Query (RAG)
results = collection.query(
    query_texts=["What does UIU stand for?"],
    n_results=3
)

print(results["documents"])
