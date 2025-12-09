#RF1
class Tema:
    def __init__(self, nome):
        self.nome = nome


class GerenciadorTema:
    def __init__(self):
        self.temas = []

    def criar_tema(self, nome):
        self.temas.append(Tema(nome))

    def editar_tema(self, nome_antigo, nome_novo):
        for tema in self.temas:
            if tema.nome == nome_antigo:
                tema.nome = nome_novo
                return True
        return False

    def excluir_tema(self, nome, tema):
        for tema in self.temas:
            if tema.nome == nome:
                self.temas.remove(tema)
                return