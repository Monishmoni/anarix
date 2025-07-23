# LLM interface for translating questions to SQL
# Fill in with your preferred LLM (local or Gemini API)

def question_to_sql(question: str) -> str:
    """
    Translate a natural language question to an SQL query using an LLM.
    Replace this stub with actual LLM integration.
    """
    # Example stub logic (replace with LLM call)
    if 'total sales' in question.lower():
        return 'SELECT SUM(total_sales) FROM total_sales;'
    elif 'roas' in question.lower():
        return 'SELECT SUM(ad_sales) / SUM(ad_spend) AS roas FROM ad_sales;'
    elif 'highest cpc' in question.lower():
        return 'SELECT product, MAX(cpc) FROM ad_sales;'
    else:
        return '-- LLM-generated SQL for: ' + question 