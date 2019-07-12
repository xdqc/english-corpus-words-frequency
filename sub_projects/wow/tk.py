from nltk.tokenize import word_tokenize
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


def camel_split(string):
  s1 = re.sub(r'(.)([A-Z][a-z]+)', r'\1 \2', string)
  return re.sub(r'([a-z])([A-Z])', r'\1 \2', s1).lower()


def add_text(filename):
  with open(filename) as f:
    for l in f.readlines():
      for string in re.sub(r'[^A-Za-z]+', ' ', l).split():
        for w in camel_split(string).split():
        # w = string.lower()
          if (w in trans and 'zh' in trans[w]):
            if w in words:
              words[w] += 1
            else:
                words[w] = 1


# (add_text('./text-slang.txt'))
(add_text('./text-spell.txt'))
for filename in os.listdir('./db-dump'):
  add_text('./db-dump/'+filename)


wow_vocab = []

for i, w in enumerate(wl, start=1):
  # compare the word rank in natural language and its count in WoW db dump
  if len(w) > 2 and w in words and 40 < math.log1p(words[w]) * math.log1p(i):
    wow_vocab.append(tuple([w, words[w]/math.log2(i)]))

wow_vocab = sorted(wow_vocab, key=lambda x: x[1], reverse=True)

for w in wow_vocab:
  print(w[0])
