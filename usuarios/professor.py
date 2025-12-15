'''from conteudo.questao import Criacao_Questoes
from conteudo.multipla_escolha import MultiplaEscolha'''
from conteudo.tema import GerenciadorTema

class Professor():
    def __init__(self, nome):
        super().__init__(nome)
        self.gerenciador_temas = GerenciadorTema()

class Professor:
    def __init__(self):
        self.gerencia_temas = GerenciadorTema()

    def criar_tema(self, nome):
        self.gerencia_temas.criar_tema(nome)

                     
gestao.criar_tema("História")
gestao.editar_tema("História", "História Geral")
gestao.excluir_tema("Matemática")

from .usuario import Usuario
from conteudo.tema import Tema
from estrutura.excecoes import DataInvalida
from datetime import datetime, timedelta

class Professor(Usuario):
    # Herda todos os atributos e métodos de Usuario
    def __init__(self, id, nome, email, senha, departamento):
        super().__init__(id, nome, email, senha)
        self.departamento = departamento

    # --- RF1: Gestão de Conteúdo (Tema) ---
    def criar_tema(self, titulo, descricao, sistema):
        # Cria a instância da classe Tema
        novo_tema = Tema(titulo, descricao)
        sistema.adicionar_tema(novo_tema)
        print(f"Professor {self.nome} criou o Tema: {titulo}")
        return novo_tema

    # --- RF2: Criação de Questões (Multipla Escolha) ---
    def criar_questao(self, enunciado, pontuacao, opcoes, indice_correto, sistema):
        from conteudo.multipla_escolha import QuestaoMultiplaEscolha
        
        # Cria uma nova Questão e pede ao Sistema para gerar um ID
        questao = QuestaoMultiplaEscolha(0, enunciado, pontuacao, opcoes, indice_correto)
        questao._id = sistema.adicionar_questao(questao)
        return questao

    # --- RF3 e RF4: Montagem e Publicação do Teste ---
    def montar_e_publicar_teste(self, titulo, questoes_com_pontuacao, id_turma, inicio_str, termino_str, tempo_max_minutos, sistema):
        from teste.teste import Teste
        
        turma = sistema.get_turma(id_turma)
        if not turma:
            raise ObjetoNaoEncontrado("Turma não encontrada para publicação.")

        # Tratamento de Exceção obrigatório (RF4)
        try:
            inicio = datetime.strptime(inicio_str, '%Y-%m-%d %H:%M')
            termino = datetime.strptime(termino_str, '%Y-%m-%d %H:%M')
            if inicio >= termino or termino < datetime.now():
                raise DataInvalida("Datas de início/término inválidas.")
        except ValueError:
            raise DataInvalida("Formato de data/hora inválido. Use YYYY-MM-DD HH:MM.")

        novo_teste = Teste(
            0, # O ID será definido pelo sistema
            titulo, 
            questoes_com_pontuacao,
            id_turma, 
            inicio, 
            termino, 
            tempo_max_minutos, 
            self._id # ID do Professor
        )
        sistema.adicionar_teste(novo_teste)
        print(f"Teste '{titulo}' criado e publicado para Turma ID: {id_turma}")
        return novo_teste