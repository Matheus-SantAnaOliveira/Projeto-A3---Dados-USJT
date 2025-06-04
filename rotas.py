from IPython.display import clear_output
import matplotlib.pyplot as plt
from recebe_valor_alternativa import recebe_valor_submenu
def analise_top_distancias(df, sistema=False):
    # Verifica se o sistema está sendo usado
    if(sistema == True):
        clear_output(wait=True)
    # Faz um GroupBy e Seleciona os 10 primeiros
    top = (df.groupby(['Centro de Distribuição','Destino'])['Distância (km)']
             .mean().sort_values(ascending=False).head(10))
    # Seta o gráfico
    fig, ax = plt.subplots()
    # Escolhe o tipo de gráfico
    top.plot(kind='barh', ax=ax)
    # Titulo
    ax.set_title('Top 10 Rotas por Distância Média')
    # horizontal
    ax.set_xlabel('Distância (km)')
    # Ajusta o layout para evitar sobreposição
    plt.tight_layout()
    # Exibe o gráfico
    plt.show()
    # Verifica se o sistema está sendo usado
    if(sistema == True):
        input("\nPressione Enter para voltar ao menu...")

def analise_tempo_medio_viagem(df, sistema=False):
    # Verifica se o sistema está sendo usado
    if(sistema == True):
        clear_output(wait=True)
    # Faz um GroupBy e seleciona os 10 primeiros
    grp = (df.groupby(['Centro de Distribuição','Destino'])['Prazo de Entrega (dias)']
             .mean().sort_values(ascending=False).head(10))
    # Seta o gráfico
    fig, ax = plt.subplots()
    grp.plot(kind='barh', ax=ax)
    # Titulo
    ax.set_title('Top 10 Rotas com maior Tempo Médio')
    # Horizontal
    ax.set_xlabel('Tempo (Dias)')
    # Ajusta o layout para evitar sobreposição
    plt.tight_layout()
    # Exibe o gráfico
    plt.show()
    # Verifica se o sistema está sendo usado
    if(sistema == True):
        input("\nPressione Enter para voltar ao menu...")

def analise_distribuicao_incidentes(df, sistema=False):
    # Verifica se o sistema está sendo usado
    if(sistema == True):
        clear_output(wait=True)
    # Verifica os que tiveram incidente
    inc = df[df['Incidente de Trânsito'] != 'Nenhum']
    # Conta a quantidade P/ CAUSA
    counts = inc['Incidente de Trânsito'].value_counts()
    # Organiza o gráfico
    fig, ax = plt.subplots()
    # Seleciona o tipo de gráfico
    counts.plot(kind='pie', autopct='%1.1f%%', ax=ax)
    # Titulo
    ax.set_title('Distribuição de Incidentes')
    # Horizontal
    plt.ylabel('')
    # Ajusta o layout para evitar sobreposição
    plt.tight_layout()
    # Exibe o gráfico
    plt.show()
    # Verifica se o sistema está sendo usado
    if(sistema == True):
        input("\nPressione Enter para voltar ao menu...")

def submenu_rotas(df):
    # Sub Menu pra organização de código no sistema
    print("\n--- SUBMENU: ROTAS ---")
    print("a - Top Distâncias")
    print("b - Tempo Médio de Viagem")
    # Trata a opção escolhida
    opt = recebe_valor_submenu()
    # Espécie de "Switch - Case" pra selecionar um deles
    if opt == 'a':
        analise_top_distancias(df, True)
    elif opt == 'b':
        analise_tempo_medio_viagem(df, True)
    elif opt == '0':
        return
    else:
        #Se não encontrar, avisa que a opção é invalida
        print("Opção inválida.")
        