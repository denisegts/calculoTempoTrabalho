import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Configuração da página
st.set_page_config(
    page_title="Cálculo de Tempo de Trabalho",
    page_icon="⏱️",
    layout="wide"
)

st.title("⏱️ Cálculo de Tempo de Trabalho por Tarefas")

# Sidebar para configurações
with st.sidebar:
    st.header("Configurações")
    st.write("Configure seus parâmetros de trabalho")

# Abas principais
tab1, tab2, tab3 = st.tabs(["Registrar Tarefas", "Análise", "Configurações"])

with tab1:
    st.header("Registrar Novas Tarefas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        data_tarefa = st.date_input("Data da tarefa", datetime.now())
    
    with col2:
        nome_tarefa = st.text_input("Nome da tarefa", placeholder="Ex: Desenvolver feature X")
    
    col3, col4 = st.columns(2)
    
    with col3:
        hora_inicio = st.time_input("Hora de início")
    
    with col4:
        hora_fim = st.time_input("Hora de término")
    
    descricao = st.text_area("Descrição da tarefa", placeholder="Descreva o que foi feito...")
    
    if st.button("✅ Registrar Tarefa", use_container_width=True):
        st.success("Tarefa registrada com sucesso!")

with tab2:
    st.header("Análise de Tarefas")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total de Tarefas", "0")
    
    with col2:
        st.metric("Tempo Total", "0h 0m")
    
    with col3:
        st.metric("Tempo Médio", "0h 0m")
    
    st.subheader("Histórico de Tarefas")
    st.info("Nenhuma tarefa registrada ainda. Comece a registrar tarefas na aba anterior!")

with tab3:
    st.header("Configurações")
    
    st.subheader("Preferências")
    formato_hora = st.selectbox("Formato de hora", ["24h", "12h"])
    
    st.subheader("Sobre")
    st.write("""
    **Cálculo de Tempo de Trabalho**
    
    Uma aplicação para rastrear e analisar o tempo gasto em diferentes tarefas.
    """)
