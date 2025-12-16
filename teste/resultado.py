from usuarios.aluno import Aluno

class Resultado:
    def __init__(self, teste_aluno, gabarito, id_teste, id_aluno, nota_final, respostas_dadas):
        self.teste_aluno = teste_aluno
        self.__gabarito = gabarito
        self.id_teste = id_teste
        self.id_aluno = id_aluno
        self.__nota_final = nota_final 
        self._respostas_dadas = respostas_dadas 



    def exibir_pontuacao(self,):
        return
    
    def exibir_gabarito(self, gabarito):
        return

    def coletar_resultado(self, calcular):
        return
    
    def get_nota_final(self):
        return self.__nota_final


    def atribuir_nota_final(self, nova_nota):
        self.__nota_final = nova_nota
    



