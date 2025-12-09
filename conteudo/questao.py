#RF 2

class Criacao_Questoes:
    def __init__(self):
        pass

    def criar_pergunta(self, questao):
        pergunta = input("Digite o texto da pergunta: ")
        return questao(pergunta)

    def inserir_opcoes(self, questao):
        print("Digite uma das opções resposta: ")


    def indicar_reposta(self, questao):
        return