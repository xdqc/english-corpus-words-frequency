import re
import bisect


def create_sorted_calibrated_corpus(filename):
  with open(filename, 'r') as f:
    total = 0
    rate = 10000000000/759851496655
    for i, line in enumerate(f, start=1):
      line = line.strip().split('\t')
      word = line[0]
      count = round(int(line[1]))
      total += count
      print(word, total, sep='\t')
      # if total > 759841118555 * .9999:
      #   print(i, word, count, total)
      #   break
    # print(total)


def digits_to_word(digits, breakpoints, wordlist):
  i = bisect.bisect(breakpoints, digits)
  return wordlist[i]


def make_breakpoints_and_list(filename):
  accu, wl = [], []
  with open(filename, 'r') as f:
    for line in f:
      line = line.strip().split()
      accu.append(int(line[1]))
      wl.append(line[0])
  return accu, wl


def generate_pi_words(in_corpus_acc, outfile='./pi-english-words.txt'):
  start = 2
  bound = 10000000
  step = 10
  accu, wl = make_breakpoints_and_list(in_corpus_acc)

  with open('./pi-billion.txt', 'r') as f:
    pi_billion = f.readline()
    with open(outfile, 'w') as of:
      for i in range(start, start+bound, step):
        digits = int(pi_billion[i:i+step])
        of.write(digits_to_word(digits, accu, wl)+' ')


generate_pi_words('./ngram_accumulated_99.txt', './pi-english-words_use.99_176k.txt')

# create_sorted_calibrated_corpus('./ngram_sort.txt')
