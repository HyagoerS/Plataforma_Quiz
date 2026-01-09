class Usuario:
    def __init__(self, id, nome, email, senha):
        self._id = id           # Protegido
        self.nome = nome          
        self.email = email
        self.__senha = senha    # Privado (Encapsulamento)
        
    def verificar_senha(self, senha_informada):
        """Método seguro para validar a senha sem expô-la"""
        return self.__senha == senha_informada

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

