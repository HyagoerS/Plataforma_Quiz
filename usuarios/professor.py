'''from conteudo.questao import Criacao_Questoes
from conteudo.multipla_escolha import MultiplaEscolha
from estrutura.excecoes import DataInvalida
from datetime import datetime, timedelta'''
from conteudo.tema import GerenciadorTema
from .usuario import Usuario
from conteudo.tema import Tema

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



class Professor(Usuario):
    def __init__(self, id, nome, email, senha, departamento):
        super().__init__(id, nome, email, senha)
        self.departamento = departamento


    def criar_tema(self, titulo, descricao, sistema):
        novo_tema = Tema(titulo, descricao)
        sistema.adicionar_tema(novo_tema)
        print(f"Professor {self.nome} criou o Tema: {titulo}")
        return novo_tema


    def criar_questao(self, enunciado, pontuacao, opcoes, indice_correto, sistema):
        from conteudo.multipla_escolha import QuestaoMultiplaEscolha
        questao = QuestaoMultiplaEscolha(0, enunciado, pontuacao, opcoes, indice_correto)
        questao._id = sistema.adicionar_questao(questao)
        return questao

  