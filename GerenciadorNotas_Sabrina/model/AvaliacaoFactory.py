from .Avaliacao import Avaliacao

class AvaliacaoFactory:

    @staticmethod
    def criar_avaliacao(tipo, nota, peso):
        nome = tipo.capitalize() + " 1"
        return Avaliacao(nome, peso, nota)
