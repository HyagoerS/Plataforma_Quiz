from flask import Flask, render_template, request 
from estrutura.sistema import Sistema
from teste.teste import meu_teste, meu_teste2

import bdpq
bdpq.alunos()



app = Flask(__name__)

emails = []

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

@app.route('/aluno/teste/games')
def aluno_teste_jogo():
    return render_template("aluno_teste_jogo.html")

@app.route('/aluno/teste/geral')
def aluno_teste_geral():
    return render_template("aluno_teste_geral.html")



#login

@app.route('/autenticar', methods=['POST'])
def autenticar():
    login_form = request.form.get("loginUsuario")
    senha_form = request.form.get("senhaUsuario")

    usuario = bdpq.login(login_form, senha_form)

    if login_form == "admin" and str(senha_form) == "123":
        return render_template("admin.html")

    elif login_form == "aluno" and str(senha_form) == "123":
        return render_template("aluno.html")

    elif login_form == "professor" and str(senha_form) == "123":
        return render_template("professor.html")
    
    if usuario:
        return render_template("aluno.html")
    else:
        return render_template("principal.html", mensagem="Login ou senha incorretos!")




#Cadastrar usuario
#essa parte de cadastrar, ser apenas utilizado no projeto de Alex
@app.route('/admin/usuarios', methods=['GET', 'POST'])
def cadastrar_usuario():

    if request.method == "POST":
        email = request.form.get("emailUsuario")
        nome = request.form.get("nomeUsuario")
        login = request.form.get("loginUsuario")
        senha = request.form.get("senhaUsuario")


        usuario = bdpq.cadastrar(email, nome, login, senha)

        if usuario:
            return render_template("admin_usuarios.html", mensagem="Usuário cadastrado com sucesso!")
        else:
            return render_template("admin_usuarios.html", mensagem="Erro: Email já cadastrado.")
        # aqui depois você chama o POO
        # sistema.cadastrar_usuario(...)

    return render_template("principal.html", mensagem="Usuário cadastrado com sucesso!")




#Remover usuario
@app.route('/admin/usuarios', methods=['GET', 'POST'])
def remover_funcionario():
    if request.method == 'POST':
        email = request.form.get("emailRemover")

        remover = bdpq.remover(email)

        if remover:
            if email in emails:
                emails.remove(email)
                return render_template("admin.html", mensagem=f"Usuário removido com sucesso!")
        else:
            return render_template("admin_usuarios.html",  mensagem=f"Usuário não foi encontrado!")
    return render_template("admin_usuarios.html")


#fazer teste Quiz
@app.route('/teste_quiz/jogo', methods=['POST'])
def aluno_quiz_jogo():
    # 1. Capturar o que o aluno marcou no HTML
    resp1 = request.form.get('pergunta1')
    resp2 = request.form.get('pergunta2')
    resp3 = request.form.get('pergunta3')
    resp4 = request.form.get('pergunta4')

    respostas_do_aluno = [resp1, resp2, resp3, resp4]


    nota_final = meu_teste.calcular_resultado(respostas_do_aluno)


    return render_template('aluno_resultado.html', nota=nota_final)

@app.route('/teste_quiz/geral', methods=['GET', 'POST'])
def aluno_quiz_geral():
    # 1. Capturar o que o aluno marcou no HTML
    resp1 = request.form.get('pergunta1')
    resp2 = request.form.get('pergunta2')
    resp3 = request.form.get('pergunta3')
    resp4 = request.form.get('pergunta4')

    respostas_do_aluno = [resp1, resp2, resp3, resp4]


    nota_final = meu_teste2.calcular_resultado(respostas_do_aluno)


    return render_template('aluno_resultado.html', nota=nota_final)

'''@app.route('/teste_resultado', methods=['GET', 'POST'])
def aluno_resultado():
   if request.method == 'POST':
        # Captura os dados enviados pelo formulário (exemplo)

 
        
        # Lógica para determinar o status (aprovado/reprovado)

        
    return render_template()'''


#area de sistemas/admin
@app.route("/admin_sistema")
def sistema_adimin():
    return render_template

if __name__ == '__main__':
    app.run(debug=True)