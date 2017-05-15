import os
import numpy

from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import KFold
from sklearn.metrics import confusion_matrix, f1_score

# classes
DRUG = 'drug'
OTHER = 'other'

# classificar arquivos manualmente em 1 pasta de 
# pagina de medicamento e 1 pasta de nao-medicamento

# pastas com os arquivos separados manualmente
DIRS = [('text/drugs', DRUG), ('text/other', OTHER)]

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

# validacao (AINDA NAO TESTADO)
k_fold = KFold(n=len(data), n_folds=8)
scores = []
confusion = numpy.array([[0, 0], [0, 0]])
for train_indexes, test_indexes in k_fold:
    train_text = data.iloc[train_indexes]['text'].values
    train_y = data.iloc[train_indexes]['class'].values

    test_text = data.iloc[test_indexes]['text'].values
    test_y = data.iloc[test_indexes]['class'].values

    pipeline.fit(train_text, train_y)
    predictions = pipeline.predict(test_text)

    confusion += confusion_matrix(test_y, predictions)
    score = f1_score(test_y, predictions, pos_label=DRUG)
    scores.append(score)

#TODO: salvar o classificador

# melhorias = feature selection;
#             usar outros classif;
#             eliminar stopwords em pt-BR;
#             ajustar parametros dos classif...

