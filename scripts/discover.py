corpus_dir = './corpus_f_n/'

twitter_words = []

with open(corpus_dir+'01_twitter.txt', 'r') as f:
    twitter_words.extend([w.strip() for i,w in enumerate(f) if i < 100000])

old_words = set()

old_files = [
    '02_norvig.txt',
    '04_google.txt',
    '03_wiki.txt',
    '05_coca.txt',
    '06_subtitle.txt'
]

for filename in old_files:
    with open(corpus_dir+filename) as f:
        for w in f:
            old_words.add(w.strip())

for i,w in enumerate(twitter_words):
    if w not in old_words:
        print(i, w, sep='\t')
