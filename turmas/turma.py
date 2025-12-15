"""from usuarios.aluno import Aluno
from usuarios.professor import Professor
from estrutura.excecoes import PermissaoNegada

class Turma:
    def __init__(self, id, nome):
        self._id = id 
        self.nome = nome
        self._alunos = []    # Lista de objetos Aluno
        self._professores = [] # Lista de objetos Professor

    # RF12: Associar Turmas a Alunos/Professores
    def adicionar_membro(self, usuario):
        if isinstance(usuario, Aluno):
            self._alunos.append(usuario)
        elif isinstance(usuario, Professor):
            self._professores.append(usuario)
        else:
            # Tratamento de exceção
            raise PermissaoNegada("Apenas Alunos ou Professores podem ser adicionados a uma Turma.")"""