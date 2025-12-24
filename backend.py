from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from rag_helper import load_rag_chain
import logging

app = FastAPI(title="Travel RAG API")

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize RAG vectorstore once on startup
vectorstore = None

@app.on_event("startup")
async def startup_event():
    global vectorstore
    logging.info("Loading RAG vectorstore...")
    vectorstore = load_rag_chain()
    logging.info("RAG vectorstore loaded successfully")

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    question: str
    answer: str

@app.post("/api/query", response_model=QueryResponse)
async def query_chatbot(request: QueryRequest):
    """Query the travel RAG chatbot - returns similar documents"""
    try:
        # Search for similar documents
        results = vectorstore.similarity_search(request.query, k=3)
        
        if results:
            # Combine the results into an answer
            answer = "\n\n".join([
                f"📍 {doc.page_content[:200]}..." if len(doc.page_content) > 200 
                else f"📍 {doc.page_content}"
                for doc in results
            ])
        else:
            answer = "No relevant information found in the travel guide."
        
        return QueryResponse(question=request.query, answer=answer)
    except Exception as e:
        return QueryResponse(question=request.query, answer=f"Error: {str(e)}")

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "Travel RAG Backend"}

@app.get("/")
async def root():
    """Root endpoint with API info"""
    return {
        "service": "Travel RAG Chatbot Backend",
        "version": "1.0.0",
        "endpoints": {
            "health": "/api/health",
            "query": "/api/query",
            "docs": "/docs"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
