'''import sqlite3 as sqlite


def aluno():
    conn = sqlite.connect('dbqr.sqlite3')
    cursor = conn.cursor()



def login(login, senha):
    conn = sqlite.connect('dbqr.sqlite3')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM aluno WHERE login=?, senha=? and email=?", (login, senha, email) )
    dados = cursor.fetchall()
    conn.close()
    return len(dados) > 0
'''
