import sqlite3


class BancoDB:

    def __init__(self):
        self.conexao = sqlite3.connect("estoque.db")
        self.cursor = self.conexao.cursor()

    def criar_tabelas(self):

        self.cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS produtos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            quantidade INTEGER
        )
        """
        )

        self.cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS movimentacoes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto_id INTEGER,
            tipo TEXT,
            quantidade INTEGER,
            data TEXT,
            responsavel TEXT
        )
        """
        )

        self.conexao.commit()
