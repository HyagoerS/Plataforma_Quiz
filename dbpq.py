import sqlite3 as sqlite


def aluno():
    conn = sqlite.connect('dbpq.sqlite3')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos(
    email TEXT PRIMARY KEY,
    nome TEXT NOT NULL,
    login TEXT NOT NULL,
    senha TEXT NOT NULL
)
    ''')


def cadastrar(email, nome, login, senha):
    conn = sqlite.connect('dbpq.sqlite3')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO alunos (email, nome, login, senha) VALUES (?, ?, ?, ?)", (email, nome, login, senha))

    conn.commit()
    conn.close()
    return "Dados inseridos com sucesso!"


def login(login, senha):
    conn = sqlite.connect('dbpq.sqlite3')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM aluno WHERE login=? and senha=?", (login, senha) )
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

