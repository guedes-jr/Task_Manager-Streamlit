import streamlit as st
import pandas as pd
from utils import carregar_dados, salvar_dados, adicionar_tarefa
import plotly.express as px

st.set_page_config(
    page_title="Gerenciador de Tarefas",
    page_icon=":clipboard:",
    layout="wide",
)

st.title("📋 Gerenciador de Tarefas")

aba = st.sidebar.radio(
    "Navegar",
    [
        "📌 Tarefas", 
        "📈 Estatísticas"
    ]
)

dados = carregar_dados()

if aba == "📌 Tarefas":
    st.subheader("Nova Tarefa")
    with st.form(key="nova_tarefa"):
        titulo = st.text_input("Título")
        categoria = st.selectbox("Categoria", ["Pessoal", "Trabalho", "Estudos"])
        prioridade = st.selectbox("Prioridade", ["Baixa", "Média", "Alta"])
        prazo = st.date_input("Prazo")
        status = st.selectbox("Status", ["Pendente", "Em Progresso", "Concluída"])
        submit = st.form_submit_button("Adicionar")
        
        if submit:
            adicionar_tarefa(dados, titulo, categoria, prioridade, prazo, status)
            st.success("✅ Tarefa adicionada com sucesso!")
            salvar_dados(dados)
    
    st.subheader("Lista de Tarefas")
    st.dataframe(dados)
    st.subheader("Estatísticas de Tarefas")
    
elif aba == "📈 Estatísticas":
    st.subheader("Tarefas por Status")
    fig = px.pie(dados, names="Status", title="Distribuição das tarefas")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Tarefas por Prioridade")
    fig2 = px.bar(dados, x="Prioridade", title="Prioridades das tarefas")
    st.plotly_chart(fig2, use_container_width=True)