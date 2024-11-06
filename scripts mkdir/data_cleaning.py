import pandas as pd

def load_data(file_path):
    """Carregar os dados a partir de um arquivo CSV ou Excel."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Limpar dados, como remover valores nulos ou duplicados."""
    df = df.dropna()  # Remover valores nulos
    df = df.drop_duplicates()  # Remover duplicatas
    return df

def save_clean_data(df, file_path):
    """Salvar os dados limpos em um novo arquivo CSV ou Excel."""
    df.to_csv(file_path, index=False)

# Exemplo de uso
if __name__ == "__main__":
    data = load_data('input_file.csv')
    clean_data = clean_data(data)
    save_clean_data(clean_data, 'cleaned_data.csv')

