from conteudo.tema import GerenciadorTema
from .usuario import Usuario
from conteudo.tema import Tema



class Professor(Usuario):
    def __init__(self, id, nome, email, senha, departamento):
        super().__init__(id, nome, email, senha)
        self.departamento = departamento


    def criar_tema(self, titulo, descricao, sistema):
        novo_tema = Tema(titulo, descricao)
        sistema.adicionar_tema(novo_tema)
        print(f"Professor {self.nome} criou o Tema: {titulo}")
        return novo_tema





  