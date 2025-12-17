


class AplicarTeste:
    def __init__(self, id, titulo, questoes_com_pontuacao, id_turma, inicio, termino, tempo_max_minutos, id_professor):
        self._id = id
        self.titulo = titulo
        self._questoes = questoes_com_pontuacao
        self.id_turma = id_turma
        self._data_inicio = inicio 
        self._data_termino = termino
        self._tempo_maximo_minutos = tempo_max_minutos
        self.id_professor = id_professor
        


    def adicionar_questoes(self, questao):
        self.questoes.append(questao)


    def exibir_teste(self):
        for teste, q in enumerate(self.lista_questoes, start=1):
            return f"{teste}. {q.questao}"

    def aplicar(self):
        for questao in self.teste.lista_questao:
            print(questao.questao)
            self.re

    def associar_turmas(self):
        return
    
    def definir_prazo(self, inicio, fim):
        return

    def definir_tempo(self, minutos):
        return

