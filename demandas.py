from IPython.display import clear_output
import matplotlib.pyplot as plt
import pandas as pd
from recebe_valor_alternativa import recebe_valor,recebe_valor_submenu


def analise_pico_sazonal(df, sistema = False):
    # Verifica se o sistema está sendo usado
    if(sistema == True):
        # Limpa a tela
        clear_output(wait=True)
    # Pega os picos sazoinais da tabela
    sazonal = df[df['Pico Sazonal'] == 'Sim'].copy()  
    # Escolhe os meses pra serem o horizontal
    sazonal.loc[:, 'Mês'] = sazonal['Data'].dt.to_period('M').astype(str)
    # Faz a contagem
    contagem_sazonal = sazonal['Mês'].value_counts().sort_index()
    # Passa o tamanho da figura
    plt.figure(figsize=(12, 6))
    # Seta o gráfico
    contagem_sazonal.plot(kind='bar', color='skyblue')
    # Passa o titulo
    plt.title('Picos Sazonais por Mês')
    # Passa o titulo na vertical
    plt.ylabel('Número de Ocorrências')
    # Passa o titulo na horizontal
    plt.xlabel('Mês')
    # Ajusta os nomes
    plt.xticks(rotation=45)
    # Ajusta o layout para evitar sobreposição
    plt.tight_layout()
    # Exbibe o dashboard
    plt.show()
    # Verifica se o sistema está sendo usado
    if(sistema == True):
        input("\nPressione Enter para voltar ao menu...")


def analise_real_vs_previsto(df, sistema = False):
    # Verifica se o sistema está sendo usado
    if(sistema == True):
        # Limpa a tela
        clear_output(wait=True)
    # Faz uma copia pra alterar o dataframe
    df_temp = df.copy()
    #Escolhe o mes e ano
    df_temp['Ano-Mês'] = df_temp['Data'].dt.to_period('M').astype(str)
    # tenta agrupar o mes e ano
    agrupado = df_temp.groupby('Ano-Mês')[['Volume de Vendas', 'Previsão de Demanda']].sum().sort_index()
    # Seleciona o tamanho da figura
    plt.figure(figsize=(14, 6))
    # Escolhe indices pra serem a previsão de vedas, e volume real
    plt.plot(agrupado.index, agrupado['Volume de Vendas'], label='Real', marker='o', color='royalblue')
    plt.plot(agrupado.index, agrupado['Previsão de Demanda'], label='Previsto', marker='x', color='orange')
    # Titulo do gráfico
    plt.title('Comparativo Real vs. Previsto da Demanda')
    # Horizontal
    plt.xlabel('Ano-Mês')
    #Vertical
    plt.ylabel('Volume')
    # Leganda
    plt.legend()
    # Ajusta os nomes
    plt.xticks(rotation=45)
    # Ajusta o layout para evitar sobreposição
    plt.tight_layout()
    # Exbibe o dashboard
    plt.show()
    # Verifica se o sistema está sendo usado
    if(sistema == True):
        input("\nPressione Enter para voltar ao menu...")

def analise_demanda_produto(df, sistema = False):
   # Verifica se o sistema está sendo usado
    if(sistema == True):
        # Limpa a tela
        clear_output(wait=True)
    # Passa a variavél de data
    df['Data'] = pd.to_datetime(df['Data'])
    # Pega por mes
    df['Ano-Mês'] = df['Data'].dt.to_period('M').astype(str)
    # Organiza o df
    df_grouped = df.groupby(['Ano-Mês', 'Produto'])['Volume de Vendas'].sum().unstack(fill_value=0)
    # Organiza o DataFrame
    df_grouped = df_grouped.sort_index()
    
    plt.figure(figsize=(14, 7))
    # Loop pra pegar as colunas pra passar como linhas no gráfico
    for produto in df_grouped.columns:
        plt.plot(df_grouped.index, df_grouped[produto], label=produto, marker='o')
    # Horizontal
    plt.xlabel('Ano-Mês')
    # Vertical
    plt.ylabel('Volume de Vendas')
    # Ajusta os nomes
    plt.xticks(rotation=45)
    #Legenda
    plt.legend(title='Produto', bbox_to_anchor=(1.05, 1), loc='upper left')
    # Selecioona o tipo de linhas
    plt.grid(True, linestyle='--', alpha=0.5)
    # Ajusta o layout para evitar sobreposição
    plt.tight_layout()
    # Exbibe o dashboard
    plt.show()
    # Verifica se o sistema está sendo usado
    if(sistema == True):
        input("\nPressione Enter para voltar ao menu...")
        
def submenu_demandas(df):
    # Sub Menu pra organização de código no sistema
    print("\n--- SUBMENU: DEMANDAS ---")
    print("a - Diferença entre Volume Real e Previsão")
    print("b - Evolução de Demanda por Data")
    # Trata a opção escolhida
    opt = recebe_valor_submenu()
    # Espécie de "Switch - Case" pra selecionar um deles
    if opt == 'a':
        analise_real_vs_previsto(df, True)
        return
    elif opt == 'b':
        analise_demanda_produto(df, True)
        return
    else:
        #Se não encontrar, avisa que a opção é invalida
        print("Opção inválida.")

