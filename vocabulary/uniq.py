wordlist = []
worddict = {}

with open('./wl1duplic', 'r') as f:
  for w in f:
    w = w.strip().lower()
    if w not in worddict:
      wordlist.append(w)
      worddict[w] = 1



with open('./wl2uniq', 'w') as f:
  [f.write(w+'\n') for w in wordlist]