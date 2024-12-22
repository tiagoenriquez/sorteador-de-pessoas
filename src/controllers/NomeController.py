from flask import Blueprint, redirect, render_template, request, url_for
from src.services import NomeService


nome_blueprint = Blueprint("nome", __name__, template_folder="templates")

@nome_blueprint.route("/nomes")
def listar():
    return render_template("nomes.html", nomes=NomeService.listar())