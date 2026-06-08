from .Pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, titulo):
        super().__init__(nome)
        self.titulo = titulo

    def exibir_dados(self):
        return f"{self.titulo} {self.nome}"
