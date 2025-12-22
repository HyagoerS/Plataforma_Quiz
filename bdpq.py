import sqlite3 as sqlite


def alunos():
    conn = sqlite.connect('bdpq.sqlite3')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos(
    email TEXT PRIMARY KEY,
    nome TEXT NOT NULL,
    login TEXT NOT NULL,
    senha TEXT NOT NULL
    
    )
''')
    conn.commit()
    conn.close()

def turmas():
    conn = sqlite.connect('bdpq.sqlite3')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXIST turmas(
    id INTERGER PRIMARY KEY,
    nome TEXT
    )
''')
    conn.commit()
    conn.close()

def temas():
    conn = sqlite.connect('bdpq.sqlite3')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXIST temas(
    id INTERGER PRIMARY KEY,
    titulo TEXT,
    descricao TEXT
    )
''')
    conn.commit()
    conn.close()


#Lógicas relacionadas a Usuários
def cadastrar(email, nome, login, senha):
    conn = sqlite.connect('bdpq.sqlite3')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO alunos (email, nome, login, senha) VALUES (?, ?, ?, ?)", (email, nome, login, senha,))

    conn.commit()
    conn.close()
    return "Dados inseridos com sucesso!"


def login(login, senha):
    conn = sqlite.connect('bdpq.sqlite3')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM alunos WHERE login=? and senha=?", (login, senha) )
    dados = cursor.fetchall()
    conn.close()
    return len(dados) > 0


def remover(email):
    conn = sqlite.connect('bdpq.sqlite3')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM alunos WHERE email=?", (email,))
    linhas_afetadas = cursor.rowcount

    conn.commit()
    conn.close()
    return linhas_afetadas > 0 

import sqlite3

def usuario():
    conn = sqlite3.connect('bdpq.sqlite3')
    cursor = conn.cursor()
    # Atualizando a tabela para incluir o PERFIL (RF11)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL,
            perfil TEXT NOT NULL -- 'admin', 'professor' ou 'aluno'
        )
    ''')
    conn.commit()
    conn.close()

def contar_registros():
    conn = sqlite3.connect('bdpq.sqlite3')
    cursor = conn.cursor()
    
    # RF13 - Pegando os números para o painel
    cursor.execute('SELECT COUNT(*) FROM usuarios')
    total_users = cursor.fetchone()[0]
    
    # (Quando você criar as outras tabelas, adicionaremos as contagens aqui)
    conn.close()
    return {'usuarios': total_users, 'turmas': 0, 'testes': 0}

#Lógica relacionada a questões/quizz
def criar_tabela_questoes():
    conn = sqlite.connect('bdpq.sqlite3')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS questoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            enunciado TEXT NOT NULL,
            alternativa_a TEXT NOT NULL,
            alternativa_b TEXT NOT NULL,
            alternativa_c TEXT NOT NULL,
            alternativa_d TEXT NOT NULL,
            correta TEXT NOT NULL -- Guardaremos aqui 'A', 'B', 'C' ou 'D'
        )
    ''')
    conn.commit()
    conn.close()

def salvar_questao(enunciado, a, b, c, d, correta):
    conn = sqlite.connect('bdpq.sqlite3')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO questoes (enunciado, alternativa_a, alternativa_b, alternativa_c, alternativa_d, correta)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (enunciado, a, b, c, d, correta))
    conn.commit()
    conn.close()
