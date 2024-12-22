from flask import Blueprint, redirect, render_template, request, url_for
from src.models.Sobrenome import Sobrenome
from src.services import SobrenomeService


sobrenome_blueprint = Blueprint("sobrenome", __name__, template_folder="templates", url_prefix="/sobrenomes")

@sobrenome_blueprint.route("/atualizacao/<id>", methods=["POST"])
def atualizar(id: int):
    SobrenomeService.atualizar(Sobrenome(id, request.form.get("nome")))
    return redirect(url_for("sobrenome.listar"))

@sobrenome_blueprint.route("/exclusao/<id>")
def excluir(id: int):
    SobrenomeService.excluir(id)
    return redirect(url_for("sobrenome.listar"))

@sobrenome_blueprint.route("/")
def listar():
    return render_template("sobrenomes.html", sobrenomes=SobrenomeService.listar())

@sobrenome_blueprint.route("/edicao/<id>")
def editar(id: int):
    return render_template("atualizarSobrenome.html", sobrenome=SobrenomeService.procurar(id))