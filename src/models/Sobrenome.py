class Sobrenome:
    def __init__(self, id: int, nome: str):
        self.id = id
        self.nome = nome
    
    def to_dict(self):
        return {"id": self.id, "nome": self.nome}
    
    def to_array(self):
        return [self.nome, self.id]