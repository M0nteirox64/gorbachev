import sqlite3
import time
from notifier import notifier_cr
from notifier import notifier_lg

def main():
    with sqlite3.connect("database.db") as db:
        adm = db.cursor()
    adm.execute("CREATE TABLE IF NOT EXISTS users (nome text, senha text)") 

    print("bem vindo a gorbachev.db")

    print("1) criar conta")
    print("2) logar na sua conta")

    chc = int(input("> "))

    if chc == 1:
        nomeC = input("[*] nome: ")
        senhaC = input("[*] senha: ")
        adm.execute(f"INSERT INTO users VALUES ('{nomeC}', '{senhaC}')")
        db.commit()
        notifier_cr(nomeC, senhaC)
        print("[*] conta criada com sucesso.")
        print("[-] a fechar o terminal em 3 segundos.")
        time.sleep(3)


    elif chc == 2:
        nomeL = input("[*] nome: ")
        senhaL = input("[*] senha: ")
        adm.execute("SELECT * FROM users WHERE nome = ? and senha = ?", (nomeL, senhaL)) # Placeholders, evita SQL Injection.
        res = adm.fetchone()
        if res: 
            print("[*] bem vindo!")
            notifier_lg(nomeL, senhaL)
            print("[*] a fechar o terminal em 3 segundos")
            time.sleep(3)
        else:
            print("[ :( ] a tua conta nao foi encontrada na database.")
            print("[ - ] a fechar o terminal em 3 segundos.")
            time.sleep(3)

if __name__ == "__main__":
    main()
