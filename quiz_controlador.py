from flask import Flask, render_template, request 
from estrutura.sistema import Sistema
'''from usuarios.professor import Professor
from usuarios.aluno import Aluno
from conteudo.tema import Tema'''
'''import dbpq
dbpq.aluno'''


app = Flask(__name__)

#senha padrão pre-definida
login = "admin"
senha = 123


sistema = Sistema()



@app.route('/')
def home():
    login = request.form.get("loginUsuario")
    senha = request.form.get("senhaUsuario")
    return render_template("principal.html", mensagem="Login ou senha incorretos!")

 


#Usuarios 
@app.route('/admin')
def area_admin():
    return render_template("admin.html")

@app.route('/professor')
def area_professor():
    return render_template("professor.html")


@app.route('/aluno')
def area_aluno():
    return render_template("aluno.html")

#login

@app.route('/autenticar', methods=['POST'])
def autenticar():
    login = request.form.get("loginUsuario")
    senha = request.form.get("senhaUsuario")


    if login and senha: 
        return render_template("aluno.html", mensagem=f"Bem-vindo(a)!")
    else:
        return render_template("principal.html", mensagem="Login ou senha incorretos!")

#Testes Quiz
'''@app.route('montar_quiz')
def montar_quiz():
    return render_template("montar_quiz.html")'''

@app.route("/teste")
def teste_quiz():
    return render_template("teste_quiz.html")


#area de sistemas/admin
@app.route("/admin_sistema")
def sistema_adimin():
    render_template

if __name__ == '__main__':
    app.run(debug=True)