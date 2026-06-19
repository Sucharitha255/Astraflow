#  AstraFlow Backend

AI-powered backend system for forecasting traffic impact caused by planned and unplanned events and generating operational recommendations.

## 📌 Overview

AstraFlow Backend is built using FastAPI and multiple AI decision engines to help traffic authorities proactively manage congestion caused by events such as:

* Construction activities
* Public events
* Vehicle breakdowns
* Accidents

The system predicts impact severity, estimates risk, finds similar historical events and recommends operational actions.

---

## ✨ Features

### 🧠 AI Prediction Pipeline

* Impact Assessment Engine
* Risk Assessment Engine
* Similarity Engine
* Resource Allocation Engine
* Barricade Recommendation Engine
* Diversion Recommendation Engine

---

## 🏗 Architecture

User Event Input

↓

Impact Engine

↓

Risk Engine

↓

Historical Similarity Engine

↓

Decision Engines

↓

Traffic Recommendations

---

## 🛠 Tech Stack

* Python
* FastAPI
* Pandas
* Scikit-learn
* Joblib
* Uvicorn

---

## 📂 Project Structure

backend/

├── api/

├── core/

├── preprocessing/

├── models/

├── config/

├── data/

├── utils/

└── main.py

---

## 🚀 Setup

### Clone repository

```bash
git clone <repository-url>
```

### Create virtual environment

```bash
python -m venv venv
```

### Activate environment

Windows:

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run server

```bash
uvicorn main:app --reload
```

Server runs at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 🔌 Available APIs

| Endpoint            | Description                 |
| ------------------- | --------------------------- |
| /predict            | Complete AstraFlow pipeline |
| /api/resources      | Resource recommendations    |
| /api/barricades     | Barricade recommendations   |
| /api/diversion      | Diversion recommendations   |
| /api/similar-events | Historical similar events   |

---










