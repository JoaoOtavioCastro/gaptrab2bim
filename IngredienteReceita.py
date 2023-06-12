from Ingrediente import Ingrediente
from Receita import Receita

class RelacaoReceitaIngrediente:
    def __init__(self, receita, ingrediente, qtd):
        self.receita = receita
        self.ingrediente = ingrediente
        self.qtd = qtd