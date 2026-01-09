QuizRush - Plataforma de Testes Online
QuizRush é uma aplicação web inspirada no estilo visual do Kahoot, desenvolvida para facilitar a criação, aplicação e correção automática de quizzes. O projeto utiliza o framework Flask, persistência em SQLite e os conceitos fundamentais de Programação Orientada a Objetos (POO).

Tecnologias Utilizadas
Backend: Python 3 + Flask

Frontend: HTML5, CSS3 (Custom Kahoot Style), Jinja2

Banco de Dados: SQLite3

Arquitetura: Programação Orientada a Objetos (POO)

    Funcionalidades Principais
O sistema é dividido em três níveis de acesso:

Administrador
Gestão de usuários (Cadastro e Remoção).


Controle de acesso ao sistema.

Professor
Criação de questões de múltipla escolha.

Definição de pontuação por questão.

Visualização de resultados e notas dos alunos.

Aluno
Realização de testes com interface dinâmica.

Cronômetro regressivo para controle de tempo.

Envio automático ao encerrar o tempo.

Resultado imediato após a correção automática.


    Como Executar o Projeto
    
Instale as dependências:
pip install flask

Inicie o servidor:
python app.py

Credenciais Padrão (Teste)

Admin: login: admin | senha: 123
Professor: login: professor | senha: 123
Aluno: Realizar cadastro no painel admin ou usar dados salvos no banco.
