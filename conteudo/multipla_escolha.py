from .questao import Questao # Importa a classe mãe

class QuestaoMultiplaEscolha(Questao):
    def __init__(self, id_questao, enunciado, pontuacao, opcoes, indice_correto):
        super().__init__(id_questao, enunciado, pontuacao)
        self.opcoes = opcoes # Lista de alternativas
        self.__indice_correto = indice_correto # Encapsulamento (Privado)

    def corrigir(self, resposta_aluno):
        # Se a resposta do aluno (ex: 'A') for igual à correta, ganha os pontos
        if resposta_aluno == self.__indice_correto:
            return self.pontuacao
        return 0
        
    def get_resposta_correta(self):
        return self.__indice_correto