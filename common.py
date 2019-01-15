import os

dict_alpha = set()

with open('./dictionary/dict_oxford.txt', 'r') as f:
  for w in f:
    dict_alpha.add(w.strip())

corpus_dir = './corpus_f_n/'
output_dir = './corpus_f_oxford/'

files = os.listdir(corpus_dir)

for filename in files:
  words = []
  with open(corpus_dir+filename, 'r') as f:
    for w in f:
      w = w.strip()
      if w in dict_alpha:
        words.append(w)

  with open(output_dir+filename, 'w') as f:
    for w in words:
      f.write(w+'\n')

