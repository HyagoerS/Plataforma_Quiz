from usuarios.professor import Professor
from estrutura.excecoes import PermissaoNegada
from usuarios.aluno import Aluno

class Turma:
    def __init__(self, id, nome):
        self._id = id 
        self.nome = nome
        self._alunos = []   
        self._professores = [] 



    def adicionar_membro(self, usuario):
        if isinstance(usuario, Aluno):
            self._alunos.append(usuario)
        elif isinstance(usuario, Professor):
            self._professores.append(usuario)
        else:
            raise PermissaoNegada("Apenas Alunos ou Professores podem ser adicionados a uma Turma.")