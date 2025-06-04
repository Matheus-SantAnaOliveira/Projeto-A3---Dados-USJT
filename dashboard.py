import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# Configuração de página
st.set_page_config(page_title="Dashboard Última Milha", layout="wide")
st.title("🚚 Dashboard de Última Milha")

# Carregar dados
xls = pd.ExcelFile("Datalog.xlsx")
abas = ["Entregas", "Veiculos", "Demandas", "Financeiros"]
dfs = {aba: pd.read_excel(xls, sheet_name=aba) for aba in abas}

df_entregas = dfs["Entregas"]
df_financeiros = dfs["Financeiros"]
df_veiculos = dfs["Veiculos"]
df_demandas = dfs["Demandas"]

# Merge para análises
df = df_entregas.merge(df_financeiros, on='Centro de Distribuição', how='left')

# Aba de Entregas
st.sidebar.title("Seções")
aba = st.sidebar.radio("Escolha uma visualização:", [
    "📦 Estados da Entrega",
    "⛔ Atrasos por Incidente",
    "💰 Custos Operacionais",
    "🚛 Dados de Veículos"
])

if aba == "📦 Estados da Entrega":
    st.subheader("📦 Porcentagem dos Estados da Entrega")
    total_entregas = len(df)
    estados = df['Status da Entrega'].value_counts()
    porcentagens = (estados / total_entregas * 100).round(2)

    fig1, ax1 = plt.subplots()
    ax1.pie(porcentagens, labels=porcentagens.index, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)

    st.dataframe(porcentagens.reset_index().rename(columns={'index': 'Status', 'Status da Entrega': 'Porcentagem (%)'}))

elif aba == "⛔ Atrasos por Incidente":
    st.subheader("⛔ Número de Atrasos por Tipo de Incidente")
    atrasados = df[df['Status da Entrega'] == 'Atrasado']
    incidentes = atrasados['Incidente de Trânsito'].value_counts()

    fig2, ax2 = plt.subplots()
    cores = ['#8B0000', '#00008B', '#006400', '#FF8C00']
    incidentes.plot(kind='bar', color=cores[:len(incidentes)], ax=ax2)
    ax2.set_xlabel("Tipo de Incidente")
    ax2.set_ylabel("Número de Atrasos")
    ax2.set_title("Número de Atrasos por Tipo de Incidente")
    st.pyplot(fig2)

    st.dataframe(incidentes.reset_index().rename(columns={'index': 'Incidente', 'Incidente de Trânsito': 'Quantidade'}))

elif aba == "💰 Custos Operacionais":
    st.subheader("💰 Custos por Centro de Distribuição")
    labels = df_financeiros['Centro de Distribuição']
    combustivel = df_financeiros['Custo do Combustivel (R$/km)']
    manutencao = df_financeiros['Custo de Manutenção (R$/km)']
    operacional = df_financeiros['Custo Operacional Total (R$/km)']
    
    x = np.arange(len(labels))
    width = 0.25

    fig3, ax3 = plt.subplots(figsize=(12, 6))
    ax3.bar(x - width, combustivel, width, label='Combustível', color='#FF8C00')
    ax3.bar(x, manutencao, width, label='Manutenção', color='#FFD700')
    ax3.bar(x + width, operacional, width, label='Operacional Total', color='#00008B')
    ax3.set_xticks(x)
    ax3.set_xticklabels(labels, rotation=45)
    ax3.set_ylabel("Custo (R$/km)")
    ax3.set_title("Custos por Centro de Distribuição")
    ax3.legend()
    st.pyplot(fig3)

    st.dataframe(df_financeiros)

elif aba == "🚛 Dados de Veículos":
    st.subheader("🚛 Dados de Veículos por Centro de Distribuição")
    labels = df_veiculos['Centro de Distribuição']
    caminhoes = df_veiculos['Número de Caminhões Disponíveis']
    capacidade = df_veiculos['Capacidade de Carga (Toneladas)']
    velocidade = df_veiculos['Velocidade média (KM/h)']

    x = np.arange(len(labels))
    width = 0.25

    fig4, ax4 = plt.subplots(figsize=(12, 6))
    ax4.bar(x - width, caminhoes, width, label='Caminhões', color='#4682B4')
    ax4.bar(x, capacidade, width, label='Capacidade (t)', color='#32CD32')
    ax4.bar(x + width, velocidade, width, label='Velocidade (km/h)', color='#FFA500')
    ax4.set_xticks(x)
    ax4.set_xticklabels(labels, rotation=45)
    ax4.set_ylabel("Valores")
    ax4.set_title("Dados de Veículos por Centro de Distribuição")
    ax4.legend()
    st.pyplot(fig4)

    st.dataframe(df_veiculos)

st.markdown("---")
st.caption("Desenvolvido com ❤️ usando Streamlit")