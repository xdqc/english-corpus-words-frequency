import os
import math

corpus_dir = './corpus_f_n/'

factors = [
    7,
    10,
    1,
    1,
    4,
    1
]

output = {}

for index, filename in enumerate(os.listdir(corpus_dir)):
    with open(corpus_dir+filename, 'r') as f:
        for i, w in enumerate(f, start=2):
            w = w.strip()
            if w in output:
                output[w] += factors[index] / math.log(i)
            else:
                output[w] = factors[index] / math.log(i)
            if i > 200000:
                break

output = sorted(output.items(), key=lambda kv: kv[1], reverse=True)

[print(w[0]) for w in output]
