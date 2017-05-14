import os
import numpy

from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# classes
DRUG = 'drug'
OTHER = 'other'

# classificar arquivos manualmente em 1 pasta de 
# pagina de medicamento e 1 pasta de nao-medicamento

#TODO: colocar as pastas
DIRS = []

#TODO: leitura de arquivos de uma pasta
def read_files(path):
	pass

# gerando dataframe para uma pasta
def generate_dataframe(path, label):
	rows = []
	index = []
	for file_name, text in read_files(path):
		rows.append({'text': text, 'class': label})
		index.append(file_name)
	df = DataFrame(rows, index=index)
	return df

# leitura de todos os arquivos
data = DataFrame({'text': [], 'class': []})
for path, label in DIRS:
	data = data.append(generate_dataframe(path, label))

# embaralhando os documentos
data = data.reindex(numpy.random.permutation(data.index))

# extraindo features e classificando com naive bayes
pipeline = Pipeline([ ('vectorizer', CountVectorizer()) , ('classifier', MultinomialNB()) ])
pipeline.fit(data['text'].values, data['class'].values)

#TODO: validacao

#TODO: salvar o classificador

# melhorias = usar outros classif;
#             eliminar stopwords em pt-BR;
#             ajustar parametros dos classif...

