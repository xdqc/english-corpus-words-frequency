import json

with open('./dictionary_alpha_arrays.json', 'r') as f:
  webster = json.load(f)
  for sublist in webster:
    for word in sublist:
      print(word)