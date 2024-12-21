from flask import Flask
from src.controllers.PessoaController import pessoa_blueprint


app = Flask(__name__)
app.register_blueprint(pessoa_blueprint)