from src.models.Sobrenome import Sobrenome
from src.repositories import SobrenomeRepository


def atualizar(sobrenome: Sobrenome):
    SobrenomeRepository.atualizar(sobrenome)

def excluir(id: int):
    SobrenomeRepository.excluir(id)

def listar():
    return SobrenomeRepository.ordenar()

def procurar(id: int):
    return SobrenomeRepository.procurar(id)