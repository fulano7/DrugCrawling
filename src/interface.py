#!/usr/bin/env python
# -*- coding: utf-8 -*-

#run with:
#FLASK_APP=interface.py flask run

from flask import Flask, flash, redirect, render_template, request, url_for, json
import json
import re
import editdistance
import heapq

# import process

app = Flask(__name__, template_folder='templates')
app.secret_key = 'some_secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    error = None
    if request.method == 'POST':
        
        produto = request.form['produto'].lower()
        farmacia = request.form['farmacia'].lower()
        price = request.form['price']

        queue = []

        results = []
        results.append('Query: ' + produto)
        with open('extraction/data.js') as json_data:
            objs = json.load(json_data)
            for obj in objs:
                if (produto.lower() in obj['sumario'].lower()):
                    results.append('Produto: ' + obj['produto'].decode('utf-8') + \
                    '<br>Farmacia: ' + obj['farmacia'] + '<br>Site: ' + obj['site'] + \
                    '<br>Preco: ' + obj['price'] + '<br>')
                for word in obj['produto'].split(' '):
                    word = word.lower()
                    produto = produto.lower()
                    ed = editdistance.eval(word, produto)
                    heapq.heappush(queue, (ed, word))

        word1 = str(heapq.heappop(queue)[1])
        while(word1 == produto):
            word1 = str(heapq.heappop(queue)[1])
        word2 = str(heapq.heappop(queue)[1])
        while(word2 == word1):
            word2 = str(heapq.heappop(queue)[1])
        word3 = str(heapq.heappop(queue)[1])
        while(word3 == word2 or word3 == word1):
            word3 = str(heapq.heappop(queue)[1])

        results.append("Palavras com maior mutual information: " + word1 + ", " + word2 + ", " + word3)
            
        return render_template('display.html', results = results)

    return render_template('search.html', error=error)

# @app.route("/")
# def hello():
#     return "Hello World!"

# @app.route('/search', methods=['GET', 'POST'])
# def search():
#     if request.method == "POST":
#         with open('extraction/data.js') as json_data:
#             objs = json.load(json_data)
#             return render_template('results.html', records=objs[0])
#     return render_template('search.html')
