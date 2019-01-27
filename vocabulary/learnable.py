unlearnble = set()
learnable = []

with open('./wl-unlearnable', 'r') as f:
  for l in f:
    for w in l.split(','):
      unlearnble.add(w.strip().lower())

with open('./wl3', 'r') as f:
  for w in f:
    w = w.strip().lower()
    if w not in unlearnble:
      learnable.append(w)

with open('./wl-leanable', 'a') as f:
  [f.write(w+'\n') for w in learnable]