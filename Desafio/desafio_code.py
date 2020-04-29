import requests
import json

class Desafio():
    """Inicializa os atributos do desafio."""
    def __init__(self, casa, token, cifrado, decifrado, resumo_criptografico):
        # Define os objetos.
        self.casa = casa
        self.token = token
        self.cifrado = cifrado
        self.decifrado = decifrado
        self.resumo_criptografico = resumo_criptografico

    def criar_dicionario(self):
        # Escreve um dicionário de acordo com os objetos.
        dict = {"numero_casa":self.casa, "token": self.token, "cifrado": self.cifrado, "decifrado":self.decifrado, "resumo_criptografico":self.resumo_criptografico}
        print(dict)

# Realiza a requisição.
def inicio(c_token):
    answer = open('answer2.json', 'w')
    api = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=' + c_token
    requisito = requests.get(api)
    print(requisito.text, file= answer)

# Realiza a descriptação da mensagem.
def descriptar(mensagem):
    # Condições para o funcionamento da função.
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    casa = 3
    # Função.
    cripto = ''
    for c in mensagem:
        if c in alfabeto:
            c_index = alfabeto.index(c)
            cripto = cripto + alfabeto[(c_index - casa) % len(alfabeto)]
        else:
            cripto = cripto + c
    print(cripto.upper())


inicio(input('Entre com o token: '))
descriptar(input('Informe a mensagem: '))

"""
teste = Desafio(10,"token_do_usuario","texto criptografado","aqui vai o texto decifrado","aqui vai o resumo")
teste.criar_dicionario()
"""

# token: 31d49c4bec438e1e41cc7eec111fb4153ae67647