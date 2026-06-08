from .Observer import Observer

class NotificadorEmail(Observer):

    def __init__(self, email_destino):
        self.email_destino = email_destino

    def atualizar(self, mensagem):
        print(f"[EMAIL PARA {self.email_destino}] {mensagem}")
