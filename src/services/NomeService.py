from src.models.Nome import Nome
from src.repositories import NomeRepository


def atualizar(nome: Nome):
    NomeRepository.atualizar(nome)

def excluir(id: int):
    NomeRepository.excluir(id)

def listar():
    return NomeRepository.ordenar()

def procurar(id: int):
    return NomeRepository.procurar(id)