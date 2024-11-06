import pandas as pd
import sqlite3

def load_excel_data(file_path):
    """Carregar dados de um arquivo Excel."""
    return pd.read_excel(file_path)

def insert_data_to_sql(df, db_name):
    """Inserir dados de um DataFrame em uma tabela SQL."""
    conn = sqlite3.connect(db_name)
    df.to_sql('tabela', conn, if_exists='replace', index=False)
    conn.close()

# Exemplo de uso
if __name__ == "__main__":
    data = load_excel_data('data.xlsx')
    insert_data_to_sql(data, 'database.db')

