from banco_db.db import BancoDB
from utils.menu import menu

if __name__ == "__main__":

    banco = BancoDB()
    banco.criar_tabelas()

    menu()
