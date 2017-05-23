import os

#change opt according to what you want
CRWOPT = 1; 

if (CRWOPT == 1):
    os.system('python src/generic_crawler.py')
elif (CRWOPT == 2):
    os.system('python src/heuristic_crawler.py')

#running classifier
os.system('python src/build_classifier.py')
os.system('python src/classify.py')

#running extractor
os.system('python src/wrapper.py')