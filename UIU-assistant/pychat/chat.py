import os
import chromadb
from dotenv import load_dotenv
from groq import Groq
import chromadb.utils.embedding_functions as embedding_functions

# Load environment variables
load_dotenv()

# Initialize Chroma Cloud
client = chromadb.CloudClient(
    api_key=os.getenv("CHROMADB_API_KEY"),
    tenant=os.getenv("CHOROMAD_TENANT_ID"),
    database=os.getenv("CHROMADB_DATABASE")
)

# Google embeddings (must match what was used during storage)
google_ef = embedding_functions.GoogleGenerativeAiEmbeddingFunction(
    api_key=os.getenv("CHROMA_GOOGLE_GENAI_API_KEY") 
)

# Get existing collection
collection = client.get_collection(
    name="Uiu_agent",
    embedding_function=google_ef
)

# Initialize Groq LLM
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Chat loop
print("💬 RAG Chat started. Type 'exit' to quit.\n")
while True:
    user_question = input("You: ")
    if user_question.lower() in ["exit", "quit"]:
        break
    
    # Retrieve relevant chunks from Chroma
    results = collection.query(query_texts=[user_question], n_results=10)
    retrieved_docs = "\n\n".join(results["documents"][0])

    if not retrieved_docs.strip():
        print("Bot: I couldn't find anything related to your question in my knowledge base.")
        continue

    # Build prompt
    prompt = f"""
You are a helpful assistant. Use the following context to answer the question.
If you cannot find an exact answer, give the closest possible answer based on the context.
Always tell the topic start date if user ask for.

Context:
{retrieved_docs}

Question:
{user_question}
"""

    # Get answer from Groq LLM
    response = groq_client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0
    )

    print("Bot:", response.choices[0].message.content, "\n")
