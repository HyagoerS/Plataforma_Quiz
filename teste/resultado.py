class Resultado:
    def __init__(self, email_aluno, nota_final):
        self.email_aluno = email_aluno
        self.__nota_final = nota_final 
        self.data_hora = "" 

    def get_nota_final(self):
        return self.__nota_final