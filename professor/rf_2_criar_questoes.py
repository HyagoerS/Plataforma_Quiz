class Questao:
    def __init__(self, pergunta):
        self.pergunta = pergunta
        self.opcoes = []



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
