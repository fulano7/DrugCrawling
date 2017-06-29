from appJar import gui
from process import *
from queue import PriorityQueue
import json
import re

rank1 = process_query('produto.frálda produto.pâmpérs',1,UNCOMPRESSED)
l1 = queue_to_list(rank1)
print(l1)
data_f = open('extraction/data.js')
data = json.load(data_f)

app = gui()

def press(btn):
    if btn=="OK":
        print(app.getEntry('produto'))
        query = ''
        produto = ['produto.'+s for s in app.getEntry('produto').split(' ') if s != '']
        for p in produto:
            query += (p+' ')
        farmacia = ['farmacia.'+s for s in app.getEntry('farmacia').split(' ') if s != '']
        for f in farmacia:
            query += (f+' ')
        site = ['site.'+s for s in app.getEntry('site').split(' ') if s != '']
        for st in site:
            query += (st+' ')
        sumario = ['sumario.'+s for s in app.getEntry('sumario').split(' ') if s != '']
        for suma in sumario:
            query += (suma+' ')
        prices = app.getOptionBox("price")
        if prices != 'Any':
            query += ('price.['+prices+'] ')
        #print('price.['+prc[0]+'] ')
        rank = process_query(query,1,UNCOMPRESSED)
        lis = queue_to_list(rank)
        app2 = gui()
        app2.startPagedWindow('Results')
        for indx, item in enumerate(lis):
            app2.startPage()
            app2.addLabel('1'+str(indx), "RESULTS", 0, 0, 2)  # Row 0,Column 0,Span 2
            print('indice do doc: ',item[0])
            app2.addLabel('2'+str(indx), "Product: "+data[item[0]]['produto'], 1, 0)              # Row 1,Column 0
            app2.addLabel('3'+str(indx), "Drugstore: "+data[item[0]]['farmacia'], 2, 0)
            app2.addLabel('4'+str(indx), "Site: "+data[item[0]]['site'], 3, 0)
            app2.addLabel('5'+str(indx), "Summary: "+data[item[0]]['sumario'], 4, 0)
            app2.addLabel('6'+str(indx), "Price: "+data[item[0]]['price'], 5, 0)
            app2.stopPage()
        app2.stopPagedWindow()
        app2.go()

app.addLabel("title", "SEARCH", 0, 0, 2)  # Row 0,Column 0,Span 2
app.addLabel("produto_l", "Product:", 1, 0)              # Row 1,Column 0
app.addEntry("produto", 1, 1)
#app.addLabel("maximo", "Consumer Secret:", 2, 0)
#app.addEntry("maximo", 2, 1) 
#app.addLabel("accessToken", "Access Token:", 3, 0)
#app.addEntry("accessToken", 3, 1)
#app.addLabel("accessTokenSecret", "Access Token Secret:", 4, 0)
#app.addEntry("accessTokenSecret", 4, 1)
app.addLabel("farmacia_l", "Drugstore:", 2, 0)              # Row 1,Column 0
app.addEntry("farmacia", 2, 1)
app.addLabel("site_l", "Site:", 3, 0)              # Row 1,Column 0
app.addEntry("site", 3, 1)
app.addLabel("sumario_l", "Summary:", 4, 0)              # Row 1,Column 0
app.addEntry("sumario", 4, 1)
app.addLabel("price_l", "Price in BRL: ", 5, 0)
app.addOptionBox("price", ['Any','0-3','4-10','11-15','16-20','21-50','51-100','101-300','300+'],5,1)
app.addButton("OK", press, 6, 0, 2)

#app.setEntryFocus("buscar")

app.go()

'''global added
		if added == False:
			app.addEmptyMessage("res")
			added = True
		criterio = app.getEntry("buscar")
		criterio = urllib.parse.quote_plus(criterio)
		results = api.search(criterio,rpp=200,pages=1)
		positivo = 0
		negativo = 0
		neutro = 0
		total = 0
		for result in results:
			r2 = result.text.encode(sys.stdout.encoding, errors='replace')
			req = urllib.request.Request(url, data = text_bytes+r2)
			analysis = urllib.request.urlopen(req)
			analysis = analysis.read().decode('utf-8')
			analysis_json = json.loads(analysis)
			if analysis_json['label'] == 'pos':
				positivo = positivo + 1
			elif analysis_json['label'] == 'neg':
				negativo = negativo + 1
			elif analysis_json['label'] == 'neutral':
				neutro = neutro + 1
			total = total + 1
		porcentagemPos = (positivo/total)*100
		porcentagemNeg = (negativo/total)*100
		porcentagemNeu = (neutro/total)*100
		porcentagem1 = "{:.2f}".format(porcentagemPos)
		porcentagem2 = "{:.2f}".format(porcentagemNeg) 
		porcentagem3 = "{:.2f}".format(porcentagemNeu)
		app.setFont(12)
		app.setMessage("res", "Positivo: "+porcentagem1+"%, negativo: "+porcentagem2+"%, neutro: "+porcentagem3+".")
'''


