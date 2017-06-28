import json
import re
from collections import Counter

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

with open('extraction/data.js') as json_data:
    objs = json.load(json_data)
    cur_id = 1

    hprice = dict()
    hproduto = dict()
    hsite = dict()
    hfarmacia = dict()
    hsumario = dict()

    for obj in objs:
        price = re.findall(r'\d+', obj['price'])[0]

        if (price in hprice):
            hprice[price].append(cur_id)
        else:
            hprice[price] = []
            hprice[price].append(cur_id)

        #indexing products:
        produto = obj['produto']
        for word in produto.split(' '):
            if (hasNumbers(word)): 
                continue
            if (len(word) > 5):
                word = word.lower()
                if (word in hproduto):
                    hproduto[word].append(cur_id)
                else:
                    hproduto[word] = []
                    hproduto[word].append(cur_id)

        #indexing sites:
        site = obj['site']
        if (site in hsite):
            hsite[site].append(cur_id)
        else:
            hsite[site] = []
            hsite[site].append(cur_id)
        
        #indexing pharmacies:
        farmacia = obj['farmacia']
        if (farmacia in hfarmacia):
            hfarmacia[farmacia].append(cur_id)
        else:
            hfarmacia[farmacia] = []
            hfarmacia[farmacia].append(cur_id)

        #indexing summaries:
        sumario = obj['sumario']
        for word in sumario.split(' '):
            if (hasNumbers(word)): 
                continue
            if (len(word) > 5):
                word = word.lower()
                if (word in hsumario):
                    hsumario[word].append(cur_id)
                else:
                    hsumario[word] = []
                    hsumario[word].append(cur_id)

        cur_id = cur_id + 1
    
    for item in hsumario.items():
        print (list(item)[0]),
        print (': '),
        print (list(item)[1])