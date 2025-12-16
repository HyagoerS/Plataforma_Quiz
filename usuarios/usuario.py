from estrutura.excecoes import ErroDeLogin

class Usuario:
    def __init__(self, id, nome, email, senha):
        self._id = id            
        self.nome = nome          
        self.email = email
        self.__senha = senha      
        
    def verificar_dados(self, email, senha):
        if self.email == email and self.__senha == senha:
            return True
        raise ErroDeLogin("Email ou senha incorretos.")

    def get_id(self):
        return self._id