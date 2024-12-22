from flask import Flask
from src.migrations.migrate import migrate
from src.controllers.NomeController import nome_blueprint
from src.controllers.PessoaController import pessoa_blueprint


migrate()
app = Flask(__name__)
app.register_blueprint(pessoa_blueprint)
app.register_blueprint(nome_blueprint)