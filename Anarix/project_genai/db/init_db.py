import os
import sqlite3
import pandas as pd

data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
db_path = os.path.join(os.path.dirname(__file__), 'ecommerce.db')

# Define CSV to table mapping
csv_tables = {
    'eligibility.csv': 'eligibility',
    'ad_sales.csv': 'ad_sales',
    'total_sales.csv': 'total_sales',
}

def load_csv_to_sqlite(csv_file, table_name, conn):
    csv_path = os.path.join(data_dir, csv_file)
    if not os.path.exists(csv_path):
        print(f"CSV not found: {csv_path}")
        return
    df = pd.read_csv(csv_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    print(f"Loaded {csv_file} into {table_name}")

def main():
    conn = sqlite3.connect(db_path)
    for csv_file, table_name in csv_tables.items():
        load_csv_to_sqlite(csv_file, table_name, conn)
    conn.close()
    print("Database initialized at", db_path)

if __name__ == '__main__':
    main() 