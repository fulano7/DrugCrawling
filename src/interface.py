#!/usr/bin/env python
# -*- coding: utf-8 -*-

#run with:
#FLASK_APP=interface.py flask run

from flask import Flask, flash, redirect, render_template, request, url_for, json
import json
import re

app = Flask(__name__, template_folder='templates')
app.secret_key = 'some_secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    error = None
    if request.method == 'POST':
        query = request.form['query']

        #todo: usar parte de Iago aqui para gerar os results[]

        #this is temporary:
        results = []
        results.append('Query: ' + query + '<br>')
        with open('extraction/data.js') as json_data:
            objs = json.load(json_data)
            for obj in objs:
                if (query.lower() in obj['sumario'].lower()):
                    results.append('Produto: ' + obj['produto'].decode('utf-8') + \
                    '<br>Farmacia: ' + obj['farmacia'] + '<br>Site: ' + obj['site'] + \
                    '<br>Preco: ' + obj['price'] + '<br>')
        ##################
            
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
