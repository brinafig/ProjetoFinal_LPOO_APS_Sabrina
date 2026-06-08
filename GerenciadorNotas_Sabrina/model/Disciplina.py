from .Status import Status

class Disciplina:

    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor
        self.avaliacoes = []
        self.observadores = []
        self.media_final = None
        self.status = None
        self.reavaliacao = None

    def registrar_observador(self, obs):
        self.observadores.append(obs)

    def notificar(self, mensagem):
        for obs in self.observadores:
            obs.atualizar(mensagem)

    def adicionar_avaliacao(self, avaliacao):
        self.avaliacoes.append(avaliacao)

    def calcular_media(self):
        pesos = sum(a.peso for a in self.avaliacoes)
        total = sum(a.peso * a.nota for a in self.avaliacoes)
        self.media_final = total / pesos
        return self.media_final


    def definir_status(self):
        self.calcular_media()

        if self.media_final >= 6:
            self.status = Status.APROVADO
        else:
            self.status = Status.RECUPERACAO

        self.notificar(f"{self.nome}: {self.status.value}")


    def aplicar_reavaliacao(self, nota):
        self.reavaliacao = nota

        if nota >= 6:
            self.status = Status.APROVADO
        else:
            self.status = Status.REPROVADO

        self.notificar(f"{self.nome} após reavaliação: {self.status.value}")


    def exibir_dados(self):
        txt = f"\n{self.nome}:"
        txt += f"\nProfessor(a): {self.professor}"
        txt += "\nAvaliações:"

        for a in self.avaliacoes:
            txt += f"\n{a.exibir_dados()}"

        if self.reavaliacao is not None:
            txt += f"\nMédia final: {self.media_final:.1f}"
            txt += f"\nReavaliação: {self.reavaliacao}"
            txt += f"\nStatus: {self.status.value}"
        else:
            txt += f"\nMédia final: {self.media_final:.1f}"
            txt += f"\nStatus: {self.status.value}"

        return txt
