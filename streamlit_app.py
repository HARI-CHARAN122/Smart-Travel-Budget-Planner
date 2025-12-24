import streamlit as st
import requests
import json

st.set_page_config(page_title="Local RAG Travel Chatbot")

st.title("🧳 Offline Travel Guide - RAG Chatbot")
st.markdown("Ask questions based on your travel documents. No API key required!")

# Backend API configuration
BACKEND_URL = "http://localhost:8000"

# Check backend connection
try:
    health = requests.get(f"{BACKEND_URL}/api/health", timeout=2)
    if health.status_code == 200:
        st.success("✅ Connected to backend")
except:
    st.error("⚠️ Backend not running. Start it with: python backend.py")

query = st.text_input("Ask a question:")

if query:
    with st.spinner("Searching..."):
        try:
            response = requests.post(
                f"{BACKEND_URL}/api/query",
                json={"query": query},
                timeout=30
            )
            if response.status_code == 200:
                result = response.json()
                st.success(result["answer"])
            else:
                st.error(f"Backend error: {response.status_code}")
        except requests.exceptions.ConnectionError:
            st.error("Cannot connect to backend. Make sure to run: python backend.py")
        except Exception as e:
            st.error(f"Error: {str(e)}")
