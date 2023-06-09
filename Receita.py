class Receita:
    id_receita = 0
    nome_receita = ""
    autor_receita = ""

def criar_receita():
    id_receita = int(input("Informe o ID da receita: "))
    nome_receita = input("Informe o Nome da receita: ")
    autor_receita = input("Informe o Autor da receita: ")
    receita = Receita(id_receita, nome_receita, autor_receita)
    return receita