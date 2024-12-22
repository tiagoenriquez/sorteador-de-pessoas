from src.connections.Connection import con
from src.models.Sobrenome import Sobrenome


def inserir(nome: str):
    with con:
        con.execute("insert into sobrenomes (nome) values (?)", [nome])
        con.commit()

def listar():
    with con:
        cur = con.cursor()
        cur.execute("select * from sobrenomes")
        sobrenomes: list[Sobrenome] = []
        for row in cur.fetchall():
            sobrenomes.append(Sobrenome(row[0], row[1]))
        return sobrenomes

def procurar(id: int):
    with con:
        cur = con.cursor()
        cur.execute("select * from sobrenomes where id = ?", [id])
        res = cur.fetchone()
        return Sobrenome(res[0], res[1])