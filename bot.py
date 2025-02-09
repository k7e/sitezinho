import requests
import unicodedata
import re


def extrair_conteudo_html(html):

    padrao = r'autofocus>(.*?)</textarea>'
    resultado = re.search(padrao, html, re.DOTALL)  

    if resultado:
        return resultado.group(1) 
    else:
        return None  


headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.invertexto.com/notepad',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
}
response = requests.get('https://www.invertexto.com/aguiabrancabot123', headers=headers)
texto = extrair_conteudo_html(response.text)


def send_discord_message(webhook_url, message):
    data = {"content": message,
            "avatar_url": "https://media.discordapp.net/attachments/1335586504201736273/1338005751624499340/df67d815d73d872f510c8cbbf9c0d0a7.jpg?ex=67a98276&is=67a830f6&hm=4526e858233b9343db3ac6e1e7f680c2a820a124d7e105767ac699e6cb7ef831&=&format=webp&width=350&height=350"}
    response = requests.post(webhook_url, json=data)
    
    if response.status_code == 204:
        print("Mensagem enviada com sucesso!")
    else:
        print(f"Erro ao enviar mensagem: {response.status_code} - {response.text}")

# Exemplo de uso
WEBHOOK_URL = "https://discord.com/api/webhooks/1338006661029298246/LYIh9-jnupXcB4B3fVnr7Rnq1NNij-VEz-szFwjpYo4JJL3rnMHcLeCYgL4CDhgp7Usj"


send_discord_message(WEBHOOK_URL, texto)
