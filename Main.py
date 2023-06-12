from Ingrediente import Ingrediente
from Receita import Receita
from IngredienteReceita import RelacaoReceitaIngrediente

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

# Lista de relação Receita X Ingredientes
relacoes = []

#Função para criar uma relação Receita X Ingredientes
def adicionar_ingredientes(receita):
    ingrediente_id = int(input("Digite o ID do ingrediente: "))
    ingrediente = None
    for i in ingredientes:
        if i.id_ing == int(ingrediente_id):
            ingrediente = i
            break
    if ingrediente is None:
        print(f"Ingrediente com ID {ingrediente_id} não encontrado.")
        return
    ingredientes.append(ingrediente)
    qtd = input("Informe a quantidade desse ingrediente:")
    relacao = RelacaoReceitaIngrediente(receita, ingredientes, qtd)
    return relacao

#Função para listar a relação Receita X Ingredientes
def listar_ingredientes_da_receita(receita, relacoes, ingredientes):
    ingredien = []
    for relacao in relacoes:
        if relacao.receita == receita:
            ingredien.append(relacao)

    if len(ingredien) == 0:
        print("Não há ingredientes cadastrados para esta receita.")
    else:
        print(f"Ingredientes da receita '{receita.nome_rec}':")
        for ingre in ingredien:
            pesquisa_ingrediente(ingre.ingrediente, ingredientes)

#Função para excluir uma relação Receita X Ingredientes
def remover_relacao_receita_ingredientes(receita, relacoes):
    for relacao in relacoes:
        if relacao.receita == receita:
            relacoes.remove(relacao)
            print("Relação entre receita e ingredientes removida com sucesso.")
            return
    print("Relação entre receita e ingredientes não encontrada.")

#Função para alterar um relação Receita X Ingredientes
def atualizar_relacao_receita_ingredientes(receita, relacoes):
    for relacao in relacoes:
        if relacao.receita == receita:
            novo_quantidade = float(input(f"Digite a nova quantidade de {relacao.ingrediente.nome_ing} necessária: "))
            relacao.quantidade = novo_quantidade
            print("Relação entre receita e ingredientes atualizada com sucesso.")
            return
    print("Relação entre receita e ingredientes não encontrada.")

def pesquisa_ingrediente(id_ing, ingredientes):
    qtd = 0
    for ingrediente in ingredientes:
        if id_ing == ingrediente.id_ing:
            qtd=1
            print(f"ID: {ingrediente.id_ing} | Nome: {ingrediente.nome_ing}")
    if qtd==0:
        print("Sem ingrediente!")

def pesquisa_receita(id_ing, ingredientes):
    qtd = 0
    for ingrediente in ingredientes:
        if id_ing == ingrediente.id_rec:
            qtd=1
            print(f"ID: {ingrediente.id_rec} | Nome: {ingrediente.nome_rec} | Autor: {ingrediente.autor_rec}")
    if qtd==0:
        print("Sem ingrediente!")

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
    print("12. Atualizar Ingredientes de uma Receita")
    print("13. Pesquisar Ingrediente")
    print("14. Pesquisar Receita")
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
        id_rec = int(input("Digite o ID da receita: "))
        receita = None
        for r in receitas:
            if r.id_rec == id_rec:
                receita = r
                break
        if receita is None:
            print("Receita não encontrada.")
        else:
            relacao = adicionar_ingredientes(receita)
            if relacao:
                relacoes.append(relacao)
                print("Ingredientes adicionados à receita com sucesso!")
    elif opcao == "10":
        id_rec = int(input("Digite o ID da receita: "))
        receita = None
        for r in receitas:
            if r.id_rec == id_rec:
                receita = r
                break
        if receita is None:
            print("Receita não encontrada.")
        else:
            listar_ingredientes_da_receita(receita, relacoes, ingredientes)
    elif opcao == "11":
        remover_relacao_receita_ingredientes(receita, relacoes)
    elif opcao == "12":
        atualizar_relacao_receita_ingredientes(receita, relacoes)
    elif opcao== "13":
        id = int(input("Informe o id do ingrediente:"))
        pesquisa_ingrediente(id, ingredientes)
    elif opcao== "14":
        id = int(input("Informe o id da receita:"))
        pesquisa_ingrediente(id, receitas)
    elif opcao == "0":
        break
    else:
        print("Opção inválida. Tente novamente.")
