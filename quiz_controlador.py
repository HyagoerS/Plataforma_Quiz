from flask import Flask, render_template, request 

app = Flask(__name__)



@app.route('/')
def home():
    nome = request.form.get("nomeUsuario")
    senha = request.form.get("senhaUsuario")
    return render_template("principal.html")


@app.route('/logado')
def menu_logado():
    return render_template("logado.html")



if __name__ == '__main__':
    app.run(debug=True)