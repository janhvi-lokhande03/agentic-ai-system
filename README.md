# Agentic AI System for Multi-Step Tasks

## Objective

This project demonstrates an Agentic AI system capable of decomposing a complex task into multiple steps, assigning specialized agents, streaming results, and handling failures gracefully.

## Features

* Task decomposition using Planner Agent
* Multiple specialized agents

  * Planner Agent
  * Retriever Agent
  * Analyzer Agent
  * Writer Agent
* Async execution pipeline
* Streaming responses
* Failure handling with fallback mechanism
* Manual batching implementation

## Project Structure

agentic-ai-system/
│
├── agents/
│ ├── planner.py
│ ├── retriever.py
│ ├── analyzer.py
│ └── writer.py
│
├── services/
│ └── orchestrator.py
│
└── main.py

## Run the Project

Install dependencies:

pip install fastapi uvicorn

Start the application:

python -m uvicorn main:app --reload

Open:

http://127.0.0.1:8000/run

## Example Workflow

User Request
↓
Planner Agent
↓
Retriever Agent
↓
Analyzer Agent
↓
Writer Agent
↓
Streaming Response
