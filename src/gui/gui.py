import customtkinter as ctk
import sqlite3
from notifier_gui import notifier_crg
from notifier_gui import notifier_lgg
from notifier_gui import notifierErrorlg

with sqlite3.connect("db_gui.db") as debe:
    admin = debe.cursor()
    admin.execute("CREATE TABLE IF NOT EXISTS users (nome text, password text)")

def criarConta():
    nomeValue = nome.get()
    senhaValue = senha.get()

    admin.execute("INSERT INTO users VALUES (?, ?)", (nomeValue, senhaValue))
    notifier_crg(nomeValue, senhaValue)
    debe.commit()

def logarConta():
    nomeValue = nome.get()
    senhaValue = senha.get()
    admin.execute("SELECT * FROM users WHERE nome = ? and password = ?", (nomeValue, senhaValue)) # Placeholders, evita SQL Injection.
    res = admin.fetchone()
    if res:
        notifier_lgg(nomeValue, senhaValue)
    else:
        notifierErrorlg(nomeValue, senhaValue)



app = ctk.CTk()

def submitN(event=None):
    valueN = nome.get()

def submitP(event=None):
    valueP = senha.get()

app.title("GORBACHEV.DB")
app.geometry("200x200")

nome = ctk.CTkEntry(app, placeholder_text="Nome")
nome.place(x=20, y=20)

senha = ctk.CTkEntry(app, placeholder_text="Password", show="*")
senha.place(x=20, y=70)


SUBMIT_CR = ctk.CTkButton(app, text="Signup", command=criarConta)
SUBMIT_CR.place(x=20, y=120)


SUBMIT_LG = ctk.CTkButton(app, text="Login", command=logarConta)
SUBMIT_LG.place(x=20, y=160)


app.mainloop()
