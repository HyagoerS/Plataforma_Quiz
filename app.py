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

login


sistema = Sistema()



@app.route('/')
def home():
    login = request.form.get("loginUsuario")
    senha = request.form.get("senhaUsuario")
    return render_template("principal.html", mensagem="Login ou senha incorretos!")

 


#Usuarios 
@app.route('/admin')
def admin_dashboard():
    return render_template("admin_dashboard.html")

@app.route('/admin')
def admin_turmas():
    return render_template("admin_turmas.html")

@app.route('/admin')
def admin_usuario():
    return render_template("admin_usuario.html")

#Professor
@app.route('/professor')
def professor_dashboard():
    return render_template("professor_dashboard.html")

@app.route('/professor')
def professor_criar_questao():
    return render_template("professor_criar_questao.html")

@app.route('/professor')
def professor_criar_teste():
    return render_template("professor_criar_teste.html")

@app.route('/professor')
def professor_resultado():
    return render_template("professor_resultados.html")

@app.route('/professor')
def professor_():
    return render_template("professor_temas.html")

#Aluno
@app.route('/aluno')
def aluno_dashboard():
    return render_template("aluno_.html")

@app.route('/aluno')
def aluno_resultado():
    return render_template("aluno_.html")

@app.route('/aluno')
def aluno_teste():
    return render_template("aluno_.html")

#login

@app.route('/autenticar', methods=['POST'])
def autenticar():
    login = request.form.get("loginUsuario")
    senha = request.form.get("senhaUsuario")


    if login and senha: 
        return render_template("admin_dashboard.html", mensagem=f"Bem-vindo(a)!")
    else:
        return render_template("principal.html", mensagem="Login ou senha incorretos!")

#Testes Quiz
@app.route('montar_quiz')
def montar_quiz():
    return render_template("professor_criar_teste.html")

@app.route("/aluno_teste")
def teste_quiz():
    return render_template("aluno_teste.html")

#Cadastrar usuario
@app.route('/admin_usuario.html', methods=['GET', 'POST'])
def cadastrarusuario():

    if request.method == "GET":
        return render_template("admin_usuario.html")
    nome = request.form.get("nomeUsuario")
    senha = request.form.get("senhaUsuario")
    login = request.form.get("loginUsuario")
    email = request.form.get("emailUsuario")

    return render_template("principal.html", mensagem=" cadastrado com sucesso!")

#Remover usuario
@app.route('/remover_usuario', methods=['GET', 'POST'])
def remover_funcionario():
    if request.method == 'POST':
        nome = request.form.get("nomeRemover")

#area de sistemas/admin
@app.route("/admin_sistema")
def sistema_adimin():
    render_template

if __name__ == '__main__':
    app.run(debug=True)