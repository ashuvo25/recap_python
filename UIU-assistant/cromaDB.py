import chromadb
import os
from dotenv import load_dotenv
from langchain.document_loaders import DirectoryLoader, PyPDFLoader
# Load variables from .env file into environment
load_dotenv()
client = chromadb.CloudClient(
  api_key=os.getenv("CHROMADB_API_KEY"),
  tenant=os.getenv
  ("CHOROMAD_TENANT_ID"),
  database=os.getenv("CHROMADB_DATABASE")
)


#loading pdf folder and the pdf
from langchain.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
  path="ScrapingwithCrwalai/dataPacks/",  # PDFs for pdf folder 
  glob="**/*.pdf",          #  load all PDFs one by one
  loader_cls=PyPDFLoader
)

documents = loader.load()
print(f"Loaded {len(documents)} documents")




import chromadb.utils.embedding_functions as embedding_functions
huggingface_ef = embedding_functions.HuggingFaceEmbeddingFunction(
    api_key=os.getenv("HUGGINGFACE_API_KEY"),
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

#make the pdf into chunk 


#Do embadding 





# collection = client.create_collection(name="agent_base_chatbot")
from datetime import datetime
collection = client.get_or_create_collection(
    name="Uiu_agent",
    embedding_function=huggingface_ef,
    metadata={
        "description": "my first Chroma collection",
        "created": str(datetime.now())
    }
)



#Create a Retriever