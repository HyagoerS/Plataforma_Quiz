from conteudo import GerenciadorTema
from conteudo import tema

class Professor(tema):
    def __init__(self, nome):
        super().__init__(nome)
        self.gerenciador_temas = GerenciadorTema()

class Professor:
    def __init__(self):
        self.gerencia_temas = GerenciadorTema()

    def criar_tema(self, nome):
        self.gerencia_temas.criar_tema(nome)

                                       
self.gestao.criar_tema("História")
self.gestao.editar_tema("História", "História Geral")
self.gestao.excluir_tema("Matemática")
