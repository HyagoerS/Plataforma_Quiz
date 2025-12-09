from flask import Flask, render_template, request 
from estrutura.sistema import Sistema


app = Flask(__name__)



# Criamos 1 único sistema GLOBAL
sistema = Sistema()



@app.route('/')
def home():
    nome = request.form.get("nomeUsuario")
    senha = request.form.get("senhaUsuario")
    return render_template("principal.html")


@app.route('/logado')
def menu_logado():
    return render_template("logado.html")

@app.route("/aluno")
def area_aluno():
    return render_template("aluno.html")



if __name__ == '__main__':
    app.run(debug=True)