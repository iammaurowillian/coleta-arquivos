import requests
import os
from bs4 import BeautifulSoup

url = "https://simpleenergy.com.br/teste/"
codigos = ["321465", "98465"]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Accept": "text/html,application/pdf"
}

pasta_arquivo = "C:/coleta_arquivos/data"

if not os.path.exists(pasta_arquivo):
    os.makedirs(pasta_arquivo)

with requests.Session() as session:
    for codigo in codigos:
        response = requests.post(
            url,
            data={"codigo": codigo,
                  "csrf": "e8aa9581032659f46599bcd8cde487b167bbd125c98ef7072e0a57f4580e16cc"
                  },
            headers=headers
        )

        if response.status_code == 200:
            print(f"Autenticação Realizada: {codigo}")
            soup = BeautifulSoup(response.text, "html.parser")
            links = soup.find_all("a")

            for link in links:
                if link.get("href") and (link["href"].endswith(".txt") or link["href"].endswith(".pdf")):

                    arquivo_url = url + link["href"]
                    arquivo_nome = arquivo_url.split("/")[-1]
                    arquivo_path = os.path.join(pasta_arquivo, arquivo_nome)
                    arquivo_response = requests.get(arquivo_url, headers=headers)

                    if arquivo_response.status_code == 200:
                        with open(arquivo_path, 'wb') as arquivo:
                            arquivo.write(arquivo_response.content)

                        print(f"Download concluído: {arquivo_nome}")
                    else:
                        print(f"Falha ao fazer o download de {arquivo_nome}")
        else:
            print(f"Falha ao enviar o código {codigo}")
