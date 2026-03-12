from banco_db.db import BancoDB


class Produto:

    def __init__(self, nome, quantidade=0):
        self.nome = nome
        self.quantidade = quantidade
        self.db = BancoDB()

    def cadastrar(self):

        sql = "INSERT INTO produtos (nome, quantidade) VALUES (?, ?)"
        self.db.cursor.execute(sql, (self.nome, self.quantidade))
        self.db.conexao.commit()

        print("Produto cadastrado com sucesso!")

    def listar(self):

        self.db.cursor.execute("SELECT * FROM produtos")
        produtos = self.db.cursor.fetchall()

        for p in produtos:
            print(f"ID:{p[0]} | Nome:{p[1]} | Quantidade:{p[2]}")
