class Sistema:
    def __init__(self):
        self.usuarios = []
        self.turmas = [] 


    def cadastrar_aluno_na_memoria(self, aluno_obj):
        self.usuarios.append(aluno_obj)



    def adicionar_aluno_na_turma(self, id_turma, aluno):
        turma = self.turmas[id_turma]
        turma.adicionar_aluno(aluno)
        return turma

