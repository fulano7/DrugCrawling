import codecs
import os
import pickle

from sklearn.pipeline import Pipeline

CLASSIFIED = "../classificados/"

def classify(path):
    count = 0
    f_debug = open("debug", "w+")
    c_file = codecs.open("../Classifier_NH.obj", "rb")
    c = pickle.load(c_file)
    for root, dir_names, file_names in os.walk(path):
        for file_name in file_names:
            if not os.path.isfile(path+file_name):
                continue
            count += 1
            f_debug.write(path+file_name+'\n')
            #pred = []
            text = ''
            doc = codecs.open(path+file_name, mode='r', encoding='utf-8')
            print(path+file_name)
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
    f_debug.close()
    print(str(count))

if not os.path.exists(CLASSIFIED):
	os.makedirs(CLASSIFIED)

#classify('../text/heuristic/drug/')
classify('../text/')

