

class Questao:
    def __init__(self, id_questao, enunciado, pontuacao):
        self._id = id_questao 
        self.enunciado = enunciado
        self.pontuacao = pontuacao


    def corrigir(self, resposta_aluno):
        raise NotImplementedError("Método 'corrigir' deve ser implementado.")


class Criacao_Questoes:
    def __init__(self):
        pass

    def criar_pergunta(self, questao):
        pergunta = input("Modificiar para marcar e não escrever: ")
        return questao(pergunta)

    def inserir_opcoes(self, questao):
        print("Marque uma das opções resposta: ")


    def indicar_reposta(self, questao):
        return

