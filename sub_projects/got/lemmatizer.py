
from nltk.stem import WordNetLemmatizer
import re

def lemmatize(w: str):
  """
  Improved lemmatizer based on nltk.stem.WordNetLemmatizer
  """
  if w in {'as', 'us', 'ms', 'mrs', 
           'vs', 'cos', 'wis', 'mis', 'gus',
           'des', 'les', 'las', 'pas', 'der', 'es', 'est',
           'during', 'feed', 'mater', 
           'ground', 'clad', 'unclad', 'infrared',
           'viking', 'thames', 'kansas', 'alps',
           'james', 'ellis', 'elias',
           'ss', 'os', 'hs', 'ps', 'cs', 'rs', 'bs', 'ds', 'fs', 'gs',
           'js', 'ks', 'ls', 'ns', 'qs', 'rs', 'ts', 'xs', 'ys', 'zs',
           'lest', 'lester', 'kester', 'vester', 'mester',
           'kest', 'cest', 'cester', 'dester'}:
    return w

  if w in {'bees', 'axes', 'vikings'}:
    return w[:-1]

  if w in {'halves', 'calves', 'thieves'}:
    return w[:-3] + 'f'

  if w in {'wives'}:
    return w[:-3] + 'fe'

  """ match open syllables 'consonant + vowel + consonant + e' """
  match_op = re.match(
      r'^([pbtdfvlmnghkczrwsx]{1,3})([aiou])([pbtdfvlmnghkczr])(es|ed|ing|ings)$', w)
  if match_op:
    return f'{match_op[1]}{match_op[2]}{match_op[3]}e'

  """ match ending 'ss' """
  match_ss = re.match(r'^([a-z]*)([aeiouy])(ss)(es|ed|er|ing)?s?$', w)
  if match_ss:
    stub = f'{match_ss[1]}{match_ss[2]}{match_ss[3]}'
    return re.sub(r'focuss$', 'focus', stub, 1)

  wnl = WordNetLemmatizer()
  stub = wnl.lemmatize(w,    pos='r')  # ADV
  stub = wnl.lemmatize(stub, pos='a')  # ADJ
  stub = wnl.lemmatize(stub, pos='v')  # VERB
  stub = wnl.lemmatize(stub, pos='n')  # NOUN
  return stub
