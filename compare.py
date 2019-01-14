import os, collections, math

def make_order(filename):
  words = {}
  index = 0
  with open(filename) as f:
    for line in f:
      index += 1
      words[line.strip()] = math.log(index)
      if index >= 10000:
        break
  return words

down_words = make_order('./words_subtitle')
up_words = make_order('./words_google')

diff = {}

for word in down_words:
  if word in up_words:
    diff[word] = down_words[word] - up_words[word]
  else:
    diff[word] = -math.log(len(up_words)) - (math.log(len(down_words)) - down_words[word])

for word in up_words:
  if word not in down_words:
    diff[word] = math.log(len(down_words)) + (math.log(len(up_words)) - up_words[word])

for word in sorted(diff.items(), key=lambda kv: kv[1], reverse=True):
  print(word[0], word[1], sep='\t')




