import json

with open('./coca_corpus.json', 'r') as f:
  data = json.load(f)
  for word in data:
    print(word)