import json
import re
from collections import Counter

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def fixWord(inputString):
    ret = ''
    for c in inputString:
        if (c.isalpha()):
            ret += c
    return ret

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
            hprice[price].append([cur_id, 1, 0])
        else:
            hprice[price] = []
            hprice[price].append([cur_id, 1, 0])

        #indexing products:
        produto = obj['produto']
        pos = 0
        for word in produto.split(' '):
            if (hasNumbers(word)): 
                continue
            word = fixWord(word)
            if (len(word) > 5):
                word = word.lower()
                if (word in hproduto):
                    hproduto[word].append([cur_id, 1, pos])
                else:
                    hproduto[word] = []
                    hproduto[word].append([cur_id, 1, pos])
            pos += 1

        #indexing sites:
        site = obj['site']
        if (site in hsite):
            hsite[site].append([cur_id, 1, 0])
        else:
            hsite[site] = []
            hsite[site].append([cur_id, 1, 0])
        
        #indexing pharmacies:
        farmacia = obj['farmacia']
        if (farmacia in hfarmacia):
            hfarmacia[farmacia].append([cur_id, 1, 0])
        else:
            hfarmacia[farmacia] = []
            hfarmacia[farmacia].append([cur_id, 1, 0])

        #indexing summaries:
        sumario = obj['sumario']
        pos = 0
        for word in sumario.split(' '):
            if (hasNumbers(word)): 
                continue
            if (len(word) > 5):
                word = word.lower()
                if (word in hsumario):
                    hsumario[word].append([cur_id, 1, pos])
                else:
                    hsumario[word] = []
                    hsumario[word].append([cur_id, 1, pos])
            pos += 1
        
        cur_id = cur_id + 1

    for item in sorted(hfarmacia.items()):
        print ("farmacia." + list(item)[0]),
        print (': '),
        print (list(item)[1])
    
    for item in sorted(hprice.items()):
        print ("price." + list(item)[0]),
        print (': '),
        print (list(item)[1])

    for item in sorted(hproduto.items()):
        print ("produto." + list(item)[0]),
        print (': '),
        print (list(item)[1])

    for item in sorted(hsite.items()):
        print ("site." + list(item)[0]),
        print (': '),
        print (list(item)[1])

    for item in sorted(hsumario.items()):
        print ("sumario." + list(item)[0]),
        print (': '),
        print (list(item)[1])