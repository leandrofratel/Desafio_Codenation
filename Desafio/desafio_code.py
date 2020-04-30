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
    return novo_cifrado.upper()

def encode_hash(frase): # Codifica e retorna a mensagem em sha1.
    # Codifica em sha1.
    return hashlib.sha1(str(frase).encode('utf-8')).hexdigest()
    
codenation = requisitar_e_salvar('31d49c4bec438e1e41cc7eec111fb4153ae67647')
print(encode_hash(codenation))

# token: 31d49c4bec438e1e41cc7eec111fb4153ae67647