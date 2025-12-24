import sqlite3 as sqlite
import datetime

import sqlite3

def criar_tabela_alunos():
    conn = sqlite3.connect('bdpq.sqlite3') # Corrigido para sqlite3
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

def inserir_usuario(nome, email, login, senha):
    conn = sqlite3.connect('bdpq.sqlite3')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO alunos (nome, email, login, senha) VALUES (?, ?, ?, ?)', 
                   (nome, email, login, senha))
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

def buscar_todas_questoes():
    conn = sqlite.connect('bdpq.sqlite3')
    cursor = conn.cursor()
    # Pega tudo: ID, Enunciado, as 4 alternativas e a Correta
    cursor.execute('SELECT * FROM questoes')
    questoes = cursor.fetchall()
    conn.close()
    return questoes


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
    
    cursor.execute('SELECT COUNT(*) FROM usuarios')
    total_usuarios = cursor.fetchone()[0]
    

    conn.close()
    return {'usuarios': total_usuarios, 'turmas': 0, 'testes': 0}

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

def buscar_todas_questoes():
    conn = sqlite3.connect('bdpq.sqlite3')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM questoes')
    questoes = cursor.fetchall() # Pega todos os resultados
    conn.close()
    return questoes # Retorna a lista para o app.py

def salvar_questao(enunciado, a, b, c, d, correta):
    conn = sqlite.connect('bdpq.sqlite3')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO questoes (enunciado, alternativa_a, alternativa_b, alternativa_c, alternativa_d, correta)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (enunciado, a, b, c, d, correta))
    conn.commit()
    conn.close()


#lógica de resultado do quizz aluno
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
    # Pega a data e hora atual do sistema
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
    # Ordenamos pelos resultados mais recentes (DESC)
    cursor.execute('SELECT aluno_email, nota, data_hora FROM resultados ORDER BY id DESC')
    resultados = cursor.fetchall()
    conn.close()
    return resultados
