import random
from src.models.Pessoa import Pessoa
from src.repositories import NomeRepository, SobrenomeRepository


def inserir(nome: str):
    partes = nome.split(" ")
    primeiro_nome = partes[0]
    sobrenomes: list[str] = []
    conectivo = ""
    for i, parte in enumerate(partes[1:]):
        if not parte[0].isupper():
            conectivo = f"{parte} "
        else:
            sobrenomes.append(f"{conectivo}{parte}")
            conectivo = ""
    for sobrenome in sobrenomes:
        SobrenomeRepository.inserir(sobrenome)
    NomeRepository.inserir(primeiro_nome)

def sortear(qtd: int):
    pessoas: list[Pessoa] = []
    for i in range(qtd):
        qtd_sobrenomes = random.choice([2, 3])
        sobrenomes: list[str] = []
        for i in range(qtd_sobrenomes):
            sobrenomes.append(SobrenomeRepository.procurar(random.choice(SobrenomeRepository.listar()).id).nome)
        pessoas.append(Pessoa(NomeRepository.procurar(random.choice(NomeRepository.listar()).id).nome, sobrenomes))
    return pessoas