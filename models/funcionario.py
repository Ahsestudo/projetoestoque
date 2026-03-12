from banco_db.db import Banco_DB


class Funcionario:

    def __init__(self, nome, cpf, senha):

        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.db = Banco_DB()

    def salvar(self):

        sql = "INSERT INTO funcionarios (nome, cpf, senha) VALUES (?, ?, ?)"

        self.db.conexao.commit()

        print("Funcionário cadastrado com sucesso!")
