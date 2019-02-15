import os
import json
import re

# dict_alpha = set()

# with open('./dictionary/dict_webster.txt', 'r') as f:
#   for w in f:
#     dict_alpha.add(w.strip())

# corpus_dir = './corpus_f_n/'
# output_dir = './corpus_f_webster/'

# files = os.listdir(corpus_dir)

# for filename in files:
#   words = []
#   with open(corpus_dir+filename, 'r') as f:
#     for w in f:
#       w = w.strip()
#       if w in dict_alpha:
#         words.append(w)

#   with open(output_dir+filename, 'w') as f:
#     for w in words:
#       f.write(w+'\n')


webster = {}

with open('./dictionary/dictionary_alpha_arrays.json', 'r') as f:
    jsonfile = json.load(f)
    for subdict in jsonfile:
        webster = dict(webster, **subdict)

for k in webster:
    webster[k.replace(r'[\-\,\/ \d\.\']', '').lower()] = webster[k]

oxford = {}

with open('./dictionary/oxford.txt', 'r', encoding='utf8') as f:
    for line in f:
        w = str(line).split('\t')[0].replace(r'[\-,/ \d\.\']', '').lower()
        if w in oxford:
            oxford[w] += '        ' + line.split('\t')[1].strip()
        else:
            oxford[w] = line.split('\t')[1].strip()


with open('./new_corpus', 'r') as f:
    with open('./word_corpus', 'w', encoding='utf8') as target:
        corpus = set()
        for w in f:
            w = w.strip()
            corpus.add(w)

        for w in oxford:
            if w not in corpus:
                target.write(w + '\t' + oxford[w] + '\n')

            # elif w in webster:
            #     target.write(
            #         w + '\t' + str(webster[w]).replace('\n', '        ') + '\n')
