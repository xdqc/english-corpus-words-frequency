from lemmatizer import lemmatize
from avalanche import i_stem
import re
import os
import math
import json

trans = json.load(
    open('../../corpus-roamer/src/assets/word_list_tran.json', 'r', encoding='utf8'))
words = {}
wl = []
with open('../../translation/classify/corpus_lemmatized.txt') as f:
  for w in f.readlines():
    wl.append(w.strip())


def add_text(filename):
  with open(filename, 'r', errors='ignore') as f:
    for l in f.readlines():
      for string in re.sub(r'[^A-Za-z]+', ' ', l).split():
        w = lemmatize(string.lower())
        if (w in trans and 'zh' in trans[w]):
          if w in words:
            words[w] += 1
          else:
            words[w] = 1


(add_text('./notre-dame.txt'))
# for dirname in os.listdir('./'):
#   if os.path.isdir('./'+dirname):
#     for filename in os.listdir('./'+dirname):
#       add_text('./' + dirname + '/'+filename)


got_vocab = []

for i, w in enumerate(wl, start=1):
  # compare the word rank in natural language and its count in WoW db dump
  if len(w) > 2 and w in words and 35 < math.log1p(words[w]) * math.log1p(i):
    got_vocab.append(tuple([w, words[w]/math.log2(i)]))

got_vocab = sorted(got_vocab, key=lambda x: x[1], reverse=True)

got_stem = {}
for w in got_vocab:
  stem = i_stem(w[0], True)
  if stem not in got_stem: 
    got_stem[stem] = []
  got_stem[stem].append(w[0])

for s in got_stem:
  print('{'+ f'"word":"{got_stem[s][0]}", "stem":"{s}"' + '},')


