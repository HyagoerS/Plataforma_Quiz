from flask import Flask, render_template, request, redirect, url_for, session
from estrutura.sistema import Sistema
from teste.teste import meu_teste_jogos, meu_teste_geral

import bdpq
bdpq.alunos()



app = Flask(__name__)


#senha padrão pré-definidas
login = "admin"
senha = 123

loginAluno = "aluno"
senhaAluno = 123

loginProfessor = "professor"
senhaProfessor = 123

sistema = Sistema()


#Rota da Página Principal/Inicial
@app.route('/')
def home():
    login = request.form.get("loginUsuario")
    senha = request.form.get("senhaUsuario")
    return render_template("principal.html", mensagem="Login ou senha incorretos!")



#Usuarios 
#Rotas do Administrado
@app.route('/admin')
def area_admin():
    return render_template("admin.html")


@app.route('/admin/turmas')
def admin_turmas():
    return render_template("admin_turmas.html")

@app.route('/admin/usuarios')
def admin_usuario():
    return render_template("admin_usuarios.html")


#Rotas do Usuário Professor
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


# Rotas do Usuário Aluno
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



#Login dos Usuários Aluno/Porfessor

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
    elif usuario:
        return render_template("aluno.html")
    else:
        return render_template("principal.html", mensagem="Login ou senha incorretos!")




#Cadastrar usuario
# aqui chamar o POO ou bdpq
# sistema.cadastrar_usuario(...)
#essa parte de cadastrar, ser apenas utilizado no projeto de Alex
#Identificar por tipo, pegando pelo email aluno e professor
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    perfil = request.form.get('perfil') # Pegando do formulário
    
    # Lógica para salvar no banco (bdpq.inserir_usuario(nome, email, senha, perfil))
    return redirect(url_for('admin_usuario'))




#Remover Usuários
@app.route('/admin/usuarios/remover', methods=['POST'])
def remover_funcionario():
    
    email = request.form.get("emailRemover")
    
    
    if bdpq.remover(email):
        return render_template("admin_usuarios.html", mensagem="Removido com sucesso!")
    else:
        return render_template("admin_usuarios.html", mensagem="Usuário não encontrado!")


# Teste Quiz Aluno
#Quiz De Jogos
@app.route('/teste_quiz/jogo', methods=['POST'])
def aluno_quiz_jogo():

    resp1 = request.form.get('pergunta1')
    resp2 = request.form.get('pergunta2')
    resp3 = request.form.get('pergunta3')
    resp4 = request.form.get('pergunta4')

    respostas_do_aluno = [resp1, resp2, resp3, resp4]


    nota_final = meu_teste_jogos.calcular_resultado(respostas_do_aluno)


    return render_template('aluno_resultado.html', nota=nota_final)

#Quiz de Conhecimento Gerias
@app.route('/teste_quiz/geral', methods=['GET', 'POST'])
def aluno_quiz_geral():

    resp1 = request.form.get('pergunta1')
    resp2 = request.form.get('pergunta2')
    resp3 = request.form.get('pergunta3')
    resp4 = request.form.get('pergunta4')

    respostas_do_aluno = [resp1, resp2, resp3, resp4]


    nota_final = meu_teste_geral.calcular_resultado(respostas_do_aluno)


    return render_template('aluno_resultado.html', nota=nota_final)

#Rota quizz do professor
@app.route('/professor/criar_questao', methods=['GET', 'POST'])
def criar_questao():
    if request.method == 'POST':
        # Pega os dados do formulário
        enunciado = request.form.get('enunciado')
        alt_a = request.form.get('alt_a')
        alt_b = request.form.get('alt_b')
        alt_c = request.form.get('alt_c')
        alt_d = request.form.get('alt_d')
        correta = request.form.get('correta')

        # Salva no banco
        bdpq.salvar_questao(enunciado, alt_a, alt_b, alt_c, alt_d, correta)
        
        return render_template("professor.html", mensagem="Questão criada com sucesso!")

    return render_template("criar_questao.html")


#area de sistemas/admin
@app.route('/admin/painel')
def admin_sistema():
    # 1. Segurança (Descomente quando tiver o login funcionando com session)
    # if session.get('perfil') != 'admin':
    #     return redirect(url_for('login'))
    
    # 2. Busca dados REAIS do banco (RF13)
    try:
        contagem = bdpq.contar_registros()
    except:
        # 3. Fallback: Se o banco falhar, mostra dados de teste para não quebrar o site
        contagem = {'usuarios': 0, 'turmas': 0, 'testes': 0}
        
    # 4. Envia tudo para o HTML
    return render_template("admin_painel.html", info=contagem)



if __name__ == '__main__':
    app.run(debug=True)