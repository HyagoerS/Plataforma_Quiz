#RF11
'''
Essa criação de usúario estara apenas envolvida com o professor o
aluno ira participar do quiz atráves do pin/código da sala
'''
class CriarUsuario:
    def __init__(self, nome, login, senha, email):
        self.nome = nome
        self.login = login
        self.senha = senha
        self.email= email
    

    def criar_usuario(self, ):
        return
    
    def editar_usuario(self,):
        return
    
    def excluir_usuario(self, id):
        for self.id in self.ids:
            if id == id:
                self.id.remove(id)
                return
        return
    
'''from .usuario import Usuario
from estrutura.excecoes import ObjetoNaoEncontrado

class Administrador(Usuario):
    def __init__(self, id, nome, email, senha):
        super().__init__(id, nome, email, senha)
        # Atributo específico
        self.nivel_acesso = "total"

    # --- RF11: Gestão de Utilizadores ---
    # O Administrador usa o método 'criar_perfil' do Sistema
    
    def editar_perfil(self, id_usuario, novos_dados, sistema):
        usuario = sistema.get_usuario(id_usuario)
        if not usuario:
            raise ObjetoNaoEncontrado(f"Usuário ID {id_usuario} não encontrado.")
        
        # Simples edição
        if 'nome' in novos_dados:
            usuario.nome = novos_dados['nome']
        if 'email' in novos_dados:
            usuario.email = novos_dados['email']
        # Nota: Senha e tipo de perfil seriam mais complexos e precisariam de métodos dedicados
        print(f"Admin editou perfil de {usuario.nome}")
        return usuario

    # --- RF12: Gestão de Turmas ---
    def criar_turma(self, nome_turma, sistema):
        from turma.turma import Turma
        nova_turma = Turma(0, nome_turma) # ID será setado pelo sistema
        sistema.adicionar_turma(nova_turma)
        print(f"Admin criou Turma: {nome_turma}")
        return nova_turma
        
    def associar_usuario_turma(self, id_turma, id_usuario, sistema):
        turma = sistema.get_turma(id_turma)
        usuario = sistema.get_usuario(id_usuario)
        
        if not turma or not usuario:
            raise ObjetoNaoEncontrado("Turma ou Usuário não encontrado.")
            
        turma.adicionar_membro(usuario) # O método da Turma cuida da associação
        print(f"Admin associou {usuario.nome} à Turma {turma.nome}")'''
    