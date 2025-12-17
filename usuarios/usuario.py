from estrutura.excecoes import ErroDeLogin

class Usuario:
    def __init__(self, id, nome, email, senha):
        self._id = id            
        self.nome = nome          
        self.email = email
        self.__senha = senha      
        
    def verificar_dados(self, login, senha):
        if self.login == login and self.__senha == senha:
            return True
        raise ErroDeLogin("Login ou senha incorretos.")

    def get_id(self):
        return self._id