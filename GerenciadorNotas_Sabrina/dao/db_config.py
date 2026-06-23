import psycopg2
from psycopg2 import Error


class DatabaseConfig:
    @staticmethod
    def conectar():
        try:
            conexao = psycopg2.connect(
                user = "postgres",
                password = "postgres",
                host = "localhost",
                port = "5432",
                database = "lpoo_projeto_sabrinafigueiredo"
            )
            return conexao
        except Error as e:
            print(f"Erro ao conectar o banco de dados: {e}")
            return None
