# AI Recruitment & Fraud Detection System

## 📌 Overview
This project is an **AI-powered recruitment and fraud detection system** designed to streamline hiring processes and ensure authenticity.  
It includes modules for **job–resume semantic matching, AI-driven interview evaluation, fraud detection (face verification & focus monitoring), and candidate scoring** across multiple dimensions (technical, communication, culture fit).  

## 🚀 Features
- **Semantic Job–Resume Matching**  
  - NLP-based similarity scoring between job descriptions and resumes.  
  - Uses embeddings (BERT/SentenceTransformers).  

- **AI Interview Module**  
  - Automatic **Q&A generation** from job descriptions.  
  - **Answer evaluation** using NLP and scoring metrics.  

- **Fraud Detection Prototype**  
  - **Face verification** during video interviews.  
  - **Focus monitoring** to detect tab-switching or distraction.  

- **Candidate Scoring Engine**  
  - Technical Fit (skills match).  
  - Communication Fit (clarity, grammar, structure).  
  - Culture Fit (soft skills, sentiment).  

- **Backend Ready**  
  - Models are **containerized** and **API-ready** for integration into systems.  

---

## 🏗️ Tech Stack
- **Languages**: Python (backend ML), JavaScript (API/UI integration)  
- **Libraries**:  
  - `transformers`, `sentence-transformers` (semantic matching, Q&A)  
  - `scikit-learn`, `xgboost` (scoring engine)  
  - `deepface`, `opencv` (fraud detection)  
  - `fastapi` / `flask` (API endpoints)  
- **Data Processing**: Pandas, NumPy  
- **Deployment**: Docker, Kubernetes (scalable microservices)  

---
