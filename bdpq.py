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

