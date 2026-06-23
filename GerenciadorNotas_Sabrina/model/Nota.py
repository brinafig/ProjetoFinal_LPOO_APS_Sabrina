class Nota:
    def __init__(self, valor, avaliacao_id, matricula_id, id=None):
        self.id = id
        self.valor = valor
        self.avaliacao_id = avaliacao_id
        self.matricula_id = matricula_id