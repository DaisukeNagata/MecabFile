import re
import bs4
import sys
import MeCab
import urllib.request
from gensim.models import word2vec
import logging
import codecs

if len(sys.argv) == 2:
    url = sys.argv[1]
else:
    exit()

soup = bs4.BeautifulSoup(urllib.request.urlopen(url).read(),"html.parser")

title        = soup.title.string
description  = soup.find(attrs={"name":re.compile(r'Description',re.I)}).attrs['content']
h1           = soup.h1.string
contents     = title + description + h1
output_words = []


m = MeCab.Tagger()
result = m.parse(contents)


for i in result.split('\n'):
    word = i.split('\t')[0]
    base_path = "./"
    insert = base_path + "insert.txt"

    if word == 'EOS':
        break
    else:
        output_words.append(word)

    f = open(insert,"w")
    f.write(str(output_words))
    f.close()

with codecs.open('insert.txt', 'r') as f:
    
    text = f.read()
    tagger = MeCab.Tagger('-Owakati')
    wakati_text = tagger.parse(text)
    open('insert.txt', 'w').write(wakati_text)
    
    sentences = word2vec.Text8Corpus("insert.txt")
    model = word2vec.Word2Vec(sentences, size=100, min_count=1)


model.save("word2vec.gensim.model")

model = word2vec.Word2Vec.load("word2vec.gensim.model")
results = model.wv.most_similar(positive=['openCV'])

for result in results:
    print(result)
