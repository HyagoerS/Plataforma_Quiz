from flask import Flask, render_template, request, redirect, url_for, session
from usuarios.usuario import Usuario
from conteudo.multipla_escolha import QuestaoMultiplaEscolha


import bdpq
bdpq.criar_tabela_usuarios()
bdpq.criar_tabela_questoes()
bdpq.criar_tabela_resultados()



app = Flask(__name__)
app.secret_key = 'projeto_quiz_key'

#senha padrão pré-definidas
login = "admin"
senha = 123

loginProfessor = "professor"
senhaProfessor = 123



#Rota da Página Principal/Inicial
@app.route('/')
def home():
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


@app.route('/professor/resultados')
def professor_resultado():
    return render_template("professor_resultados.html")



# Rotas do Usuário Aluno
@app.route('/aluno')
def area_aluno():
    return render_template("aluno.html")


@app.route('/aluno/resultado')
def aluno_resultado():
    return render_template("aluno_resultado.html")

@app.route('/aluno/quiz') 
def aluno_quiz(): 
    questoes = bdpq.buscar_todas_questoes()
    return render_template("aluno_quiz.html", lista_questoes=questoes)


#Login dos Usuários Aluno/Porfessor



@app.route('/autenticar', methods=['POST'])
def autenticar():
    login_form = request.form.get("loginUsuario")
    senha_form = request.form.get("senhaUsuario")

    # PRIMEIRO: Checa se é o Admin (Fixo no código)
    if login_form == "admin" and str(senha_form) == "123":
        session['usuario_logado'] = "admin@sistema.com"
        session['perfil'] = 'admin'
        return redirect('/admin')
    
    if login_form == "professor" and str(senha_form) == "123":
        session['usuario_logado'] = "professor@sistema.com"
        session['perfil'] = 'professor'
        return redirect('/professor')

    # SEGUNDO: Se não for admin, aí sim ele tenta buscar no banco
    dados = bdpq.buscar_usuario_para_login(login_form) # Agora não vai crashar porque a tabela existe!

    if dados:
        user = Usuario(dados[0], dados[1], dados[2], dados[3])
        if user.verificar_senha(senha_form):
            session['usuario_logado'] = user.email
            session['perfil'] = 'aluno'
            return redirect('/aluno')

    return render_template("principal.html", mensagem="Login ou senha incorretos!")

@app.route('/logout')
def logout():
    session.clear()
    
    return redirect('/')

#Cadastrar usuario
#Identificar por tipo, pegando pelo email aluno e professor
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form.get('nome')
    email = request.form.get('email')
    login = request.form.get('login')
    senha = request.form.get('senha')

    try:
        bdpq.inserir_usuario(nome, email, login, senha, perfil='aluno')
        return render_template('admin_usuarios.html', mensagem="Usuário cadastrado com sucesso!")
    except Exception as e:
        return render_template('admin_usuarios.html', mensagem=f"Erro: {e}")




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
    dados_banco = bdpq.buscar_todas_questoes()
    
    # 2. DEBUG: Verifique se o console mostra as questões ao carregar a página
    print(f"DEBUG: Carregando {len(dados_banco)} questões para o aluno.")

    return render_template("aluno_quiz.html", lista_questoes=dados_banco)

@app.route('/aluno/corrigir_teste', methods=['POST'])
def corrigir_teste():
    # 1. Busca os dados brutos no banco
    questoes_banco = bdpq.buscar_todas_questoes()
    
    nota_total = 0
    maximo_pontos = 0

    for q in questoes_banco:
        # q[0]=ID, q[1]=Enunciado, q[2]=Alt_A, q[3]=Alt_B, q[4]=Alt_C, q[5]=Alt_D, q[6]=Correta
        
        id_q = q[0]
        
        # 2. Pega o que o aluno marcou no formulário HTML
        resposta_usuario = request.form.get(f'resposta_{id_q}')
        
        # 3. INSTANCIAÇÃO DO OBJETO POO
        # Passamos os dados do banco para o molde da classe
        objeto_questao = QuestaoMultiplaEscolha(
            id_questao=q[0],
            enunciado=q[1],
            pontuacao=2.5,
            opcoes=[q[2], q[3], q[4], q[5]], 
            indice_correto=q[6]
        )
        
        # 4. USO DO MÉTODO DO OBJETO
        # Aqui é a POO em ação: o objeto "sabe" se ele mesmo está correto
        pontos_recebidos = objeto_questao.corrigir(resposta_usuario)
        nota_total += pontos_recebidos
        maximo_pontos += objeto_questao.pontuacao

    
    email_aluno = session.get('usuario_logado')
    if email_aluno:
        bdpq.salvar_resultado(email_aluno, nota_total)
    
    return render_template("aluno_resultado.html", nota=nota_total, total=maximo_pontos)


#Rota quizz do professor

@app.route('/professor/criar_questao', methods=['GET', 'POST'])
def criar_questao():
    if request.method == 'POST':

        enunciado = request.form.get('enunciado')
        pontos = float(request.form.get('pontuacao'))
        opcoes = [
            request.form.get('alt_a'),
            request.form.get('alt_b'),
            request.form.get('alt_c'),
            request.form.get('alt_d')
        ]
        correta = request.form.get('correta')

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


@app.route('/professor/resultados')
def visualizar_resultados():
    # Segurança: apenas professores podem ver as notas
    if session.get('perfil') != 'professor':
        return "Acesso negado!", 403

    # Busca a lista de notas no banco de dados
    lista_notas = bdpq.buscar_todos_resultados()
    
    return render_template("professor_resultados.html", resultados=lista_notas)



if __name__ == '__main__':
    app.run(debug=True)