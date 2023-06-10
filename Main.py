from Ingrediente import Ingrediente
from Receita import Receita

# Lista de ingredientes
ingredientes = []
# Função para criar um novo ingrediente
def criar_ingrediente():
    id_ing = int(input("Digite o ID do ingrediente: "))
    nome_ing = input("Digite o nome do ingrediente: ")
    ingrediente = Ingrediente(id_ing, nome_ing)
    return ingrediente

# Função para listar os ingredientes
def listar_ingredientes(ingredientes):
    if len(ingredientes) == 0:
        print("Não há ingredientes cadastrados.")
    else:
        print("Lista de Ingredientes:")
        for ingrediente in ingredientes:
            print(f"ID: {ingrediente.id_ing} | Nome: {ingrediente.nome_ing}")

# Função para remover um ingrediente
def remover_ingrediente(ingredientes):
    id_ing = int(input("Digite o ID do ingrediente a ser removido: "))
    for ingrediente in ingredientes:
        if ingrediente.id_ing == id_ing:
            ingredientes.remove(ingrediente)
            print("Ingrediente removido com sucesso.")
            return
    print("Ingrediente não encontrado.")

# Função para atualizar um ingrediente
def atualizar_ingrediente(ingredientes):
    id_ing = int(input("Digite o ID do ingrediente a ser atualizado: "))
    for ingrediente in ingredientes:
        if ingrediente.id_ing == id_ing:
            novo_nome = input("Digite o novo nome do ingrediente: ")
            ingrediente.nome_ing = novo_nome
            print("Ingrediente atualizado com sucesso.")
            return
    print("Ingrediente não encontrado.")

# Lista de receitas
receitas = []

# Função para criar uma nova receita
def criar_receita():
    id_rec = int(input("Digite o ID da receita: "))
    nome_rec = input("Digite o nome da receita: ")
    autor_rec = input("Digite o autor da receita: ")
    receita = Receita(id_rec, nome_rec, autor_rec)
    return receita

# Função para listar as receitas
def listar_receitas(receitas):
    if len(receitas) == 0:
        print("Não há receitas cadastradas.")
    else:
        print("Lista de Receitas:")
        for receita in receitas:
            print(f"ID: {receita.id_rec} | Nome: {receita.nome_rec} | Autor: {receita.autor_rec}")

# Função para remover uma receita
def remover_receita(receitas):
    id_rec = int(input("Digite o ID da receita a ser removida: "))
    for receita in receitas:
        if receita.id_rec == id_rec:
            receitas.remove(receita)
            print("Receita removida com sucesso.")
            return
    print("Receita não encontrada.")

# Função para atualizar uma receita
def atualizar_receita(receitas):
    id_rec = int(input("Digite o ID da receita a ser atualizada: "))
    for receita in receitas:
        if receita.id_rec == id_rec:
            novo_nome = input("Digite o novo nome da receita: ")
            receita.nome_rec = novo_nome
            print("Receita atualizada com sucesso.")
            return
    print("Receita não encontrada.")

# Lista de relações entre receitas e ingredientes
relacoes = []

# Loop para o usuário interagir com o programa
while True:
    print("\nMenu:")
    print("1. Criar Ingrediente")
    print("2. Listar Ingredientes")
    print("3. Remover Ingrediente")
    print("4. Atualizar Ingrediente")
    print("5. Criar Receita")
    print("6. Listar Receitas")
    print("7. Remover Receita")
    print("8. Atualizar Receita")
    print("9. Adicionar Ingredientes à Receita")
    print("10. Listar Ingredientes de uma Receita")
    print("11. Remover Relação entre Receita e Ingredientes")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        ingrediente = criar_ingrediente()
        ingredientes.append(ingrediente)
        print("Ingrediente criado com sucesso!")
    elif opcao == "2":
        listar_ingredientes(ingredientes)
    elif opcao == "3":
        remover_ingrediente(ingredientes)
    elif opcao == "4":
        atualizar_ingrediente(ingredientes)
    elif opcao == "5":
        receita = criar_receita()
        receitas.append(receita)
        print("Receita criada com sucesso!")
    elif opcao == "6":
        listar_receitas(receitas)
    elif opcao == "7":
        remover_receita(receitas)
    elif opcao == "8":
        atualizar_receita(receitas)
    elif opcao == "9":
        pass
    elif opcao == "10":
        pass
    elif opcao == "11":
        pass
    elif opcao == "0":
        break
    else:
        print("Opção inválida. Tente novamente.")