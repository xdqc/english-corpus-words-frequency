dict_alpha = set()
words = []

with open('./dict_webster.txt', 'r') as f:
  for w in f:
    dict_alpha.add(w.strip())

with open('./words_subtitle_', 'r') as f:
  for w in f:
    words.append(w.strip())

for w in words:
  if w in dict_alpha:
    print(w)