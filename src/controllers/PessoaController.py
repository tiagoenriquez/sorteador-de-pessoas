from flask import Blueprint, render_template


pessoa_blueprint = Blueprint("pessoa", __name__, template_folder="templates")

@pessoa_blueprint.route("/")
def criar_sorteio():
    return render_template("cadastrarSorteio.html")

@pessoa_blueprint.route("/cadastro")
def criar():
    return render_template("cadastrarPessoa.html")