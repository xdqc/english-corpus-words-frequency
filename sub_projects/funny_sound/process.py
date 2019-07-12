funny = {}
corpus = []
rank_funny = []

with open('../../translation/classify/corpus_complete_rank.txt', 'r') as f:
  for l in f:
    corpus.append(l.strip())

with open('./raw.txt', 'r') as f:
  f = list(f)
  for i, l in enumerate(f):
    if i % 2 == 0:
      word = l.strip()
      meaning = f[i+1].strip()
      funny[word] = meaning

for w in corpus:
  if w in funny:
    rank_funny.append(tuple([w, funny[w]]))
    print('{' + f'"word": "{w}", "value": "{funny[w]}"'+'}')
    funny[w] = ''

print()

for w in funny:
  if funny[w]:
    print('{' + f'"word": "{w}", "value": "{funny[w]}"'+'}')
