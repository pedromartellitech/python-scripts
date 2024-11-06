import matplotlib.pyplot as plt
import pandas as pd

def plot_data(df, column_name):
    """Criar um gráfico de barras simples a partir de uma coluna."""
    df[column_name].value_counts().plot(kind='bar')
    plt.title(f'Visualização de {column_name}')
    plt.xlabel('Categorias')
    plt.ylabel('Contagem')
    plt.show()

# Exemplo de uso
if __name__ == "__main__":
    data = pd.read_csv('data.csv')
    plot_data(data, 'column_name')

