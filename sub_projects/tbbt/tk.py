from nltk.tokenize import word_tokenize
from lemmatizer import lemmatize
import re
import os
import math
import json

trans = json.load(open('../../corpus-roamer/src/assets/word_list_tran.json', 'r', encoding='utf8'))
words = {}
wl = []
with open('../../translation/classify/corpus_lemmatized.txt') as f:
  for w in f.readlines():
    wl.append(w.strip())


with open('./tbbt.txt') as f:
  for l in f.readlines():
    w = lemmatize(l.split()[0])
    wc = int(l.split()[1])
    if (w in trans and 'zh' in trans[w]):
      if w in words:
        words[w] += wc
      else:
        words[w] = wc


wow_vocab = []

for i, w in enumerate(wl, start=1):
  # compare the word rank in natural language and its count in WoW db dump
  if len(w) > 2 and w in words and i > 1000 and 20 < math.log1p(words[w]) * math.log1p(i):
    wow_vocab.append(tuple([w, i, words[w]/math.log2(i)]))

wow_vocab = sorted(wow_vocab, key=lambda x: x[2], reverse=True)

for w in wow_vocab:
  print(w[1], w[0], words[w[0]])
