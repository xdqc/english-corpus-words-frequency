# english-corpus-words-frequency
Compare various English corpus by measuring differences between words frequency lists.

## Corpus

- [My Twitter Curpus](https://github.com/xdqc/tweet-trend-everyday) - `twit`

- [Norvig Natural Language Corpus](https://github.com/colinscape/norvig-frequencies/tree/master/data) - `norv`

- [Google's Ngram Corpus](https://github.com/hackerb9/gwordlist) - `ngra`

- [Wikipedia Frequency Lookup](https://github.com/prabhakar267/wikipedia-frequency-lookup) - `wiki`

- [Google 10000 English](https://github.com/first20hours/google-10000-english) - `goog`

- [Corpus of Contemporary American English](https://github.com/oyrx/word_frequency) - `coca`

- [Open Subtitle](http://opus.nlpl.eu/index.php) - `subt`

## Dictionary

- [Oxford](https://github.com/DevangMstryls/Oxford-English-Dictionary-41K-words-) `dict_oxford.txt`

- [Webster](https://github.com/matthewreagan/WebstersEnglishDictionary) `dict_webster.txt`

- [English words](https://github.com/dwyl/english-words) `dict_alpha.txt`


## How to compare corpus?

#### Similarity

**Similarity** of two corpus is depend on *percentage of common words* and *average word distance* in two corpus.

#### Word distance

**Distance** means how far away a word position of the frequency ranking in different corpus. Distance has sign (can be negative).

*distance* = *ln(indexofWordInSecondCorpus)* - *ln(indexofWordInFirstCorpus)*


#### Compare size

For fairness, two corpus should be compared with same size of N most common words. Typically, first 10000 common words covers 97% of entire corpus, first 20000 common words convers more than 99% of entire corpus.

#### Dictionary filter

Use dictionaries as masks to mitigate criteriary differences when generating these corpus.


## Comparison

### Results

one of the results using *all-dictionary mask* and *10000 compare size*.
![alt text](https://raw.githubusercontent.com/xdqc/english-corpus-words-frequency/master/results/t-all-10000.PNG "dictinary mask=dict_all, compare size=10000")

![alt text](https://raw.githubusercontent.com/xdqc/english-corpus-words-frequency/master/results/g-all-10000.PNG "dictinary mask=dict_all, compare size=10000")

`norv` and `ngra` have 99.9% words in common, and 100x similarity value to other corpus, thuns can be considered the same.

#### 
