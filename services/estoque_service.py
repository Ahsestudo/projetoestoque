from models.movimentacao import Movimentacao
from banco_db.db import BancoDB

db = BancoDB()


def entrada_produto():

    produto_id = int(input("ID do produto: "))
    quantidade = int(input("Quantidade recebida: "))
    responsavel = input("Responsável: ")

    db.cursor.execute(
        "UPDATE produtos SET quantidade = quantidade + ? WHERE id=?",
        (quantidade, produto_id),
    )

    db.conexao.commit()

    movimentacao = Movimentacao(produto_id, "entrada", quantidade, responsavel)
    movimentacao.registrar()


def saida_produto():

    produto_id = int(input("ID do produto: "))
    quantidade = int(input("Quantidade retirada: "))
    responsavel = input("Responsável: ")

    db.cursor.execute("SELECT quantidade FROM produtos WHERE id=?", (produto_id,))

    estoque = db.cursor.fetchone()

    if estoque[0] < quantidade:
        print("Estoque insuficiente!")
        return

    db.cursor.execute(
        "UPDATE produtos SET quantidade = quantidade - ? WHERE id=?",
        (quantidade, produto_id),
    )

    db.conexao.commit()

    movimentacao = Movimentacao(produto_id, "saida", quantidade, responsavel)
    movimentacao.registrar()
