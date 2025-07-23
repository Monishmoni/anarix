import sqlite3

def execute_sql(query: str, db_path: str):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(query)
    columns = [desc[0] for desc in cursor.description] if cursor.description else []
    rows = cursor.fetchall()
    conn.close()
    return columns, rows

def format_result(columns, rows):
    if not rows:
        return 'No results.'
    result = []
    for row in rows:
        result.append(dict(zip(columns, row)))
    return result 