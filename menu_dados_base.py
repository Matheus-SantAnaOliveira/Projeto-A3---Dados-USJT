# Importações
from IPython.display import clear_output
from entregas import submenu_entregas
from rotas import submenu_rotas
from custos import submenu_custos
from veiculos import submenu_veiculos
from recebe_valor_alternativa import recebe_valor
from demandas import submenu_demandas
from financeiro  import submenu_financeiro
# Sub Menu base pro sistema
def abre_menu_principal(df, df_veiculos, df_demandas, df_financeiro):
    # Limpa a tela
    clear_output(wait=True)
    print("\n=== MENU PRINCIPAL ===")
    print("1 - Verificar Entregas")
    print("2 - Verificar Rotas")
    print("3 - Verificar Custos")
    print("4 - Análise de Veículos")
    print("5 - Análise de Demandas")
    print("6 - Análise de Financeiro")
    print("0 - Sair")
    # Recebe o valor
    escolha = recebe_valor()
     # Espécie de "Switch - Case" pra selecionar Outro SubMenu
    if escolha == '0':
        print("Encerrando o sistema. Até mais!")
        return 0
    elif escolha == '1':
        submenu_entregas(df)
        return 1
    elif escolha == '2':
        submenu_rotas(df)
        return 2
    elif escolha == '3':
         submenu_custos(df)
         return 3
    elif escolha == '4':
        submenu_veiculos(df_veiculos)
        return 4
    elif escolha == '5':
        submenu_demandas(df_demandas)
        return 5
    elif escolha == '6':
        submenu_financeiro(df, df_financeiro, df_veiculos)
    else:
        print("Opção inválida. Tente novamente.")
        return 6