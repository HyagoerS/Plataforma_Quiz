import sqlite3 
from datetime import datetime


# GESTÃO DE USUÁRIOS (Tabela Única)


def criar_tabela_usuarios():
    conn = sqlite3.connect('bdpq.sqlite3')
    cursor = conn.cursor()
    # Criamos uma tabela única que serve para Alunos, Professores e Admins
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            login TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL,
            perfil TEXT NOT NULL -- 'aluno', 'professor' ou 'admin'
        )
    ''')
    conn.commit()
    conn.close()

def inserir_usuario(nome, email, login, senha, perfil='aluno'):
    conn = sqlite3.connect('bdpq.sqlite3')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO usuarios (nome, email, login, senha, perfil) 
        VALUES (?, ?, ?, ?, ?)
    ''', (nome, email, login, senha, perfil))
    conn.commit()
    conn.close()

def buscar_usuario_para_login(login_informado):
    conn = sqlite3.connect('bdpq.sqlite3')
    cursor = conn.cursor()
    # Busca por login ou email para flexibilidade
    cursor.execute('SELECT id, nome, email, senha, perfil FROM usuarios WHERE login = ? OR email = ?', 
                   (login_informado, login_informado))
    usuario = cursor.fetchone()
    conn.close()
    return usuario

def remover_usuario(email):
    conn = sqlite3.connect('bdpq.sqlite3')
    cursor = conn.cursor()
    # Atualizado para remover da tabela correta 'usuarios'
    cursor.execute("DELETE FROM usuarios WHERE email=?", (email,))
    linhas_afetadas = cursor.rowcount
    conn.commit()
    conn.close()
    return linhas_afetadas > 0 


# GESTÃO DE QUESTÕES (QUIZ)

def criar_tabela_questoes():
    conn = sqlite3.connect('bdpq.sqlite3')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS questoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            enunciado TEXT NOT NULL,
            alternativa_a TEXT NOT NULL,
            alternativa_b TEXT NOT NULL,
            alternativa_c TEXT NOT NULL,
            alternativa_d TEXT NOT NULL,
            correta TEXT NOT NULL 
        )
    ''')
    conn.commit()
    conn.close()

def buscar_todas_questoes():
    conn = sqlite3.connect('bdpq.sqlite3')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM questoes')
    questoes = cursor.fetchall()
    conn.close()
    return questoes

def salvar_questao(enunciado, a, b, c, d, correta):
    conn = sqlite3.connect('bdpq.sqlite3')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO questoes (enunciado, alternativa_a, alternativa_b, alternativa_c, alternativa_d, correta)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (enunciado, a, b, c, d, correta))
    conn.commit()
    conn.close()


# GESTÃO DE RESULTADOS

def criar_tabela_resultados():
    conn = sqlite3.connect('bdpq.sqlite3')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS resultados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            aluno_email TEXT NOT NULL,
            nota REAL NOT NULL,
            data_hora TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def salvar_resultado(email, nota):
    conn = sqlite3.connect('bdpq.sqlite3')
    cursor = conn.cursor()
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    cursor.execute('''
        INSERT INTO resultados (aluno_email, nota, data_hora)
        VALUES (?, ?, ?)
    ''', (email, nota, agora))
    conn.commit()
    conn.close()

def buscar_todos_resultados():
    conn = sqlite3.connect('bdpq.sqlite3')
    cursor = conn.cursor()
    cursor.execute('SELECT aluno_email, nota, data_hora FROM resultados ORDER BY id DESC')
    resultados = cursor.fetchall()
    conn.close()
    return resultados