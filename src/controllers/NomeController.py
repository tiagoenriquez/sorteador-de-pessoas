from flask import Blueprint, redirect, render_template, request, url_for
from src.models.Nome import Nome
from src.services import NomeService


nome_blueprint = Blueprint("nome", __name__, template_folder="templates", url_prefix="/nomes")

@nome_blueprint.route("/atualizacao/<id>", methods=["POST"])
def atualizar(id: int):
    NomeService.atualizar(Nome(id, request.form.get("nome")))
    return redirect(url_for("nome.listar"))

@nome_blueprint.route("/")
def listar():
    return render_template("nomes.html", nomes=NomeService.listar())

@nome_blueprint.route("/edicao/<id>")
def procurar(id: int):
    return render_template("atualizarNome.html", nome=NomeService.procurar(id))