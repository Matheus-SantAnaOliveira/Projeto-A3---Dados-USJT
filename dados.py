# Importações
import pandas as pd
# Métodos que carrega as tabelas

# Método que carrega a tabela de entregas
def carregar_dados():
    # Le o excel
    df = pd.read_excel('Datalog.xlsx', sheet_name='Entregas', parse_dates=['Data'])
    # Evita um erro e um Warning
    df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y', errors='coerce')
    # Retorna o Data Frame
    return df
    
# Método que carrega a tabela de Veiculos
def carrega_dados_veiculos():
    # Le o excel
    df = pd.read_excel('Datalog.xlsx', sheet_name='Veiculos')
    # Retorna o Data Frame
    return df

# Método que carrega a tabela de Demandas
def carrega_dados_demandas():
    # Le o excel
    df = pd.read_excel('Datalog.xlsx', sheet_name='Demandas', parse_dates=['Data'])
    # Evita um erro e um Warning
    df['Data'] = pd.to_datetime(df['Data'], errors='coerce') 
    # Retorna o Data Frame
    return df

# Método que carrega a tabela de Financeiro
def carrega_dados_financeiro():
    # Le o excel
    df = pd.read_excel('Datalog.xlsx', sheet_name='Financeiros')
    # Retorna o Data Frame
    return df
