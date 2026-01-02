from usuarios.professor import Professor
from usuarios.aluno import Aluno

class Turma:
    def __init__(self, id, nome):
        self._id = id 
        self.nome = nome
        self._alunos = []   
        self._professores = [] 

    def adicionar_aluno(self, aluno):
        """Adiciona um objeto da classe Aluno à turma"""
        self._alunos.append(aluno)

    def total_alunos(self):
        """Retorna a quantidade de alunos matriculados"""
        return len(self._alunos)



