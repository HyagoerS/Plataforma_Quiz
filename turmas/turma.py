from usuarios.professor import Professor
from estrutura.excecoes import PermissaoNegada
from usuarios.aluno import Aluno

class Turma:
    def __init__(self, id, nome):
        self._id = id 
        self.nome = nome
        self._alunos = []   
        self._professores = [] 



