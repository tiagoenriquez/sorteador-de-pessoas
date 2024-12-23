from flask import Blueprint, redirect, render_template, request, url_for
from src.services import PessoaService


pessoa_blueprint = Blueprint("pessoa", __name__, template_folder="templates")

@pessoa_blueprint.route("/")
def criar_sorteio():
    return render_template("cadastrarSorteio.html")

@pessoa_blueprint.route("/cadastro")
def criar():
    return render_template("cadastrarPessoa.html")

@pessoa_blueprint.route("/insercao", methods=["POST"])
def inserir():
    PessoaService.inserir(request.form["nome"])
    return redirect(url_for("pessoa.criar"))

@pessoa_blueprint.route("/sorteio", methods=["POST"])
def sortear():
    pessoas: list[dict] = []
    for pessoa in PessoaService.sortear(int(request.form.get("numero"))):
        pessoas.append(pessoa.to_dict())
    return render_template("sorteados.html", pessoas=pessoas)