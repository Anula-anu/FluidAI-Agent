# 🤖 FluidAI Autonomous Agent

An Autonomous AI-powered Document Generation System built with **FastAPI**, **Google Gemini API**, and **python-docx**.

The system follows a multi-agent workflow where AI plans, executes, reviews, and generates professional Word documents automatically based on a user's request.

---

# 📌 Features

- ✅ Multi-Agent AI Workflow
- ✅ Planner Agent
- ✅ Executor Agent
- ✅ Reflection Agent
- ✅ Automatic Word Document Generation (.docx)
- ✅ REST API using FastAPI
- ✅ Interactive Swagger Documentation
- ✅ Google Gemini Integration
- ✅ Professional Proposal Generation

---

# 🏗 Architecture

```
                User Request
                      │
                      ▼
             FastAPI (/agent)
                      │
                      ▼
             Planner Agent
                      │
                      ▼
            Executor Agent
                      │
                      ▼
           Reflection Agent
                      │
                      ▼
        Word Document Generator
                      │
                      ▼
          Download .docx File
```

---

# 📂 Project Structure

```
FluidAI-Agent/
│
├── app.py
├── config.py
├── planner.py
├── executor.py
├── reflection.py
├── doc_generator.py
├── prompts.py
├── requirements.txt
├── README.md
├── .env
├── docs/
└── venv/
```

---

# ⚙️ Technologies Used

- Python 3.13
- FastAPI
- Uvicorn
- Google Gemini API
- python-docx
- Pydantic
- dotenv

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/FluidAI-Agent.git
cd FluidAI-Agent
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variable

Create a `.env` file.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

# ▶️ Run the Application

```bash
uvicorn app:app --reload
```

Application runs at

```
http://127.0.0.1:8000
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# 📡 API Endpoint

## POST /agent

Generates a professional AI document.

### Request

```json
{
    "request": "Create a project proposal for an AI Hospital Management System."
}
```

### Response

Downloads

```
AI_Project_Proposal.docx
```

---

# 🧠 Workflow

### 1️⃣ Planner Agent

- Understands the user request
- Creates a structured plan

---

### 2️⃣ Executor Agent

- Expands the plan
- Generates complete document content

---

### 3️⃣ Reflection Agent

- Reviews
- Improves formatting
- Corrects grammar
- Enhances quality

---

### 4️⃣ Document Generator

Creates a professionally formatted Microsoft Word document.

---

# 📷 Screenshots

## Swagger UI

_Add Screenshot_

---

## Generated Word Document

_Add Screenshot_

---

## Project Folder

_Add Screenshot_

---

# 📦 Dependencies

Main libraries

- FastAPI
- Uvicorn
- Google Generative AI
- python-docx
- python-dotenv
- Pydantic

---

# 📈 Future Improvements

- Multi-document support
- PDF Export
- Chat Interface
- Docker Deployment
- Authentication
- Multi-model LLM Support
- Memory-based AI Agents
- Logging & Monitoring

---

# 👨‍💻 Author

**Anula Biju**

GitHub:
https://github.com/YOUR_USERNAME

LinkedIn:
https://www.linkedin.com/in/YOUR_PROFILE

---

# 📄 License

This project is developed for learning, portfolio, and demonstration purposes.