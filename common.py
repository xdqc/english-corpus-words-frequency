dict_alpha = set()
words = []

with open('./dictionary/dict_all.txt', 'r') as f:
  for w in f:
    dict_alpha.add(w.strip())

with open('./corpus_original/coca_corpus.txt', 'r') as f:
  for w in f:
    w = w.split('\t')[0]
    words.append(w.strip())

for w in words:
  if w in dict_alpha:
    print(w)