from src.connections.Connection import con
from src.models.Nome import Nome


def inserir(nome: str):
    with con:
        con.execute("insert into nomes (nome) values (?)", [nome])
        con.commit()

def listar():
    with con:
        cur = con.cursor()
        cur.execute("select * from nomes")
        nomes: list[Nome] = []
        for row in cur.fetchall():
            nomes.append(Nome(row[0], row[1]))
        return nomes

def procurar(id: int):
    with con:
        cur = con.cursor()
        cur.execute("select * from nomes where id = ?", [id])
        res = cur.fetchone()
        return Nome(res[0], res[1])