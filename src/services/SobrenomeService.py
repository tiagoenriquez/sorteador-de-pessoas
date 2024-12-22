from src.models.Sobrenome import Sobrenome
from src.repositories import SobrenomeRepository


def atualizar(sobrenome: Sobrenome):
    SobrenomeRepository.atualizar(sobrenome)

def listar():
    return SobrenomeRepository.ordenar()

def procurar(id: int):
    return SobrenomeRepository.procurar(id)