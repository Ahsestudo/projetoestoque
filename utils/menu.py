from services.estoque_service import entrada_produto, saida_produto
from models.produto import Produto
from models.movimentacao import Movimentacao


def menu():

    while True:

        print("\n===== SISTEMA DE ESTOQUE =====")
        print("1 - Cadastrar Produto")
        print("2 - Listar Produtos")
        print("3 - Entrada de Produto")
        print("4 - Saída de Produto")
        print("5 - Ver Movimentações")
        print("6 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            produto = Produto(nome)
            produto.cadastrar()

        elif opcao == "2":
            Produto("").listar()

        elif opcao == "3":
            entrada_produto()

        elif opcao == "4":
            saida_produto()

        elif opcao == "5":
            mov = Movimentacao(0, "", 0, "")
            mov.listar_movimentacoes()

        elif opcao == "6":
            break

        else:
            print("Opção inválida!")
