from model.Aluno import Aluno
from model.Disciplina import Disciplina
from model.AvaliacaoFactory import AvaliacaoFactory
from model.NotificadorEmail import NotificadorEmail
from model.Professor import Professor


def main():

    aluno = Aluno("Sabrina", "20242PF.CC0019")
    print(aluno.exibir_dados())
    print("\nDisciplinas: TOO e Banco de Dados I\n")

    email = "sabrinaalmeida.pf019@academico.ifsul.edu.br"


    prof_too = Professor("Vanessa", "Doutora")
    too = Disciplina("TOO", prof_too)
    too.registrar_observador(NotificadorEmail(email))

    too.adicionar_avaliacao(AvaliacaoFactory.criar_avaliacao("prova", 10, 5))
    too.adicionar_avaliacao(AvaliacaoFactory.criar_avaliacao("trabalho", 8, 5))

    too.definir_status()
    aluno.adicionar_disciplina(too)


    prof_bd = Professor("Alexandre", "Doutor")
    bd = Disciplina("Banco de Dados I", prof_bd)
    bd.registrar_observador(NotificadorEmail(email))

    bd.adicionar_avaliacao(AvaliacaoFactory.criar_avaliacao("prova", 5, 6))
    bd.adicionar_avaliacao(AvaliacaoFactory.criar_avaliacao("trabalho", 5, 4))

    bd.definir_status()      
    bd.aplicar_reavaliacao(8) 

    aluno.adicionar_disciplina(bd)


    print("\n------- RESULTADOS --------\n")

    for disc in aluno.disciplinas:
        print(disc.exibir_dados())
        print()


if __name__ == "__main__":
    main()
