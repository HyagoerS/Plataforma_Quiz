class ErroDeLogin(Exception):
    """RF7: Erro durante a autenticação."""
    pass

class DataInvalida(Exception):
    """RF4: Erro de prazo ou data de publicação."""
    pass

class PermissaoNegada(Exception):
    """Erro para ações que o usuário não pode executar (e.g., Aluno tentar criar Tema)."""
    pass

class ObjetoNaoEncontrado(Exception):
    """Erro ao buscar Turma, Tema, Questão que não existe."""
    pass