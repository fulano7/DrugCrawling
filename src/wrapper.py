import requests
import os
import json
from bs4 import BeautifulSoup
from collections import deque

#folder where extraction happens
PATH = '../classificados'

#folder where extraction is saved
EXT = '../extraction'

def onofre_w(soup):
    obj = {}
    obj['produto'] = soup.find('span', id='lblProductName').text
    obj['price'] = soup.find('span', class_='regular-price').text
    obj['sumario'] = soup.title.text
    obj['farmacia'] = 'Onofre'
    obj['site'] = 'www.onofre.com.br'
    return obj

def uf_w(soup):
    obj = {}
    obj['produto'] = soup.find('h1', class_='div_nome_prod').text
    obj['price'] = soup.find('div', class_='txt_preco_por').text
    obj['sumario'] = soup.title.text
    obj['farmacia'] = 'Ultra Farma'
    obj['site'] = 'www.ultrafarma.com.br'
    return obj
    
def farmadelivery_w(soup):
    obj = {}
    obj['produto'] = soup.find('div', class_='product-name').text
    obj['price'] = soup.find_all('span', class_='price')[1].text
    obj['sumario'] = soup.title.text
    obj['farmacia'] = 'Farma Delivery'
    obj['site'] = 'www.farmadelivery.com.br'
    return obj
    
def farma22_w(soup):
    obj = {}
    obj['produto'] = soup.title.text
    obj['price'] = soup.find_all('strong', class_='skuPrice')[0].text
    obj['sumario'] = soup.title.text
    obj['farmacia'] = 'Farma 22'
    obj['site'] = 'www.farma22.com.br'
    return obj
    
def farmagora_w(soup):
    obj = {}
    obj['produto'] = soup.find('div', class_='columns small-12 hidden-for-large-up').text
    obj['price'] = soup.find('span', class_='preco-por').text
    obj['sumario'] = soup.title.text
    obj['farmacia'] = 'Farmagora'
    obj['site'] = 'www.farmagora.com.br'
    return obj
    
def drogariasp_w(soup):
    obj = {}
    obj['produto'] = soup.find('span', class_='glis-sku-single-item').text
    obj['price'] = soup.find('em', class_='valor-por').text
    obj['sumario'] = soup.title.text
    obj['farmacia'] = 'Drogaria Sao Paulo'
    obj['site'] = 'www.drogariasaopaulo.com.br'
    return obj
    
def cristorei_w(soup):
    obj = {}
    obj['produto'] = soup.find('li', class_='product').text
    obj['price'] = soup.find_all('span', class_='price')[1].text
    obj['sumario'] = soup.title.text
    obj['farmacia'] = 'Farmacia Cristo Rei'
    obj['site'] = 'www.farmaciacristorei.com.br'
    return obj

def sare_w(soup):
    obj = {}
    obj['produto'] = soup.title.text
    obj['price'] = soup.find('p', class_='text-success').text
    obj['sumario'] = soup.title.text
    obj['farmacia'] = 'Sare Drogarias Online'
    obj['site'] = 'www.saredrogarias.com.br'
    return obj

def wrap(document, filename):
    soup = BeautifulSoup(open(document), 'html.parser')
    obj = {}
    if ('onofre' in filename):
        obj = onofre_w(soup)
    elif('ultrafarma' in filename):
        obj = uf_w(soup)
    elif('farmadelivery' in filename):
        obj = farmadelivery_w(soup)
    elif('farma22' in filename):
        obj = farma22_w(soup)
    elif('farmagora' in filename):
        obj = farmagora_w(soup)
    elif('drogariasaopaulo' in filename):
        obj = drogariasp_w(soup)
    elif('cristorei' in filename):
        obj = cristorei_w(soup)
    elif('saredrogarias' in filename):
        obj = sare_w(soup)
    return obj

for filename in os.listdir(PATH):
    document = os.path.join(PATH, filename)
    try:
        obj = wrap(document, filename)
        if (obj != {}):
            print(obj)
        else:
            continue
    except:
        continue
            

