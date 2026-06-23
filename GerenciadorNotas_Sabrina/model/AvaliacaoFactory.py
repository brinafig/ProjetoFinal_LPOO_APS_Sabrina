from .Avaliacao import Avaliacao

class AvaliacaoFactory:
    @staticmethod
    def criar_avaliacao(tipo, nota, peso, data=""):
        nome = tipo.capitalize()
        return Avaliacao(nome, peso, nota, data=data)
