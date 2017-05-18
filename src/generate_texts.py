import os
import re
import codecs
import html2text

TEXT = '../text/'
HTML_NH = '../html/no heuristic/'
HTML_H = '../html/heuristic/'

def convert(path):
	counter = 0
    # da match com sintaxe markdown
	regex = re.compile(r"[\{\}\[\]\(\)_\*#!]+", flags=re.MULTILINE)
    # da match com urls
	regex2 = re.compile(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)", flags=re.MULTILINE)
	h2t = html2text.HTML2Text()
	h2t.ignore_links = True
	h2t.ignore_images = True
	for root, dir_names, file_names in os.walk(path):
		total = len(file_names)
		for file_name in file_names:
			counter+= 1
			print('Converting file #'+ str(counter) +' of '+str(total)+'...')
			html = codecs.open(path+file_name, encoding='utf-8')
			html = html.read()
			#atencao com w+
			text = codecs.open(TEXT+file_name+'.txt', mode='w+', encoding='utf-8')
			text2 = h2t.handle(html)
			text2 = regex.sub("", text2)
			text2 = regex2.sub("", text2)
			text.write(text2)
			text.close()

if not os.path.exists(TEXT):
	os.makedirs(TEXT)

# convert(HTML_NH) - ja separado manualmente
# convert(HTML_H) - ja separado manualmente

