from src.connections.Connection import con
from src.migrations.NomeMigration import nome_definition
from src.migrations.SobrenomeMigration import sobrenome_definition


def migrate():
    with con:
        con.execute(nome_definition)
        con.execute(sobrenome_definition)
        con.commit()