# Autonomous Content-to-Action Agent
## Google Antigravity Hackathon – Challenge 1

### Overview
An enterprise-grade autonomous AI orchestration platform that converts unstructured business content into actionable operational decisions using multi-agent reasoning.

---

## 🛠️ Setup Instructions

### Backend (Python/FastAPI)
```bash
cd backend
pip install -r requirements.txt
```
**CRITICAL**: Create a `.env` file in the `backend` directory and add your Gemini API key:
`GEMINI_API_KEY=your_actual_key_here`

```bash
uvicorn main:app --reload
```
Backend runs at: `http://127.0.0.1:8000`

### Frontend (Flutter)
```bash
cd frontend
flutter pub get
flutter run
```

---

## 🏛️ Architecture Overview

The system operates on a linear, multi-agent pipeline orchestrated by a central engine:

1. **User Upload** → Unstructured text is ingested.
2. **Content Understanding Agent** → Parses input and extracts key findings/metrics.
3. **Insight Extraction Agent** → Determines primary insights and root causes.
4. **Impact Analysis Agent** → Evaluates business impact and financial risk.
5. **Decision Agent** → Recommends actions and concrete execution steps.
6. **Tool Execution Engine** → Simulates an external API/CRM call based on the decision.
7. **Simulation Agent** → Projects the "before vs. after" system state and generates logs.
8. **Visualization** → The frontend visualizes the improved system state and traces.

---

## 🔌 Tools & APIs Used

- **Google Gemini API (`gemini-1.5-flash`)**: Powers the intelligence of all 5 reasoning agents, dynamically parsing text and generating structured JSON outcomes.
- **FastAPI / Python**: Handles backend orchestration, state management, and provides REST endpoints.
- **Flutter**: Provides a cross-platform mobile (and web) interface for users to upload content and visualize the autonomous execution and resulting system state.

---

## 🚀 How Antigravity is Used

The core of the system is the **AntigravityWorkflowEngine** and **AntigravityRuntime**. This platform:
- **Orchestrates Agent Workflows**: Dynamically manages the pipeline, passing the specific JSON context output from one AI agent into the prompt of the next.
- **Manages State & Tracing**: Logs every start/complete event for each agent, maintaining an observable reasoning chain (`/workflow-trace`).
- **Handles Execution**: Automatically delegates the recommended action to the Tool Registry to simulate external CRM updates.

---

## 📌 Assumptions

- **Input Format**: We assume the unstructured input is provided as text (which can be OCR'd or extracted from PDFs prior to the `/analyze` call).
- **Simulation Environment**: Real CRM/ERP systems are not actually modified; we use a realistic `SimulationAgent` and `tool_registry` to mock the state change.
- **Domain Focus**: While the agents are generic, they are currently prompted to prioritize business/financial metrics and risks, aligning with the "Business Insight" and "Policy/News" example scenarios.