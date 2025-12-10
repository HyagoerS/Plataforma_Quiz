'''from conteudo.questao import Criacao_Questoes
from conteudo.multipla_escolha import MultiplaEscolha'''
from conteudo.tema import GerenciadorTema

class Professor():
    def __init__(self, nome):
        super().__init__(nome)
        self.gerenciador_temas = GerenciadorTema()

class Professor:
    def __init__(self):
        self.gerencia_temas = GerenciadorTema()

    def criar_tema(self, nome):
        self.gerencia_temas.criar_tema(nome)

                     
gestao.criar_tema("História")
gestao.editar_tema("História", "História Geral")
gestao.excluir_tema("Matemática")
