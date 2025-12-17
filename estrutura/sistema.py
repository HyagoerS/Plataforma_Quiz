'''from usuarios.professor import Professor
from conteudo.tema import Tema'''
from usuarios.aluno import Aluno
from turmas.turma import Turma


class Sistema:
    def __init__(self):
        self.usuarios = {}
        self.turmas = {}       
        self.temas = {}        
        self.testes_disponiveis = {} 
        self.resultados = {}   



    def cadastrar_aluno(self, nome, login, senha, email):
        aluno = Aluno(nome, login, senha, email)
        self.usuarios.append(aluno)
        return aluno


    def autenticar(self, email, senha):
        for usuario in self.usuarios:
            if usuario.email == email and usuario.senha == senha:
                return usuario
        return None


# RF: criar turma

    def criar_turma(self, nome, professor):
        turma = Turma(nome, professor)
        self.turmas.append(turma)
        return turma



    def adicionar_aluno_na_turma(self, id_turma, aluno):
        turma = self.turmas[id_turma]
        turma.adicionar_aluno(aluno)
        return turma


class Notas:
    def __init__(self, nota_aluno):
        self.nota_aluno = {}


    def buscar_nota(self):
        return
    

class AutenticarLogin:
    def __init__(self):
        pass


    def validar_login(self):
        return
    

    def testes_liberados(self):
        return
    



