from flask import Flask, render_template, request 
from estrutura.sistema import Sistema
'''from usuarios.professor import Professor
from usuarios.aluno import Aluno
from conteudo.tema import Tema'''
app = Flask(__name__)


nome = "aluno"
senha = 123

sistema = Sistema()



@app.route('/')
def home():
    nome = request.form.get("nomeUsuario")
    senha = request.form.get("senhaUsuario")
    return render_template("aluno.html")
 
#Usuarios 
@app.route("/admin")
def area_admin():
    return render_template("admin.html")

@app.route("/professor")
def area_professor():
    return render_template("professor.html")


@app.route("/aluno")
def area_aluno():
    return render_template("aluno.html")


#Testes Quiz
@app.route("/monter_quiz")
def montar_quiz():
    return render_template("montar_quiz.html")

@app.route("/teste")
def teste_quiz():
    return render_template("teste_quiz.html")

if __name__ == '__main__':
    app.run(debug=True)