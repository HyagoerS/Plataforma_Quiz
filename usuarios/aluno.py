from .usuario import Usuario

class Aluno(Usuario):
    def __init__(self, id, nome, email, senha, turma="Geral"):
        # super() passa os dados para a classe Usuario
        super().__init__(id, nome, email, senha)
        self.turma = turma
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)


