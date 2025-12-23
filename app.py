from flask import Flask, render_template, request, redirect, url_for, session
from estrutura.sistema import Sistema
from conteudo.multipla_escolha import QuestaoMultiplaEscolha
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
@app.route('/aluno/teste')
def exibir_teste():
    # Busca as questões no banco e manda para o HTML
    dados_banco = bdpq.buscar_todas_questoes()
    return render_template("realizar_teste.html", lista_questoes=dados_banco)

@app.route('/aluno/corrigir_teste', methods=['POST'])
def corrigir_teste():
    questoes_banco = bdpq.buscar_todas_questoes()
    nota_final = 0
    total_possivel = 0

    for q in questoes_banco:
        id_q = q[0]
        resposta_aluno = request.form.get(f'resposta_{id_q}')
        
        # 1. Instanciamos a SUA classe POO para cada questão
        # id, enunciado, pontuacao, opcoes, correta
        objeto_questao = QuestaoMultiplaEscolha(q[0], q[1], 2.5, [q[2],q[3],q[4],q[5]], q[6])
        
        # 2. Usamos o seu método corrigir() que você criou!
        pontos_recebidos = objeto_questao.corrigir(resposta_aluno)
        
        nota_final += pontos_recebidos
        total_possivel += objeto_questao.pontuacao

    return render_template("resultado_aluno.html", nota=nota_final, total=total_possivel)
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
# No app.py


@app.route('/professor/criar_questao', methods=['GET', 'POST'])
def criar_questao():
    if request.method == 'POST':
        # 1. Pegamos os dados que o professor digitou no HTML
        enunciado = request.form.get('enunciado')
        pontos = float(request.form.get('pontuacao'))
        opcoes = [
            request.form.get('alt_a'),
            request.form.get('alt_b'),
            request.form.get('alt_c'),
            request.form.get('alt_d')
        ]
        correta = request.form.get('correta')

        # 2. Criamos o objeto usando a SUA classe POO!
        # Passamos None para o ID porque o Banco vai gerar um automático
        nova_q = QuestaoMultiplaEscolha(None, enunciado, pontos, opcoes, correta)

        # 3. Chamamos o banco para salvar (RF2)
        # Aqui você usa a função que criamos no bdpq.py
        bdpq.salvar_questao(
            nova_q.enunciado, 
            nova_q.opcoes[0], nova_q.opcoes[1], 
            nova_q.opcoes[2], nova_q.opcoes[3], 
            nova_q.get_resposta_correta() # Usando o seu método get
        )

        return render_template("professor_criar_questao.html", mensagem="Sucesso!")

    return render_template("professor_criar_questao.html")


@app.route('/salvar_pergunta', methods=['POST'])
def salvar_pergunta():
    # 1. Pega os dados do formulário
    enunciado = request.form.get('enunciado')
    correta = request.form.get('correta')
    
    # 2. Usa a SUA classe para organizar os dados
    # (Criamos o objeto com ID temporário e pontuação padrão 2.5)
    nova_q = QuestaoMultiplaEscolha(None, enunciado, 2.5, [], correta)
    
    # 3. Manda para o banco de dados
    bdpq.salvar_questao(nova_q.enunciado, ..., nova_q._QuestaoMultiplaEscolha__resposta_correta)
    
    return "Salvo com sucesso usando POO!"


#area de sistemas/admin
@app.route('/admin/painel')
def admin_sistema():

    try:
        contagem = bdpq.contar_registros()
    except:
        contagem = {'usuarios': 0, 'turmas': 0, 'testes': 0}
        

    return render_template("admin_painel.html", info=contagem)



if __name__ == '__main__':
    app.run(debug=True)