'''from teste.teste import AplicarTesteTeste'''


class Aluno:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha


    def realizar_teste(self, teste, sistema):
        return
    

    def visualizar_gabarito(self, teste):
        return
    
    
#modificar essa ideia de fazer login para aluno 
class AlunoLogin:
    def __init__(self, login, senha, testes_disponiveis):
        self.login = login
        self.senha = senha
        self.testes_disponiveis = testes_disponiveis


'''from .usuario import Usuario
from teste.resultado import Resultado

class Aluno(Usuario):
    def __init__(self, id, nome, email, senha):
        super().__init__(id, nome, email, senha)
        self._respostas_dadas = {} # Protegido: {id_teste: lista_respostas}

    # --- RF8: Realização do Teste ---
    def iniciar_teste(self, teste):
        # Controle de Tempo (RF8) - O Teste controla o tempo, o Aluno apenas inicia.
        print(f"Aluno {self.nome} iniciou o teste: {teste.titulo}")
        # Simulação de início
        return True
        
    def enviar_teste(self, teste, respostas_aluno, sistema):
        # RF8: Envio das respostas
        
        # O teste é corrigido automaticamente (RF10) ou manualmente (RF5) dependendo do tipo
        nota = teste.corrigir_respostas(respostas_aluno)
        
        # Cria o objeto Resultado (RF5)
        resultado = Resultado(teste._id, self._id, nota, respostas_aluno)
        
        # Registra no sistema (RF9)
        sistema.registrar_resultado(self._id, resultado)
        
        return resultado'''