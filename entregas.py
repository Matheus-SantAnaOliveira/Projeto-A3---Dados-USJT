from IPython.display import clear_output
import matplotlib.pyplot as plt
import pandas as pd
from recebe_valor_alternativa import recebe_valor_submenu

#sistema é por padrão, FALSE, só se altera caso seja chamado pelo sistema e não por linha - linha, (via submenu)
# Um gráfico de pizza que exibe o status de entrega
def analise_status_entregas(df, sistema = False):
    # Verificar se o código está sendo chamado pelo sistema
    if(sistema == True):
        # Limpa a tela
        clear_output(wait=True)
    # Pega o tamanho total de entregas
    total_entregas = len(df)
    # Conta a quantidade de valores do "Status entrega"
    estados = df['Status da Entrega'].value_counts()
    # Exibe a porcentagem de entregas p/ estado
    porcentagens = (estados / total_entregas * 100).round(2)
    # Cria uma figura e um ax
    fig1, ax1 = plt.subplots()
    # Configura o ax
    ax1.pie(porcentagens, labels=porcentagens.index, autopct='%1.1f%%', startangle=90)
    # Garante que o gráfico de pizza seja circular(segundo a documentação :D)
    ax1.axis('equal')
    # Exibe o gráfico
    plt.show()
    # Verifica se o sistema está sendo usado
    if(sistema == True):
        input("\nPressione Enter para voltar ao menu...")
        
# Método responsável por exibir o gráfico de análise de entregas p/ estado(Destino)
def analise_entregas_estado(df, sistema = False):
    # Verificar se o código está sendo chamado pelo sistema
    if(sistema == True):
        # Limpa a tela
        clear_output(wait=True)
    # Conta a quantidade de destinos
    counts = df['Destino'].value_counts()
    #Colore o Dashboard
    counts.plot(kind='bar', color='lightgreen')
    # Coloca o titulo no gráfico
    plt.title('Entregas por Destino')
    # Passa o titulo do eixo Y
    plt.ylabel('Contagem')
    # ajeita o eixo do gráfico
    plt.xticks(rotation=30, ha='right')
    # Ajusta o layout para evitar sobreposição
    plt.tight_layout()
    # Exibe o gráfico
    plt.show()
    # Verifica se o sistema está sendo usado
    if(sistema == True):
        input("\nPressione Enter para voltar ao menu...")
    
def analise_entregas_por_data(df, sistema = False):
    # Verificar se o código está sendo chamado pelo sistema
    if(sistema == True):
        # Limpa a tela
        clear_output(wait=True)
    # Passa o campo data de entrega pro Data frame
    df['Data'] = pd.to_datetime(df['Data'])  # Data estimada de entrega
    # Faz um "Count" diferente, pois se trata de data, e organiza o indicde por isso
    counts = df['Data'].dt.date.value_counts().sort_index()
    # Escolhe o tipo de grafico
    counts.plot(kind='line', marker='o')
    # Passa o titulo do grafico
    plt.title('Entregas Estimadas por Data')
    # Passa o testo da horizontal
    plt.xlabel('Data Estimada')
    # Passa o texto na vertical
    plt.ylabel('Número de Entregas')
    # Ajusta os nomes
    plt.xticks(rotation=45)
    # Ajusta o layout para evitar sobreposição
    plt.tight_layout()
    # Exibe o gráfico
    plt.show()
    # Verifica se o sistema está sendo usado
    if(sistema == True):
        input("\nPressione Enter para voltar ao menu...")
    
# Grafico pra exibir a % de entregas atrasadas
def analise_entregas_atrasadas(df, sistema = False):
    # Verificar se o código está sendo chamado pelo sistema
    if(sistema == True):
        # Limpa a tela
        clear_output(wait=True)
    # Passa o campo data de entrega pro Data frame
    df['Data'] = pd.to_datetime(df['Data'])  
    # Campo data de entrega + Tempo de atraso
    df['Data de Entrega'] = df['Data'] + pd.to_timedelta(df['Tempo'], unit='D')
    # Passa pra um DF as que o tempo de atraso, for maior que a data estimada de entrega
    df['Atrasada'] = df['Data de Entrega'] > df['Data']
    # Conta a quantidade de atrasadas
    counts = df['Atrasada'].value_counts()
    # Passa pros indices
    counts.index = ['No Prazo', 'Atrasada']
    # Estiliza o Gráfico
    counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['lightblue', 'salmon'])
    # Passa o titulo do grafico
    plt.title('Entregas Atrasadas vs No Prazo')
    # Titulo 2
    plt.ylabel('')
    # Ajusta o layout para evitar sobreposição
    plt.tight_layout()
    # Exibe o gráfico
    plt.show()
    # Verifica se o sistema está sendo usado
    if(sistema == True):
        input("\nPressione Enter para voltar ao menu...")
