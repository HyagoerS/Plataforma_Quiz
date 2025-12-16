from .questao import Questao


class MultiplaEscolha:
    def __init__(self, lista_opcoes, reposta_correta):
        self.lista_opcoes = lista_opcoes
        self.reposta_correta = reposta_correta


    def adicionar_opcao(self, opcao):
        return

    def difinir_correta(self, indice):
        return


class QuestaoMultiplaEscolha(Questao):
    def __init__(self, id_questao, enunciado, pontuacao, opcoes, indice_correto):
        super().__init__(id_questao, enunciado, pontuacao)
        self.opcoes = opcoes
        self.__indice_correto = indice_correto



    def corrigir(self, resposta_aluno):
        if resposta_aluno == self.__indice_correto:
            return self.pontuacao
        return 0
        
    def get_resposta_correta(self):
        return self.__indice_correto