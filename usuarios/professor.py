from .usuario import Usuario

class Professor(Usuario):
    def __init__(self, id, nome, email, senha, departamento="Educação"):
        super().__init__(id, nome, email, senha)
        self.departamento = departamento




  