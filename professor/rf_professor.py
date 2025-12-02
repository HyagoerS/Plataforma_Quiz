#RF 1
class Topico:
    def __init__(self, nome):
        self.nome = nome

class GerenciadorTopicos:
    def __init__(self):
        self.topicos = []

    def criar_topico(self, nome):
        self.topicos.append(Topico(nome))

    def editar_topico(self, nome_antigo, nome_novo):
        for topico in self.topicos:
            if topico.nome == nome_antigo:
                topico.nome = nome_novo
                return True
        return False

    def excluir_topico(self, nome):
        for topico in self.topicos:
            if topico.nome == nome:
                self.topicos.remove(topico)
                return

gestao = GerenciadorTopicos()

gestao.criar_topico("Matemática")
gestao.criar_topico("História")

gestao.editar_topico("História", "História Geral")

gestao.excluir_topico("Matemática")

#RF 2

class Criacao_Questoes:
    def __init__(self):
        pass

    def criar_pergunta(self):
        pergunta = input("Digite o texto da pergunta: ")
        return Questao(pergunta)

    def inserir_opcoes(self, questao):
        print("Digite uma das opções resposta: ")


    def indicar_reposta(self, questao):
        return


#RF 3