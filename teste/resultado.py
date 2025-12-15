from usuarios.aluno import Aluno

class Resultado:
    def __init__(self, teste_aluno, gabarito):
        self.teste_aluno = teste_aluno
        self.__gabarito = gabarito



    def exibir_pontuacao(self,):
        return
    
    def exibir_gabarito(self, gabarito):
        return

    def coletar_resultado(self, calcular):
        return
    
class Resultado:
    def __init__(self, id_teste, id_aluno, nota_final, respostas_dadas):
        self.id_teste = id_teste
        self.id_aluno = id_aluno
        self.__nota_final = nota_final # Privado
        self._respostas_dadas = respostas_dadas # Protegido

    # RF9: Visualização de Desempenho
    def get_nota_final(self):
        return self.__nota_final

    # RF5: Correção Manual (Professor pode atribuir nota final, mas aqui está a nota calculada)
    def atribuir_nota_final(self, nova_nota):
        # Este método seria usado pelo Professor (RF5)
        self.__nota_final = nova_nota