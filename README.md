Vibraa 🎵
An AI-powered music streaming backend built with FastAPI.

Tech Stack
FastAPI
Python
PostgreSQL (Coming Soon)
SQLAlchemy
LangChain
LangGraph
Spotify API
OpenAI
Docker
Features
REST API
AI Chat
Smart Recommendations
Mood Detection
Playlist Intelligence
Long-term Memory
Authentication
Run Locally
python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt

cd backend
python -m uvicorn app.main:app --reload
