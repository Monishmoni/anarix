# GenAI E-commerce Data Agent

## Overview
This project builds an AI agent that answers questions about e-commerce data using natural language. It uses a local LLM to translate questions into SQL, queries a local SQLite database, and returns answers via API endpoints. Bonus: supports visualizations and streaming responses.

## Setup
1. Place your CSV datasets in the `data/` directory.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Initialize the database:
   ```
   python db/init_db.py
   ```
4. Run the API server:
   ```
   uvicorn api.main:app --reload
   ```

## API Usage
- `POST /ask` with JSON `{ "question": "..." }` to get an answer.
- (Bonus) `POST /ask/stream` for streamed responses.
- (Bonus) `POST /ask/visual` for chart/graph answers.

## LLM Options
- Use a local LLM (e.g., Llama.cpp, GPT4All) or Gemini API.
- Configure in `llm/llm_interface.py`.

## Directory Structure
- `data/` - Place CSVs here
- `db/` - Database and init scripts
- `llm/` - LLM interface code
- `api/` - FastAPI app
- `utils/` - Utility scripts

## Example Questions
- What is my total sales?
- Calculate the RoAS (Return on Ad Spend).
- Which product had the highest CPC (Cost Per Click)? 