import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import clear_output
from recebe_valor_alternativa import recebe_valor_submenu
def analise_custos_operacionais(df_fin, sistema=False):
    # Verifica se o sistema está sendo usado
    if (sistema == True):
        clear_output(wait=True)
    # Valor total do custo operacional
    total = df_fin['Custo Operacional Total (R$/km)'].sum()
    # Grupo By no df
    resumo = df_fin.groupby('Centro de Distribuição')['Custo Operacional Total (R$/km)'] \
                    .sum().reset_index()
    # Custo operacional em %
    resumo['Porcentagem'] = (resumo['Custo Operacional Total (R$/km)'] / total * 100).round(2)
    
    # organiza o plot
    fig, ax = plt.subplots()
    # Formata o gráfico
    ax.pie(resumo['Porcentagem'], labels=resumo['Centro de Distribuição'], autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    # Titulo
    plt.title('Custo Operacional Total por Centro')
    #Exibe o Gráfico
    plt.show()
    # Verifica se o sistema está sendo usado
    if sistema:
        input("\nPressione Enter para voltar ao menu...")

def analise_gasto_medio_por_corrida(df_entregas, df_fin, df_veiculos, sistema=False):
    # Verifica se o sistema está sendo usado
    if (sistema == True):
        clear_output(wait=True)
    # Merge de 2 df's
    df = df_entregas.merge(df_fin, on='Centro de Distribuição', how='left')
    # Nova coluna calculada via esses 2 campos
    df['Custo_por_Corrida'] = df['Distância (km)'] * df['Custo Operacional Total (R$/km)']

    # Repetindo o merge no Df usaando a de veidculos
    df = df.merge(df_veiculos, on='Centro de Distribuição', how='left')
    # Verifica a chave
    grp_key = 'Tipo' if 'Tipo' in df_veiculos.columns else 'Centro de Distribuição'
    # Calcula a média do custo
    media = df.groupby(grp_key)['Custo_por_Corrida'].mean().reset_index()
    # Nova coluna de custo médio
    media['Custo Médio'] = media['Custo_por_Corrida'].round(2)

    # Formata o plot
    plt.figure()
    # Chama o gráfico de barras
    plt.bar(media[grp_key], media['Custo Médio'])
    # Vertical
    plt.xlabel(grp_key)
    # Horizontal
    plt.ylabel('Custo Médio por Corrida (R$)')
    # Titulo
    plt.title('Gasto Médio por Corrida')
    plt.xticks(rotation=45)
    # Ajusta o layout para evitar sobreposição
    plt.tight_layout()
    # Exibe o gráfico
    plt.show()
    if sistema:
        input("\nPressione Enter para voltar ao menu...")

def submenu_financeiro(df_entregas, df_fin, df_veiculos=None):
        # Sub Menu pra organização de código no sistema
        print("\n--- SUBMENU: FINANCEIRO ---")
        print("a - Custos Operacionais por Centro")
        print("b - Gasto Médio por Corrida")
        print("0 - Voltar")
        # Trata a opção escolhida
        opt = recebe_valor_submenu()
        # Espécie de "Switch - Case" pra selecionar um deles
        if opt == 'a':
            analise_custos_operacionais(df_fin, sistema=True)
        elif opt == 'b':
            analise_gasto_medio_por_corrida(df_entregas, df_fin, df_veiculos, sistema=True)
        elif opt == '0':
            return
        else:
            #Se não encontrar, avisa que a opção é invalida
            print("Opção inválida. Tente novamente.")
