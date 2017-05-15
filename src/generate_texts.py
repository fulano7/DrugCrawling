import os
import codecs
import html2text

TEXT = '../text/'
HTML_NH = '../html/no heuristic/'

def convert(path):
	counter = 0
	for root, dir_names, file_names in os.walk(path):
		total = len(file_names)
		for file_name in file_names:
			counter+= 1
			print('Converting file #'+ str(counter) +' of '+str(total)+'...')
			html = codecs.open(path+file_name, encoding='utf-8')
			html = html.read()
			#atencao com w+
			text = codecs.open(TEXT+file_name+'.txt', mode='w+', encoding='utf-8')
			text.write(html2text.html2text(html))
			text.close()

if not os.path.exists(TEXT):
	os.makedirs(TEXT)

convert(HTML_NH)

