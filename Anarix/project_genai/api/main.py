from fastapi import FastAPI, Request
from pydantic import BaseModel
from llm.llm_interface import question_to_sql
from utils.sql_utils import execute_sql, format_result
import os

app = FastAPI()
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'db', 'ecommerce.db')

class Question(BaseModel):
    question: str

@app.post('/ask')
async def ask(question: Question):
    sql = question_to_sql(question.question)
    columns, rows = execute_sql(sql, DB_PATH)
    result = format_result(columns, rows)
    return {"question": question.question, "sql": sql, "result": result} 