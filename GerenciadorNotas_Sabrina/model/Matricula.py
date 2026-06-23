from .Status import Status


class Matricula:

    def __init__(self, aluno, disciplina, presencas=0, status=Status.RECUPERACAO, id=None):
        self.id = id
        self.aluno = aluno
        self.disciplina = disciplina
        self.presencas = presencas
        self.status = status

    def registrar_presenca(self):
        self.presencas += 1

    def calcular_frequencia(self):

        if self.disciplina.total_aulas == 0:
            return 0

        return (self.presencas / self.disciplina.total_aulas) * 100

    def definir_status(self, media):

        frequencia = self.calcular_frequencia()

        if frequencia < 75:
            self.status = Status.REPROVADO

        elif media >= 6:
            self.status = Status.APROVADO

        else:
            self.status = Status.RECUPERACAO

    def exibir_dados(self):

        return (
            f"Aluno: {self.aluno.nome}\n"
            f"Disciplina: {self.disciplina.nome}\n"
            f"Presenças: {self.presencas}\n"
            f"Frequência: {self.calcular_frequencia():.1f}%\n"
            f"Status: {self.status.value}"
        )