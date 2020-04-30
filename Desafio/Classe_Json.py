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
        dict = {
            "numero_casa": self.casa, 
            "token": self.token, 
            "cifrado": self.cifrado, 
            "decifrado": self.decifrado, 
            "resumo_criptografico": self.resumo_criptografico
            }
        print(dict)