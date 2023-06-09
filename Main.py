from Ingrediente import Ingrediente

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
        pass
    elif opcao == "6":
        pass
    elif opcao == "7":
        pass
    elif opcao == "8":
        pass
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