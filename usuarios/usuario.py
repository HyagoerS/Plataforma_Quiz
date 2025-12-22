from estrutura.excecoes import ErroDeLogin

class Usuario:
    def __init__(self, id, nome, email, senha):
        self._id = id            
        self.nome = nome          
        self.email = email
        self.__senha = senha      
        
def verificar_dados(self, login_informado, senha_informada):
    # Usando o email como login
    if self.email == login_informado and self.__senha == senha_informada:
        return True
    raise ErroDeLogin("Login ou senha incorretos.")
   
   
    def get_id(self):
        return self._id
    
    # --- Herança: Aluno (RF7, RF8) ---
class Aluno(Usuario):
    def __init__(self, id, nome, email, senha, turma):
        super().__init__(id, nome, email, senha) # Chama o construtor do Pai (Usuario)
        self.turma = turma
        self.notas = []

# --- Herança: Professor (RF1, RF2, RF3) ---
class Professor(Usuario):
    def __init__(self, id, nome, email, senha, especialidade=None):
        super().__init__(id, nome, email, senha)
        self.especialidade = especialidade

    def criar_tema(self, titulo, descricao):
        # Aqui você futuramente instanciará a classe Tema (RF1)
        print(f"Professor {self.nome} criou o tema: {titulo}")
        # return Tema(titulo, descricao)
