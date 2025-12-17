'''from usuarios.professor import Professor
from conteudo.tema import Tema'''
from usuarios.aluno import Aluno
from turmas.turma import Turma

class Notas:
    def __init__(self, nota_aluno):
        self.nota_aluno = []


    def buscar_nota(self):
        return
    

class AutenticarLogin:
    def __init__(self):
        pass


    def validar_login(self):
        return
    

    def testes_liberados(self):
        return
    


class Sistema:
    def __init__(self):
        self.usuarios = {}
        self.turmas = {}       
        self.temas = {}        
        self.testes_disponiveis = {} 
        self.resultados = {}   



    def cadastrar_aluno(self, nome, senha):
        aluno = Aluno(nome, senha)
        self.usuarios.append(aluno)
        return aluno


    def autenticar(self, nome, senha):
        for usuario in self.usuarios:
            if usuario.nome == nome and usuario.senha == senha:
                return usuario
        return None


# RF: criar turma

    def criar_turma(self, nome, professor):
        turma = Turma(nome, professor)
        self.turmas.append(turma)
        return turma



    def adicionar_aluno_na_turma(self, id_turma, aluno):
        turma = self.turmas[id_turma]
        turma.adicionar_aluno(aluno)
        return turma

'''from usuarios.administrador import Administrador
from usuarios.professor import Professor
from usuarios.aluno import Aluno
from estrutura.excecoes import ErroDeLogin, ObjetoNaoEncontrado
from datetime import datetime

class Sistema:

        
        # Contadores para IDs únicos (simulação de auto-incremento)
        self._contador_usuarios = 0
        self._contador_turmas = 0
        self._contador_testes = 0
        self._contador_questoes = 0

    # --- RF7: Autenticação ---
    def login(self, email, senha):
        for usuario in self.usuarios.values():
            try:
                if usuario.verificar_credenciais(email, senha):
                    print(f"Login bem-sucedido para {usuario.nome} ({type(usuario).__name__})")
                    return usuario 
            except ErroDeLogin:
                # Se a senha não bater, tentamos o próximo
                continue
        
        raise ErroDeLogin("Email ou senha incorretos.")

    # --- RF11: Gestão de Utilizadores (Administrador) ---
    def criar_perfil(self, tipo_usuario, nome, email, senha):
        self._contador_usuarios += 1
        id_novo = self._contador_usuarios
        
        # Atribuir perfil (RF11)
        if tipo_usuario == "Administrador":
            novo_usuario = Administrador(id_novo, nome, email, senha)
        elif tipo_usuario == "Professor":
            novo_usuario = Professor(id_novo, nome, email, senha)
        elif tipo_usuario == "Aluno":
            novo_usuario = Aluno(id_novo, nome, email, senha)
        else:
            raise ValueError("Tipo de usuário inválido.")

        self.usuarios[id_novo] = novo_usuario
        return novo_usuario

    def get_usuario(self, id_usuario):
        return self.usuarios.get(id_usuario)

    # --- RF10/RF6/RF9: Visualização de Resultados ---
    def calcular_e_visualizar_resultados(self, id_teste):
        # RF10: Cálculo do resultado Total do Quiz
        resultados_teste = []
        for aluno_id, testes_aluno in self.resultados.items():
            if id_teste in testes_aluno:
                resultado = testes_aluno[id_teste]
                resultados_teste.append({
                    'aluno': self.get_usuario(aluno_id).nome,
                    'nota_total': resultado.get_nota_final()
                })
        
        # Este é o dado para visualização (RF6, RF9)
        return resultados_teste

    # --- Métodos de Orquestração para Conteúdo ---
    def adicionar_tema(self, tema):
        self.temas[tema.titulo] = tema

    def adicionar_turma(self, turma):
        self._contador_turmas += 1
        turma._id = self._contador_turmas
        self.turmas[turma._id] = turma
        
    def get_turma(self, id_turma):
        return self.turmas.get(id_turma)

    def adicionar_teste(self, teste):
        self._contador_testes += 1
        teste._id = self._contador_testes
        self.testes_disponiveis[teste._id] = teste

    def adicionar_questao(self, questao):
        self._contador_questoes += 1
        questao._id = self._contador_questoes
        # Poderia ser adicionada a uma lista global de questões
        # Para simplicidade, não vamos armazenar todas as questões globalmente
        return self._contador_questoes
        
    def registrar_resultado(self, id_aluno, resultado):
        # Adiciona o resultado para consulta (RF5, RF9)
        if id_aluno not in self.resultados:
            self.resultados[id_aluno] = {}
        self.resultados[id_aluno][resultado.id_teste] = resultado'''
