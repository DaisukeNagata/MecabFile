import re
import bs4
import sys
import MeCab
import urllib.request
from gensim.models import word2vec

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
    insert = base_path + "insert.html"

    if word == 'EOS':
        break
    else:
        output_words.append(word)

    f = open(insert,"w")
    f.write('<meta http-equiv="content-type" charset="utf-8">' + str(output_words))
    f.close()

model = word2vec.Word2Vec(output_words,
                          size=100,
                          min_count=5,
                          window=5,
                          iter=5)

print(model)

model.save("word2vec.gensim.model")
