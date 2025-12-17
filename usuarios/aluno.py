from .usuario import Usuario

class Aluno(Usuario):
    def __init__(self, nome, email, senha):
        super().__init__(id, nome, email, senha)
        self.nome = nome
        self.senha = senha


    def realizar_teste(self, teste, sistema):
        return
    

    def visualizar_gabarito(self, gabarito):
        self.gabarito = gabarito

    
    

class AlunoLogin:
    def __init__(self, login, senha, testes_disponiveis):
        self.login = login
        self.senha = senha
        self.testes_disponiveis = testes_disponiveis


