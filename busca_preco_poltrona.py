from bs4 import BeautifulSoup
import requests
#import pandas as pd

#import smtplib
#import email.message

#URL = "https://www.dclassedecor.com.br/poltrona/poltrona-golden-pes-palito-suede-azul-tiffany-d-classe-decor"
URL = "https://www.dclassedecor.com.br/cadeiras/cadeira-para-sala-de-jantar-lia-pes-palito-suede-marsala-d-classe-decor"
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}

site = requests.get(URL, headers=headers)


    
soup = BeautifulSoup(site.content, 'html.parser')


#imprimi todo o HTML do site
#print(soup.prettify())
#busca o nome do produto dentro da tag(no caso esta dentro de H1, na classe product-name)
title = soup.find('h1', class_='product-name').get_text()
preco = soup.find('span', id='variacaoPreco').get_text().strip()


print(title)
print("R$:",preco)




#num_preco = preco[0:6]
#num_preco = num_preco.replace(',','')
#num_preco = int(num_preco)

#def send_email():

 #      email_conteudo = """https://www.dclassedecor.com.br/poltrona/poltrona-golden-pes-palito-suede-azul-tiffany-d-classe-decor"""


  #     msg = email.message.Message()
   #    msg['Subject'] = 'Preço Baixou'

    #   msg['From'] = ''
     #  msg['To'] = 'contatorafadecor@gmail.com'
      # password = 'Helton100%'
      # msg.add_hearder('Content-Type','text/html')
      # msg.set_payload(email_conteudo)

      # s = smtplib.SMTP('heltoncardososuaves@gmail.com: 587')
      # s.starttls()
      ## s.login(msg['From'],password)
       #s.sendmail(msg['From'], [msg['To']], msg.as_string())


#print("Sucesso enviar email#")

#if( num_preco <=100):
 #       send_email()




