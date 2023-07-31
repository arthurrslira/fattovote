import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.camara.leg.br/deputados/quem-sao/resultado"
params = {
    "search": "",
    "partido": "",
    "uf": "",
    "legislatura": "57",
    "sexo": "",
    "pagina": 1,
}

deputados = []

while True:
    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')
    deputados_html = soup.find_all('li', class_='lista-resultados__item')

    if not deputados_html:
        break

    for deputado_html in deputados_html:
        nome_deputado_com_partido = deputado_html.find('a').text
        partido = nome_deputado_com_partido.split('(', 1)[-1].replace(')', '')
        nome_deputado = nome_deputado_com_partido.split('(', 1)[0].strip()
        link_imagem = deputado_html.find('img')['src']

        deputados.append({
            'Nome do Deputado': nome_deputado,
            'Partido': partido,
            'Link da Imagem': link_imagem
        })

    params["pagina"] += 1

df = pd.DataFrame(deputados)

nome_arquivo_excel = 'deputados_imagens.xlsx'
df.to_excel(nome_arquivo_excel, index=False)

print(f"Arquivo Excel '{nome_arquivo_excel}' criado com sucesso!")
