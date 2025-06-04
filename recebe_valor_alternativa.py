def recebe_valor():
    # Recebe o valor e tira espaços vazios
    escolha = input("Escolha uma opção: ").strip()
    return escolha

def recebe_valor_submenu():
    # Recebe o valor, e tira espaços vazios e deixa minusculo
    escolha = input("Escolha uma opção: ").strip().lower()
    return escolha