def analise_motivos_atrasos(df, sistema=False):
    # Verificar se o código está sendo chamado pelo sistema
    if(sistema == True):
        # Limpa a tela
        clear_output(wait=True)

    # Passa o campo data de entrega pro Data frame
    df['Data'] = pd.to_datetime(df['Data']) 
    # Campo data de entrega + Tempo de atraso
    df['Data de Entrega'] = df['Data'] + pd.to_timedelta(df['Tempo'], unit='D')
    # Passa pra um DF o que for maior que a data estimada de entrega
    df['Atrasada'] = df['Data de Entrega'] > df['Data']
    # Confirma se tem atrasadas
    df_atrasadas = df[df['Atrasada'] == True]
    # Verifica se não tem atrasadas
    if df_atrasadas.empty:
        print("Nenhuma entrega atrasada encontrada.")
    else:
        # Se tiver
        # Passa os motivos pra uma váriavel
        motivos = df_atrasadas['Incidente de Trânsito'].value_counts()
        # Deixa o gráfico decorado
        motivos.plot(kind='bar', color='salmon', edgecolor='black')
        # Passa o titulo do grafico
        plt.title('Motivos dos Atrasos nas Entregas')
        # Passa o testo da horizontal
        plt.xlabel('Motivo')
        # Passa o texto na vertical
        plt.ylabel('Quantidade')
        # Deixa mais bonito os nomes
        plt.xticks(rotation=45, ha='right')
        # Ajusta o layout para evitar sobreposição
        plt.tight_layout()
        # Exibe o gráfico
        plt.show()
        # Verifica se o sistema está sendo usado
    if(sistema == True):
        input("\nPressione Enter para voltar ao menu...")
def analise_tempos_entrega(df, sistema=False):
    # Verificar se o código está sendo chamado pelo sistema
    if(sistema == True):
        # Limpa a tela
        clear_output(wait=True)
    # Seta campo data
    df['Data'] = pd.to_datetime(df['Data'], dayfirst=True)
    # Campo data de entrega + Prazo de entrega
    df['Data de Entrega Original'] = df['Data'] + pd.to_timedelta(df['Prazo de Entrega (dias)'], unit='D')
    # Campo data de entrega + Tempo de atraso
    df['Data de Entrega Com Atraso'] = df['Data de Entrega Original'] + pd.to_timedelta(df['Tempo'], unit='D')
    
    # Passa pra um DF as que o tempo de atraso, for maior que a data estimada de entrega
    df['Atrasada'] = df['Data de Entrega Com Atraso'] > df['Data de Entrega Original']
    
    # Filtra o DataFrame para obter apenas as entregas atrasadas
    df_atrasadas = df[df['Atrasada'] == True]
    
    # Verifica se não há entregas atrasadas
    if df_atrasadas.empty:
        print("Nenhuma entrega atrasada encontrada.")
    else:
        # Se houver entregas atrasadas, seleciona as colunas relevantes para análise
        tempos = df_atrasadas[['Centro de Distribuição', 'Destino', 'Data de Entrega Original',
                               'Data de Entrega Com Atraso', 'Tempo', 'Prazo de Entrega (dias)',
                               'Incidente de Trânsito']].copy()
        
        fig, ax = plt.subplots()
        ax.axis('off')

        col_labels = ['Centro de Distribuição', 'Destino', 'Data de Entrega\nOriginal',
                      'Data de Entrega\nCom Atraso', 'Atraso(dias)', 'Prazo de Entrega\n(dias)',
                      'Incidente de Trânsito']
         # Cria a tabela com os dados filtrados, rótulos e formatação personalizada
        table = ax.table(
            cellText=tempos.values,
            colLabels=col_labels,
            loc='center',
            cellLoc='center',
            colWidths=[0.2, 0.2, 0.3, 0.3, 0.15, 0.2, 0.2]
        )
        # Define o tamanho da fonte 
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        # Define tamanho da escala
        table.scale(1.2, 1.5)
        # Ajusta o tamanho da figura de acordo com o conteúdo da tabela
        bbox = table.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
        fig.set_size_inches(bbox.width, bbox.height)
         # Exibe a tabela na tela
        plt.show()

    # Verifica se o sistema está sendo usado
    if(sistema == True):
        input("\nPressione Enter para voltar ao menu...")
   #Submenu pra facilitar o código do sistema         
def submenu_entregas(df):
        # Exibe opções
        print("\n--- SUBMENU: ENTREGAS ---")
        print("a - Entregas por Destino")
        print("b - Entregas por Data")
        print("c - Entregas Atrasadas")
        print("d - Motivo Atraso")
        print("e - Tabela de Atrasos Completa")
        print("0 - Voltar")
        #Epécie de "Switch - Case" pra selecionar um deles
        # Trata a opção escolhida
        opt = recebe_valor_submenu()
        if opt == 'a':
            analise_entregas_estado(df, True)
        elif opt == 'b':
            analise_entregas_por_data(df, True)
        elif opt == 'c':
            analise_entregas_atrasadas(df, True)
        elif opt == 'd':
            analise_motivos_atrasos(df, True)
        elif opt == 'e':
            analise_tempos_entrega(df, True)
        elif opt == '0':
            return
        else:
            #Se não encontrar, avisa que a opção é invalida
            print("Opção inválida.")

