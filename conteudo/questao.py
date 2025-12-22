class Questao:
    def __init__(self, id_questao, enunciado, pontuacao):
        self._id = id_questao 
        self.enunciado = enunciado
        self.pontuacao = pontuacao

    def corrigir(self, resposta_aluno):
        raise NotImplementedError("Método 'corrigir' deve ser implementado nas subclasses.")

# Aqui entra a Herança (RF2) baseada no seu código
class QuestaoMultiplaEscolha(Questao):
    def __init__(self, id_questao, enunciado, pontuacao, opcoes, resposta_correta):
        # O super() reaproveita o que você já fez na Questao original
        super().__init__(id_questao, enunciado, pontuacao)
        self.opcoes = opcoes  # Uma lista ['Opção A', 'Opção B'...]
        self.__resposta_correta = resposta_correta # Atributo privado

    def corrigir(self, resposta_aluno):
        # Implementando o método que você deixou preparado
        return resposta_aluno == self.__resposta_correta