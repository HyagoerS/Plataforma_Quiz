#RF2

class Questao:
    def __init__(self):
        pass

class Criacao_Questoes:
    def __init__(self):
        pass

    def criar_pergunta(self, questao):
        pergunta = input("Moficiar para marcar e não escrever: ")
        return questao(pergunta)

    def inserir_opcoes(self, questao):
        print("Digite uma das opções resposta: ")


    def indicar_reposta(self, questao):
        return