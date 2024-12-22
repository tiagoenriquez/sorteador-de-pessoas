import random


class Pessoa:
    def __init__(self, nome: str, sobrenomes: list[str]):
        self.nome = f"{nome} {" ".join(sobrenomes)}"
        self.sortear_cpf()
        self.sortear_telefone()
        self.sortear_usuario(nome, sobrenomes[-1])
        self.sortear_email()
        self.sortear_senha()
    
    def sortear_cpf(self):
        cpf = str(random.randint(0, 99999999999)).zfill(11)
        self.cpf = f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"
    
    def sortear_telefone(self):
        telefone = str(random.randint(0, 99999999)).zfill(8)
        self.telefone = f"9{telefone[0:4]}-{telefone[4:8]}"
    
    def sortear_usuario(self, nome: str, sobrenome: str):
        self.usuario = f"{nome.lower()}.{sobrenome.lower()}{str(random.randint(0, 99))}".replace(" ", "-")
    
    def sortear_email(self):
        servidores = ["gmail", "outlook", "protonmail"]
        self.email = f"{self.usuario}@{random.choice(servidores)}.com"
    
    def sortear_senha(self):
        caracteres = list("qwertyuiopasdfghjklçzxcvbnmQWERTYUIOPASDFGHJKLÇZXCVBNM!@#$%&*()_=+,<.>;:/?[{]}")
        qtd_digitos = random.randint(8, 15)
        self.senha = ""
        for i in range(qtd_digitos):
            self.senha += random.choice(caracteres)
    
    def to_dict(self):
        return {
            "nome": self.nome,
            "cpf": self.cpf,
            "telefone": self.telefone,
            "email": self.email,
            "usuario": self.usuario,
            "senha": self.senha
        }