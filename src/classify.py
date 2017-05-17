import codecs
import os
import pickle

from sklearn.pipeline import Pipeline

CLASSIFIED = "../classificados/"

def classify(path):
    c_file = codecs.open("../Classifier_NH.obj", "rb")
    c = pickle.load(c_file)
    for root, dir_names, file_names in os.walk(path):
        for file_name in file_names:
            #pred = []
            text = ''
            doc = codecs.open(root+file_name, mode='r', encoding='utf-8')
            for line in doc:
                text += (line)
            pred = [text]
            h = c.predict(pred)
            print(h[0])
            if h[0] == 'drug':
                original_doc = codecs.open(("../html/heuristic/")+(file_name[:((file_name).rfind('.'))]), mode='r', encoding='utf-8')
                text2 = ''
                for line2 in original_doc:
                    text2 += line2
                doc2 = codecs.open(CLASSIFIED+(file_name[:((file_name).rfind('.'))]), mode="w+", encoding='utf-8')
                doc2.write(text2)            
                doc2.close()
            doc.close()
    c_file.close()

if not os.path.exists(CLASSIFIED):
	os.makedirs(CLASSIFIED)

classify('../text/heuristic/drug/')
classify('../text/heuristic/other/')

