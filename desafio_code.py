import requests
import json
import hashlib
from Classe_Json import Desafio

def requisitar_e_salvar(c_token): # Cria uma cópia da requisição e retorna a mensagem decriptada.
    # Realiza a requisição.
    api = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=' + c_token
    requisito = requests.get(api)
    req = requisito.json()

    # Salva a requisição em json.
    with open('original_answer.json', 'w') as file:
        json.dump(req, file)

    # Captura as chaves da requisição.
    requisito_casas = req['numero_casas']
    requisito_cifrado = req['cifrado']
    
    # Realiza a decriptação
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    casas = requisito_casas
    novo_cifrado = ''
    
    for letra in requisito_cifrado:
        if letra in alfabeto:
            indice_letra = alfabeto.index(letra)
            novo_cifrado += alfabeto[(indice_letra - casas) % len(alfabeto)]
        else:
            novo_cifrado += letra
    return novo_cifrado.lower()

def encode_hash(frase): # Codifica e retorna a mensagem em sha1.
    # Codifica em sha1.
    return hashlib.sha1(str(frase).encode('utf-8')).hexdigest()

def captura_cifra(nome_do_arquivo): # Captura Cifra
    # Salva a requisição em json.
    with open(nome_do_arquivo, 'r') as file:
        relatorio = json.load(file)
        return relatorio["cifrado"]

def captura_casa(nome_do_arquivo): # Captura Casa
    # Salva a requisição em json.
    with open(nome_do_arquivo, 'r') as file:
        relatorio = json.load(file)
        return relatorio["numero_casas"]

def postar(url, filename):
    with open(filename, 'r') as file:
        answer_content = file.read()

    files = {'answer': ('answer', answer_content, 'aplication/json')}

    return requests.post(url, files=files).text
    

original_token = '31d49c4bec438e1e41cc7eec111fb4153ae67647'
inicio = requisitar_e_salvar(original_token)

resumo_criptografico = encode_hash(inicio)
cifra = captura_cifra('original_answer.json')
casa = captura_casa('original_answer.json')

fim = Desafio(casa, original_token, cifra, inicio, resumo_criptografico)
fim.criar_dicionario()

print(postar('https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=31d49c4bec438e1e41cc7eec111fb4153ae67647','answer.json'))