class Questao:
    def __init__(self, id_questao, enunciado, pontuacao):
        self._id = id_questao 
        self.enunciado = enunciado
        self.pontuacao = pontuacao

    def corrigir(self, resposta_aluno):
        raise NotImplementedError("As classes filhas devem implementar a correção.")