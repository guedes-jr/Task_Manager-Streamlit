from datetime import datetime
import pandas as pd
import os

ARQUIVO = "tarefas.csv"

   
def carregar_dados():
    if not os.path.exists(ARQUIVO) or os.stat(ARQUIVO).st_size == 0:
        return pd.DataFrame(columns=["Título", "Categoria", "Prioridade", "DataEntrega", "Status"])
    try:
        return pd.read_csv(ARQUIVO)
    except pd.errors.EmptyDataError:
        return pd.DataFrame(columns=["Título", "Categoria", "Prioridade", "DataEntrega", "Status"])

def salvar_dados(df):
    df.to_csv(ARQUIVO, index=False)

def adicionar_tarefa(df, titulo, categoria, prioridade, prazo, status):
    nova_linha = {
        "Título": titulo,
        "Categoria": categoria,
        "Prioridade": prioridade,
        "DataEntrega": prazo.strftime("%Y-%m-%d"),
        "Status": status
    }
    df.loc[len(df)] = nova_linha
