import json

def captura_cifra(nome_do_arquivo):
    # Salva a requisição em json.
    with open(nome_do_arquivo, 'r') as file:
        relatorio = json.load(file)
        return relatorio["cifrado"]

def captura_casa(nome_do_arquivo):
    # Salva a requisição em json.
    with open(nome_do_arquivo, 'r') as file:
        relatorio = json.load(file)
        return relatorio["numero_casas"]

def captura_token(nome_do_arquivo):
    # Salva a requisição em json.
    with open(nome_do_arquivo, 'r') as file:
        relatorio = json.load(file)
        return relatorio["token"]


cifra = captura_cifra('original_answer.json')
casa = captura_casa('original_answer.json')
token = captura_casa('original_answer.json')

print(cifra)
print(casa)
print(token)