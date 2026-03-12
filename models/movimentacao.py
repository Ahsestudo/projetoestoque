from banco_db.db import BancoDB
from datetime import datetime


class Movimentacao:

    def __init__(self, produto_id, tipo, quantidade, responsavel):

        self.produto_id = produto_id
        self.tipo = tipo
        self.quantidade = quantidade
        self.responsavel = responsavel
        self.data = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.db = BancoDB()

    def registrar(self):

        sql = """
        INSERT INTO movimentacoes
        (produto_id, tipo, quantidade, data, responsavel)
        VALUES (?, ?, ?, ?, ?)
        """

        self.db.cursor.execute(
            sql,
            (self.produto_id, self.tipo, self.quantidade, self.data, self.responsavel),
        )

        self.db.conexao.commit()

        print("Movimentação registrada com sucesso!")

    def listar_movimentacoes(self):

        self.db.cursor.execute(
            """
        SELECT m.id, p.nome, m.tipo, m.quantidade, m.data, m.responsavel
        FROM movimentacoes m
        JOIN produtos p ON p.id = m.produto_id
        """
        )

        movimentacoes = self.db.cursor.fetchall()

        print("\n===== HISTÓRICO DE MOVIMENTAÇÕES =====")

        for mov in movimentacoes:
            print(
                f"ID:{mov[0]} | Produto:{mov[1]} | "
                f"Tipo:{mov[2]} | Quantidade:{mov[3]} | "
                f"Data:{mov[4]} | Responsável:{mov[5]}"
            )
