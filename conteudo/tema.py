#RF 1
class Tema:
    def __init__(self, nome):
        self.nome = nome


class GerenciadorTema:
    def __init__(self):
        self.topicos = []

    def criar_tema(self, nome):
        self.topicos.append(Tema(nome))

    def editar_tema(self, nome_antigo, nome_novo):
        for topico in self.topicos:
            if topico.nome == nome_antigo:
                topico.nome = nome_novo
                return True
        return False

    def excluir_tema(self, nome, tema):
        for tema in self.temas:
            if tema.nome == nome:
                self.topicos.remove(tema)
                return