from IPython.display import clear_output
import matplotlib.pyplot as plt
import pandas as pd
from recebe_valor_alternativa import recebe_valor_submenu
def analise_custos(df, sistema=False):
    # Verifica se o sistema está sendo usado
    if(sistema == True):
        clear_output(wait=True)
    # Organiza o DF pela linha especifica
    fig, ax = plt.subplots(figsize=(8, 5))
    # Faz um plot com base nessa coluna
    ax.hist(df['Custo por Entrega (R$)'].dropna(), bins=20, color='skyblue', edgecolor='black')
    # Titulo
    ax.set_title('Histograma de Custos por Entrega')
    #configura os eixos x e y
    ax.set_xlabel('Custo por Entrega (R$)')
    ax.set_ylabel('Frequência')
    # Exibe o gráfico
    
    plt.show()
    # Verifica se o sistema está sendo usado
    if(sistema == True):
        input("\nPressione Enter para voltar ao menu...") 
def submenu_custos(df):
    # Sub Menu pra organização de código no sistema
    print("\n--- SUBMENU: Custos ---")
    print("a - Análise de custos")
    print("0 - Voltar")
    # Espécie de "Switch - Case" pra selecionar um deles
    # Trata a opção escolhida
    opt = recebe_valor_submenu()
    if opt == 'a':
        analise_custos(df, True)
    elif opt == '0':
         return
    else:
        #Se não encontrar, avisa que a opção é invalida
        print("Opção inválida.")