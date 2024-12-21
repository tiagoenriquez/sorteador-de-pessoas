from src.connections.Connection import con


def inserir(nome: str):
    with con:
        con.execute("insert into nomes (nome) values (?)", [nome])
        con.commit()