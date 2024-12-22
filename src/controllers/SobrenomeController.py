from flask import Blueprint, redirect, render_template, request, url_for
from src.services import SobrenomeService


sobrenome_blueprint = Blueprint("sobrenome", __name__, template_folder="templates")

@sobrenome_blueprint.route("/sobrenomes")
def listar():
    return render_template("sobrenomes.html", sobrenomes=SobrenomeService.listar())