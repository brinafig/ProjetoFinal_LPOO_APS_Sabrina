class Avaliacao:
    def __init__(self, nome, peso, nota):
        self.nome = nome
        self.peso = peso
        self.nota = nota

    def exibir_dados(self):
        return f"{self.nome}: Peso = {self.peso}, Nota = {self.nota}"
