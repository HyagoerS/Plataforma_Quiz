from flask import Flask, render_template, request 
from estrutura.sistema import Sistema
from usuarios.professor import Professor
from usuarios.aluno import Aluno
from conteudo.tema import Tema

app = Flask(__name__)



# Criamos 1 único sistema GLOBAL
sistema = Sistema()



@app.route('/')
def home():
    nome = request.form.get("nomeUsuario")
    senha = request.form.get("senhaUsuario")
    return render_template("principal.html")
 

@app.route("/admin")
def area_admin():
    return render_template("admin.html")

@app.route("/professor")
def area_professor():
    return render_template("professor.html")


@app.route("/aluno")
def area_aluno():
    return render_template("aluno.html")



if __name__ == '__main__':
    app.run(debug=True)