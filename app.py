from flask import Flask, render_template, request 
from estrutura.sistema import Sistema




app = Flask(__name__)

#senha padrão pre-definida
login = "admin"
senha = 123

loginAluno = "aluno"
senhaAluno = 123

loginProfessor = "professor"
senhaProfessor = 123


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


@app.route('/admin/turmas')
def admin_turmas():
    return render_template("admin_turmas.html")

@app.route('/admin/usuarios')
def admin_usuario():
    return render_template("admin_usuarios.html")


#Professor
@app.route('/professor')
def area_professor():
    return render_template("professor.html")


@app.route('/professor/criar_questao')
def professor_criar_questao():
    return render_template("professor_criar_questao.html")

@app.route('/professor/criar_teste')
def professor_criar_teste():
    return render_template("professor_criar_teste.html")

@app.route('/professor/resultados')
def professor_resultado():
    return render_template("professor_resultados.html")

@app.route('/professor/temas')
def professor_temas():
    return render_template("professor_temas.html")


#Aluno
@app.route('/aluno')
def area_aluno():
    return render_template("aluno.html")


@app.route('/aluno/resultado')
def aluno_resultado():
    return render_template("aluno_resultado.html")

@app.route('/aluno/teste')
def aluno_teste():
    return render_template("aluno_teste.html")

#login

@app.route('/autenticar', methods=['POST'])
def autenticar():
    login_form = request.form.get("loginUsuario")
    senha_form = request.form.get("senhaUsuario")

    if login_form == login and str(senha_form) == str(senha):
        return render_template("admin.html")

    elif login_form == loginAluno and str(senha_form) == str(senhaAluno):
        return render_template("aluno.html")

    elif login_form == loginProfessor and str(senha_form) == str(senhaProfessor):
        return render_template("professor.html")

    else:
        return render_template("principal.html", mensagem="Login ou senha incorretos!")




#Cadastrar usuario
#essa parte de cadastrar, ser apenas utilizado no projeto de Alex
@app.route('/admin/usuarios', methods=['GET', 'POST'])
def cadastrar_usuario():
    if request.method == "POST":
        nome = request.form.get("nomeUsuario")
        login = request.form.get("loginUsuario")
        senha = request.form.get("senhaUsuario")
        email = request.form.get("emailUsuario")

        # aqui depois você chama o POO
        # sistema.cadastrar_usuario(...)

        return render_template("admin_usuarios.html", mensagem="Usuário cadastrado com sucesso!")

    return render_template("admin_usuarios.html")


#Remover usuario
@app.route('/remover_usuario', methods=['GET', 'POST'])
def remover_funcionario():
    if request.method == 'POST':
        email = request.form.get("emailRemover")

        return render_template("admin_usuarios.html")

#fazer teste Quiz
@app.route('/teste', methods=['GET', 'POST'])
def aluno_quiz():
   if request.method == 'POST':
        # Captura os dados enviados pelo formulário (exemplo)

        pontuacao = 80
        
        # Lógica para determinar o status (aprovado/reprovado)
        quiz_aluno = "Aprovado" if pontuacao >= 70 else "Reprovado"
        
        # Renderiza o template 'resultado.html' passando as variáveis
        return render_template('aluno_resultado.html', quiz_aluno=quiz_aluno)


#area de sistemas/admin
@app.route("/admin_sistema")
def sistema_adimin():
    return render_template

if __name__ == '__main__':
    app.run(debug=True)