
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Caminho do arquivo Excel
tabela = "Datalog.xlsx"

# Abrir o arquivo Excel corretamente
xls = pd.ExcelFile(tabela)

# Lista das abas que queremos acessar
abas = ["Entregas", "Veiculos", "Demandas", "Financeiros"]

# Carregar os DataFrames de cada aba em um dicionário
dfs = {}
for aba in abas:
    dfs[aba] = pd.read_excel(xls, sheet_name=aba)
    print(f"\n### Aba: {aba} ###")
    print(dfs[aba].head())  # Exibir as primeiras linhas para verificação

# Percorrer e exibir cada aba separadamente
for aba in abas:
    df = pd.read_excel(xls, sheet_name=aba)
    print(f"\n### Aba: {aba} ###")
    print(df.head())  # Exibir apenas as primeiras linhas para evitar sobrecarga

# Mesclar dados relevantes para análise de última milha
df_entregas = dfs["Entregas"]
df_financeiros = dfs["Financeiros"]
df_veiculos = dfs["Veiculos"]
df_demandas = dfs["Demandas"]
df = df_entregas.merge(df_financeiros, on='Centro de Distribuição', how='left')



def calcular_estados_entrega(df):
    total_entregas = len(df)
    estados = df['Status da Entrega'].value_counts()
    porcentagens = (estados / total_entregas * 100).round(2)
    print("\n1. Porcentagem dos Estados da Entrega:")
    print("\n".join([f"{estado}: {porc:.2f}%" for estado, porc in porcentagens.items()]))
    
    plt.figure(figsize=(8, 6))
    plt.pie(porcentagens, labels=porcentagens.index, autopct='%1.1f%%', startangle=90)
    plt.title('Porcentagem dos Estados da Entrega')
    plt.axis('equal')
    plt.show()


# 2. Número de Atrasos por Tipo de Incidente (com cores diferentes para cada barra)
def atrasos_por_incidente(df):
    atrasados = df[df['Status da Entrega'] == 'Atrasado']
    incidentes = atrasados['Incidente de Trânsito'].value_counts()
    print("\n2. Número de Atrasos por Tipo de Incidente:")
    print("\n".join([f"{incidente}: {count}" for incidente, count in incidentes.items()]))
    
    # Gráfico de barras com cores diferentes
    plt.figure(figsize=(10, 6))
    cores = ['#8B0000', '#00008B', '#006400', '#FF8C00'] # Lista de cores (vermelho claro, azul, verde claro, laranja claro)
    incidentes.plot(kind='bar', color=cores[:len(incidentes)])  # Usa apenas o número de cores necessário
    plt.title('Número de Atrasos por Tipo de Incidente')
    plt.xlabel('Tipo de Incidente')
    plt.ylabel('Número de Atrasos')
    plt.xticks(rotation=45)
    plt.show()


# 3. Exibir os dados da aba "Financeiros" no terminal
# Dados da aba "Financeiros"
def custos_operacional_total(df_financeiros):
    #Dados da aba "Finaneiros"
    labels = df_financeiros['Centro de Distribuição']
    combustivel_means = df_financeiros['Custo do Combustivel (R$/km)']
    manutencao_means = df_financeiros['Custo de Manutenção (R$/km)']
    operacional_means = df_financeiros['Custo Operacional Total (R$/km)']

    x = np.arange(len(labels))  # Localizações dos rótulos
    width = 0.25  # Largura das barras (ajustada para 3 barras)

    fig, ax = plt.subplots(figsize=(12, 6))  # Tamanho ajustado para melhor visualização

    rects1 = ax.bar(x - width, combustivel_means, width, label='Custo do Combustivel (R$/km)', color='#FF8C00')
    rects2 = ax.bar(x, manutencao_means, width, label='Custo de Manutenção (R$/km)', color='#FFD700')
    rects3 = ax.bar(x + width, operacional_means, width, label='Custo Operacional Total (R$/km)', color='#00008B')

    # Personalizar o gráfico
    ax.set_ylabel('Custo (R$/km)')
    ax.set_title('Custos por Centro de Distribuição - Aba Financeiros')
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45)
    ax.legend()

    # Adicionar rótulos nas barras
    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    ax.bar_label(rects3, padding=3)

    fig.tight_layout()
    plt.show()



df_veiculos = dfs ["Veiculos"]

# Preparar dados para o gráfico
labels = df_veiculos['Centro de Distribuição']
n_caminhoes = df_veiculos['Número de Caminhões Disponíveis']
capacidade = df_veiculos['Capacidade de Carga (Toneladas)']
velocidade = df_veiculos['Velocidade média (KM/h)']


x = np.arange(len(labels))  # posições no eixo X
width = 0.25  # largura das barras

# Criar o gráfico
fig, ax = plt.subplots(figsize=(12, 6))

rects1 = ax.bar(x - width, n_caminhoes, width, label='Caminhões', color='#4682B4')
rects2 = ax.bar(x, capacidade, width, label='Capacidade (t)', color='#32CD32')
rects3 = ax.bar(x + width, velocidade, width, label='Velocidade (km/h)', color='#FFA500')

# Personalizações
ax.set_ylabel('Valores')
ax.set_title('Dados de Veículos por Centro de Distribuição')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45)
ax.legend()

# Rótulos nas barras
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.bar_label(rects3, padding=3)

fig.tight_layout()
plt.show()






# Executando as análises com gráficos
print("\n=== Análise de Última Milha ===")
calcular_estados_entrega(df)
atrasos_por_incidente(df)
custos_operacional_total(df_financeiros)








   




