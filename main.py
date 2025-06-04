from IPython.display import clear_output
from menu_dados_base import abre_menu_principal
from dados import carregar_dados, carrega_dados_veiculos, carrega_dados_demandas, carrega_dados_financeiro
def main():
    # Carrega os data frames
    df = carregar_dados()
    df_veiculos = carrega_dados_veiculos()
    df_demanda = carrega_dados_demandas()
    df_financeiro = carrega_dados_financeiro()
    while True:
        # Abre o menu principal
        sair = abre_menu_principal(df, df_veiculos, df_demanda, df_financeiro)
        if(sair == 0):
            break

if __name__ == '__main__':
    main()
