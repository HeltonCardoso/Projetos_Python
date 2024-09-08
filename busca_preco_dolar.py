from bs4 import BeautifulSoup
import requests
#import pandas as pd

#import smtplib
#import email.message

#URL = "https://www.dclassedecor.com.br/poltrona/poltrona-golden-pes-palito-suede-azul-tiffany-d-classe-decor"
URL = "https://dolarhoje.com/"
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}

site = requests.get(URL, headers=headers)


    
soup = BeautifulSoup(site.content, 'html.parser')

title = soup.find(class_='cotMoeda nacional')

if title:
    valor = title.get('value', 'Atributo não encontrado')
    print(f'Valor do imput:{valor}')
else:
    print('Elemento não encontrado')

#valor = soup.get('value')
#imprimi todo o HTML do site
#print(soup.prettify())
#busca o nome do produto dentro da tag(no caso esta dentro de H1, na classe product-name)
#title = soup.find('span', class_='cotMoeda nacional').get_text()
#preco = soup.find('span', class_='optional').get_text()
#preco = soup.find('span', id='variacaoPreco').get_text().strip()


#print(title)
#print(preco)

