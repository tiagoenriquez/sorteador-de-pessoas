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