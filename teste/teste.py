


class AplicarTeste:
    def __init__(self, id, titulo, questoes_com_pontuacao, id_turma, inicio, termino, tempo_max_minutos, id_professor):
        self._id = id
        self.titulo = titulo
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


    def associar_turmas(self):
        return
    
    def definir_prazo(self, inicio, fim):
        return

    def definir_tempo(self, minutos):
        return

class Teste:
    # O molde agora só precisa de um título e um gabarito
    def __init__(self, titulo, gabarito): 
        self.titulo = titulo
        self.gabarito = gabarito

    # Um único método que serve para QUALQUER teste
    def calcular_resultado(self, respostas_aluno):
        pontos = 0
        for i in range(len(self.gabarito)):
            # Compara com o gabarito DESTE objeto específico
            if respostas_aluno[i] == self.gabarito[i]:
                pontos += 2.5
        return pontos

# --- CRIAÇÃO DOS OBJETOS ---

# Gabarito de Jogos
gab_jogos = ["clair-obscur", "clair-obscur", "clair-obscur", "hollow-knight-silksong"]
# Gabarito Geral
gab_geral = ["russia", "famosas", "vinci", "independencia"]

# Criamos dois objetos diferentes usando o MESMO molde (Classe)
meu_teste_jogos = Teste("Quiz de Games 2025", gab_jogos)
meu_teste_geral = Teste("Quiz de Perguntas Gerais", gab_geral)