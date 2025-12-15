'''from turmas.turma import Turma'''


class AplicarTeste:
    def __init__(self, data, horario, tempo_maximo):
        self.questoes = []
        self.pontuacao = []
        self.data = data
        self.horario = horario
        self.tempo_maximo = tempo_maximo


    def adicionar_questoes(self, questoes):
        self.questoes.append(questoes)



    def associar_turmas(self):
        return
    
    def definir_prazo(self, inicio, fim):
        return

    def definir_tempo(self, minutos):
        return

'''from datetime import datetime
from estrutura.excecoes import DataInvalida

class Teste:
    def __init__(self, id, titulo, questoes_com_pontuacao, id_turma, inicio, termino, tempo_max_minutos, id_professor):
        self._id = id # Protegido
        self.titulo = titulo
        # { Questao_Objeto: pontuacao_definida } (RF3)
        self._questoes = questoes_com_pontuacao
        self.id_turma = id_turma
        
        # RF4: Publicação e Prazo
        self._data_inicio = inicio 
        self._data_termino = termino
        self._tempo_maximo_minutos = tempo_max_minutos
        self.id_professor = id_professor
        
    def esta_disponivel(self):
        agora = datetime.now()
        # Verifica se está no intervalo de datas
        return self._data_inicio <= agora <= self._data_termino

    def corrigir_respostas(self, respostas_aluno):
        # RF10: Cálculo do resultado Total do Quiz (Automático)
        nota_total = 0
        
        for i, (questao, pontuacao_definida) in enumerate(self._questoes.items()):
            # A resposta do aluno é o índice que ele escolheu na questão i
            resposta_dada = respostas_aluno[i]
            
            # Chama o método corrigir da Questão (Polimorfismo)
            nota_da_questao = questao.corrigir(resposta_dada) 
            
            # Garante que a nota não exceda a pontuação máxima definida (RF3)
            nota_total += min(nota_da_questao, pontuacao_definida)
            
        return nota_total
        
    def verificar_prazo(self, tempo_decorrido):
        # RF8: Controle de Tempo / Envio automático
        if tempo_decorrido > self._tempo_maximo_minutos:
            return True # O tempo acabou, enviar automaticamente
        return False'''
    
    


    

