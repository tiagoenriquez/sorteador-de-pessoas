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
    return redirect(url_for("pessoa.criar_sorteio"))