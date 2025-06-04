from IPython.display import clear_output
from IPython.display import clear_output
import matplotlib.pyplot as plt
import pandas as pd
from recebe_valor_alternativa import recebe_valor,recebe_valor_submenu

def analise_veiculos_disponiveis(df, sistema = False):
    # Verifica se o sistema está sendo usado
    if(sistema == True):
        clear_output(wait=True)
    # Organiza o DF pela linha especifica
    df_sorted = df.sort_values("Número de Caminhões Disponíveis", ascending=False) 
    # Coloca uma organização especifica
    df_sorted.plot(
        x='Centro de Distribuição',
        y='Número de Caminhões Disponíveis',
        kind='bar',
        color='skyblue',
        legend=False
    )
    # Titulo pro gráfico
    plt.title('Quantidade de Caminhões por Centro de Distribuição')
    # Horizontal
    plt.xlabel('Centro de Distribuição')
    # Vertical
    plt.ylabel('Nº de Caminhões')
    # Ajusta os nomes
    plt.xticks(rotation=30, ha='right')
    # Ajusta o layout para evitar sobreposição
    plt.tight_layout()
    # Exibe o gráfico
    plt.show()
    # Verifica se o sistema está sendo usado
    if(sistema == True):
        input("\nPressione Enter para voltar ao menu...")

def analise_capacidade_total(df, sistema = False):
    # Verifica se o sistema está sendo usado
    if(sistema == True):
        clear_output(wait=True)

    # Nova Coluna pro dataframe
    df["Capacidade Total (Toneladas)"] = df["Número de Caminhões Disponíveis"] * df["Capacidade de Carga (Toneladas)"]
    # Organiza pela Coluna
    df_sorted = df.sort_values("Capacidade Total (Toneladas)", ascending=False)

    # Organiza o gráfico
    df_sorted.plot(
        x='Centro de Distribuição',
        y='Capacidade Total (Toneladas)',
        kind='bar',
        color='orange',
        legend=False
    )
    #Passa o titulo pro gráfico
    plt.title('Capacidade Total de Carga por Centro de Distribuição')
    # Horizontal
    plt.xlabel('Centro de Distribuição')
    # Vertical
    plt.ylabel('Capacidade Total (Toneladas)')
    # Ajusta os nomes
    plt.xticks(rotation=30, ha='right')
    # Ajusta o layout para evitar sobreposição
    plt.tight_layout()
    # Exibe o gráfico
    plt.show()
    # Verifica se o sistema está sendo usado
    if(sistema == True):
        input("\nPressione Enter para voltar ao menu...")

def analise_velocidade_media(df, sistema = False):
    # Verifica se o sistema está sendo usado
    if(sistema == True):
        clear_output(wait=True)
    # Organiza o Data Frame pela coluna especifica
    df_sorted = df.sort_values("Velocidade média (KM/h)", ascending=False)

    # Gera o plot do DF
    df_sorted.plot(
        x='Modelo',
        y='Velocidade média (KM/h)',
        kind='bar',
        color='lightcoral',
        legend=False
    )
    # Titulo pro gráfico
    plt.title('Velocidade Média dos Veículos por Modelo de Caminhão')
    # Horizontal
    plt.xlabel('Modelo')
    # Vertical
    plt.ylabel('Velocidade Média (KM/h)')
    # Ajusta os nomes
    plt.xticks(rotation=30, ha='right')
    # Ajusta o layout para evitar sobreposição
    plt.tight_layout()
    # Exibe o gráfico
    plt.show()
    # Verifica se o sistema está sendo usado
    if(sistema == True):
        input("\nPressione Enter para voltar ao menu...")

def analise_modelos(df, sistema = False):
    # Verifica se o sistema está sendo usado
    if(sistema == True):
        clear_output(wait=True)
    # Faz um group by nos modelos
    soma_por_modelo = df.groupby('Modelo')['Número de Caminhões Disponíveis'].sum()
    # Faz um Plot
    soma_por_modelo.plot(kind='pie', autopct='%1.1f%%', startangle=90)
    # Titulo pro gráfico
    plt.title('Distribuição dos Caminhões por Modelo')
    # Vertical
    plt.ylabel('')
    # Ajusta o layout para evitar sobreposição
    plt.tight_layout()
    # Exibe o gráfico
    plt.show()
    # Verifica se o sistema está sendo usado
    if(sistema == True):
        input("\nPressione Enter para voltar ao menu...")

def submenu_veiculos(df):
    # Sub Menu pra organização de código no sistema
    print("\n--- SUBMENU: VEÍCULOS ---")
    print("a - Caminhões por Centro de Distribuição")
    print("b - Capacidade por Centro de Distribuição")
    print("c - Velocidade Média por Modelo de Caminhão")
    print("d - Distribuição de Modelos de Caminhões")
    # Trata a opção escolhida
    opt = recebe_valor_submenu()   
    # Espécie de "Switch - Case" pra selecionar um deles
    if opt == 'a':
        analise_veiculos_disponiveis(df, True)
        return
    elif opt == 'b':
        analise_capacidade_total(df, True)
        return
    elif opt == 'c':
        analise_velocidade_media(df, True)
        return
    elif opt == 'd':
        analise_modelos(df, True)
        return
    else:
        #Se não encontrar, avisa que a opção é invalida
        print("Opção inválida.")
        
