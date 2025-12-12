'''import sqlite3 as sqlite


def aluno():
    conn = sqlite.connect('dbpq.sqlite3')
    cursor = conn.cursor()



def login(login, senha):
    conn = sqlite.connect('dbpq.sqlite3')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM aluno WHERE login=? and senha=?", (login, senha) )
    dados = cursor.fetchall()
    conn.close()
    return len(dados) > 0
'''


'''def buscar(teste_quiz):
    conn = sqlite.connect('dbpq.sqlite3')
    cursor = conn.cursor()

    cursor.execute("SELEC WHERE teste=?", (teste_quiz,))
    resultado = cursor.fetchall()

    conn.close()
    return resultado'''