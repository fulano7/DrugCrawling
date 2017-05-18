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
    obj['produto'] = soup.find_all('span', id='lblProductName')[0].text
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
    return obj

for filename in os.listdir(PATH):
    document = os.path.join(PATH, filename)
    obj = wrap(document, filename)
    if (obj != {}):
        if ('farma22' in filename):
            print(obj)
    else:
        continue
            

