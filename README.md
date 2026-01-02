# 🧳 Smart Travel Budget Planner

A complete **RAG-based AI travel planning system** with real-time budget calculation, vector search, and multiple UI interfaces.

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [System Architecture](#system-architecture)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Component Breakdown](#component-breakdown)
- [Data Flow](#data-flow)
- [Installation & Setup](#installation--setup)
- [How to Use](#how-to-use)
- [Key Features Summary](#key-features-summary)

---

## 🎯 Project Overview

Smart Travel Budget Planner is a comprehensive travel planning application that combines:
- **Frontend**: Interactive HTML planner with 50+ Indian cities
- **Backend**: FastAPI with RAG (Retrieval-Augmented Generation) for AI-powered travel insights
- **Vector Database**: ChromaDB for instant travel guide searches
- **Multiple Interfaces**: HTML webapp, Streamlit app, and REST API

No API keys required. Works offline after initial setup.

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Frontend Layer                           │
├──────────────────┬──────────────────┬──────────────────────┤
│  travelpromax    │   travelpro.html │  Streamlit App       │
│  .html           │   (7 cities)     │  (http://8501)       │
│ (50+ cities)     │                  │                      │
└────────┬─────────┴────────┬─────────┴──────────────┬────────┘
         │                  │                        │
         └──────────────────┼────────────────────────┘
                            │
                   API Calls (fetch)
                            │
         ┌──────────────────▼────────────────────┐
         │     FastAPI Backend (Port 8000)       │
         │                                       │
         │   Routes:                             │
         │   - POST /api/query                   │
         │   - GET /api/health                   │
         │   - GET /                             │
         └────────────────┬──────────────────────┘
                          │
         ┌────────────────▼──────────────────┐
         │    RAG Chain (rag_helper.py)      │
         │                                   │
         │  - Load travel documents          │
         │  - Create embeddings              │
         │  - Vector similarity search       │
         └────────────────┬──────────────────┘
                          │
         ┌────────────────▼──────────────────┐
         │   ChromaDB Vector Store           │
         │   (Persistent storage)            │
         └───────────────────────────────────┘
```

---

## ✨ Features

### Frontend - HTML Travel Planner

**File**: `travelpromax.html` (Main app)

- 🏙️ **50+ Indian Cities** with real data
- 💰 **Real-time Budget Calculator** 
  - Transport (Bus, Train, Car, Flight)
  - Accommodation (Budget, Standard, Premium)
  - Food estimates per day
  - Activity costs based on travel type
- 🎯 **Travel Type Selection**
  - General, Budget, Luxury, Family, Adventure
  - Beach, Culinary, Pilgrimage, Romantic
- 📍 **Interactive Maps** (OpenStreetMap integration)
- 🔍 **City Search** with autocomplete
- 🌙 **Dark Mode** toggle
- 📊 **City Comparison** tool
- ✈️ **Transport Options** for all cities

### Backend - FastAPI Server

**File**: `backend.py`

**REST Endpoints**:
```
POST /api/query
├─ Input: {"query": "Travel guide for Mumbai"}
└─ Output: {"question": "...", "answer": "..."}

GET /api/health
└─ Returns: {"status": "healthy", "service": "Travel RAG Backend"}

GET /
└─ Returns: API info and available endpoints
```

### RAG Chain System

**File**: `rag_helper.py`

- **What is RAG?** Retrieval-Augmented Generation
- Retrieves relevant documents from vector database
- Returns similar travel guides based on search queries
- Process:
  1. Load travel guide text (UTF-8 encoded)
  2. Split into chunks (500 chars, 100 overlap)
  3. Convert to embeddings using HuggingFace: `all-MiniLM-L6-v2`
  4. Store in ChromaDB (persistent vector database)
  5. On query: Find similar documents using vector similarity

### Streamlit Application

**File**: `streamlit_app.py`

**URL**: `http://localhost:8501`

- ✨ Beautiful Streamlit interface
- 🔌 Connects to backend API
- 💬 Chat-based travel Q&A
- 📡 Real-time backend status check
- 🎨 Responsive, clean UI

### Vector Database
**ChromaDB** - Persistent vector storage
>> Note: The `chromadb/` folder is auto-generated on first backend run and is intentionally excluded from GitHub using `.gitignore`.



```
chromadb/
├── chroma.sqlite3        # Persistent database
└── [collection_id]/      # Embedding vectors
```

Stores:
- Travel guide text chunks
- Their embeddings (768-dimensional vectors)
- Metadata for retrieval

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **Backend API** | FastAPI + Uvicorn |
| **Vector DB** | ChromaDB |
| **Embeddings** | HuggingFace (all-MiniLM-L6-v2) |
| **RAG Framework** | LangChain |
| **Frontend (Web)** | Vanilla HTML/CSS/JS |
| **Frontend (App)** | Streamlit |
| **Python Version** | 3.11 (recommended) |
| **Dependencies** | See requirements.txt |

---

## 📁 Project Structure

```
travel_streamlit/
├── backend.py              # FastAPI backend server
├── rag_helper.py          # RAG (Retrieval-Augmented Generation) helper
├── streamlit_app.py       # Streamlit web app
├── requirements.txt       # Python dependencies
├── chromadb/              # Vector database (stores travel guide embeddings)
│   ├── chroma.sqlite3
│   └── [collection_id]/
└── docs/
    ├── travelpromax.html  # Main travel planner (50+ cities)
    ├── travelpro.html     # Alternative version (7 cities)
    ├── travelguide.txt    # Travel content for RAG
    └── [other travel docs]
```

---

## 🔍 Component Breakdown

### 1. Frontend - HTML Travel Planner

**travelpromax.html** (Main application)

Features:
- City selection from 50+ Indian cities
- Real-time budget calculation
- Transport type selection with cost estimates
- Accommodation type selection (Budget/Standard/Premium)
- Travel specialization modifiers (affects costs)
- Interactive OpenStreetMap integration
- Dark/Light theme toggle
- City comparison feature
- Search functionality

**How it works**:
1. User selects a city from dropdown
2. Frontend displays city info (attractions, tips)
3. User adjusts transport, days, people, accommodation type
4. Budget calculator updates in real-time
5. Can compare 2 cities side-by-side

### 2. Backend - FastAPI Server

**backend.py**

Responsibilities:
- Runs the RAG chain
- Searches vector database
- Returns relevant travel information
- Handles CORS for frontend access
- Provides REST API endpoints

**Endpoints**:
- `POST /api/query` - Query the travel chatbot
- `GET /api/health` - Health check
- `GET /` - API information

### 3. RAG Chain - rag_helper.py

**Purpose**: Retrieval-Augmented Generation for travel guides

**Process**:
1. Load travel guide text (UTF-8 encoded)
2. Split into chunks (500 chars, 100 overlap)
3. Convert to embeddings using HuggingFace model: `all-MiniLM-L6-v2`
4. Store in ChromaDB (persistent vector database)
5. When queried, find similar documents using vector similarity

**Example**:
```
Query: "Travel guide for Mumbai"
↓
Search ChromaDB for similar chunks
↓
Return top 3 matching documents
```

### 4. Streamlit App - streamlit_app.py

**Purpose**: Interactive web interface for travel Q&A

Features:
- Beautiful Streamlit UI
- Connects to backend API
- Chat-based travel questions
- Real-time backend status
- Responsive design

### 5. Vector Database - ChromaDB

**Purpose**: Stores embeddings of travel documents

**Structure**:
```
chromadb/
├── chroma.sqlite3        # Persistent database
└── [collection_id]/      # Embedding vectors (768-dim)
```

Stores:
- Travel guide text chunks
- Their vector embeddings
- Metadata for retrieval

---

## 📊 Data Flow

### User Opens travelpromax.html:

```
1. User selects "Mumbai"
   ↓
2. Frontend loads city info (name, banner, attractions)
3. Budget calculator shows estimated costs
4. User changes transport/days/people
5. Budget updates in real-time (100% frontend, no API call)
```

### User Queries Streamlit App:

```
1. User types: "best time to visit goa"
   ↓
2. POST request to http://localhost:8000/api/query
   ↓
3. Backend:
   - Creates embedding from query
   - Searches ChromaDB for similar documents
   - Returns top 3 matching travel guide chunks
   ↓
4. Streamlit displays the answer
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.11 (recommended)
- Git
- pip or conda

### Step 1: Clone the Repository

```bash
git clone https://github.com/HARI-CHARAN122/Smart-Travel-Budget-Planner.git
cd travel_streamlit
```

### Step 2: Create Virtual Environment

```bash
py -3.11 -m venv venv
venv\Scripts\activate # Windows
source .venv/bin/activate  # Linux/Mac
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Python Environment (if needed)

```bash
python -c "import sys; print(sys.executable)"
```

---

## 💻 How to Use

### Option 1: Use the HTML Travel Planner (Recommended)

**Open in Browser**:
```
c:\Users\Admin\Desktop\travel_streamlit\docs\travelpromax.html
```

Or right-click → Open with Browser

**Features**:
- Select a city from the list
- Adjust transport, days, people
- Change accommodation type
- Travel specialization affects costs
- Compare 2 cities
- Dark mode toggle

### Option 2: Start Backend + Streamlit

**Terminal 1 - Start Backend**:
```powershell
python backend.py
# Runs on http://localhost:8000
```

**Terminal 2 - Start Streamlit**:
```powershell
streamlit run streamlit_app.py
# Runs on http://localhost:8501
```

**Then**:
- Visit http://localhost:8501
- Type travel questions
- Get answers from your travel guides

### Option 3: Use REST API Directly

```bash
curl -X POST http://localhost:8000/api/query \
  -H "Content-Type: application/json" \
  -d '{"query":"Travel guide for Delhi"}'
```

---

## 🎯 Key Features Summary

✅ **Frontend Travel Planner**
- 50+ Indian cities with real data
- Real-time budget calculation
- Travel type specialization (affects costs)
- Dark/Light theme
- City comparison
- Interactive maps

✅ **Backend RAG System**
- Vector similarity search
- Travel guide Q&A
- REST API
- CORS enabled
- Health checks

✅ **Persistent Data**
- Vector embeddings stored in ChromaDB
- Survives app restarts
- Fast retrieval (instant search)

✅ **Multiple Interfaces**
- HTML webapp (browser-based, no installation)
- Streamlit app (interactive Python app)
- REST API (extensible, can integrate anywhere)

---

## 🌟 What Makes This Special

🚀 **No API Keys Required** - Uses free HuggingFace embeddings

💾 **Offline-Capable** - Works without internet (after initial setup)

⚡ **Fast** - Vector search is instant (< 100ms)

🎨 **Beautiful UI** - Modern, responsive design

🔧 **Extensible** - Easy to add more cities/travel guides

📊 **Educational** - Complete example of RAG + Vector DB + FastAPI + Frontend

---

## 📝 License

This project is open source and available under the MIT License.

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork and submit pull requests.

---

## 📧 Contact & Support

For issues or questions, please create a GitHub issue or contact the author.

---

## 🙏 Acknowledgments

- HuggingFace for free embeddings
- ChromaDB for vector storage
- FastAPI for backend framework
- Streamlit for web interface
- LangChain for RAG framework

---

**Happy Travels! 🚀✈️🏖️**
