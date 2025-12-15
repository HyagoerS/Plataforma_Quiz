from estrutura.excecoes import ErroDeLogin

class Usuario:
    def __init__(self, id, nome, email, senha):
        self._id = id             # Protegido
        self.nome = nome          # Público
        self.email = email
        self.__senha = senha      # Privado (Encapsulamento)
        
    def verificar_credenciais(self, email, senha):
        if self.email == email and self.__senha == senha:
            return True
        # Tratamento de exceção obrigatório (RF7)
        raise ErroDeLogin("Email ou senha incorretos.")

    def get_id(self):
        return self._id