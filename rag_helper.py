from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

def load_rag_chain():
    """Load and return a simple RAG chain using vector similarity"""
    try:
        # Load travel guide text with proper encoding
        loader = TextLoader("./docs/travelguide.txt", encoding="utf-8")
        documents = loader.load()
        print(f"Loaded {len(documents)} documents")
    except FileNotFoundError:
        print("Warning: travelguide.txt not found, using existing chromadb")
        # Use existing chromadb if available
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        vectorstore = Chroma(persist_directory="./chromadb", embedding_function=embeddings)
        return vectorstore

    # Split into chunks
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    texts = splitter.split_documents(documents)
    print(f"Split into {len(texts)} chunks")

    # Free Embeddings
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(texts, embeddings, persist_directory="./chromadb")
    print("Vectorstore created and persisted")
    
    return vectorstore
