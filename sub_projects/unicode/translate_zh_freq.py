import json
import re


def pin2yin(numbered: str):
  pinyin_table = {
      'ang1': 'āng',
      'ang2': 'áng',
      'ang3': 'ǎng',
      'ang4': 'àng',
      'eng1': 'ēng',
      'eng2': 'éng',
      'eng3': 'ěng',
      'eng4': 'èng',
      'ing1': 'īng',
      'ing2': 'íng',
      'ing3': 'ǐng',
      'ing4': 'ìng',
      'ong1': 'ōng',
      'ong2': 'óng',
      'ong3': 'ǒng',
      'ong4': 'òng',
      'ung1': 'ūng',
      'ung2': 'úng',
      'ung3': 'ǔng',
      'ung4': 'ùng',
      'vng1': 'ǖng',
      'vng2': 'ǘng',
      'vng3': 'ǚng',
      'vng4': 'ǜng',
      'an1': 'ān',
      'an2': 'án',
      'an3': 'ǎn',
      'an4': 'àn',
      'en1': 'ēn',
      'en2': 'én',
      'en3': 'ěn',
      'en4': 'èn',
      'in1': 'īn',
      'in2': 'ín',
      'in3': 'ǐn',
      'in4': 'ìn',
      'on1': 'ōn',
      'on2': 'ón',
      'on3': 'ǒn',
      'on4': 'òn',
      'un1': 'ūn',
      'un2': 'ún',
      'un3': 'ǔn',
      'un4': 'ùn',
      'vn1': 'ǖn',
      'vn2': 'ǘn',
      'vn3': 'ǚn',
      'vn4': 'ǜn',
      'ai1': 'āi',
      'ai2': 'ái',
      'ai3': 'ǎi',
      'ai4': 'ài',
      'ao1': 'āo',
      'ao2': 'áo',
      'ao3': 'ǎo',
      'ao4': 'ào',
      'er1': 'ēr',
      'er2': 'ér',
      'er3': 'ěr',
      'er4': 'èr',
      'ei1': 'ēi',
      'ei2': 'éi',
      'ei3': 'ěi',
      'ei4': 'èi',
      'ou1': 'ōu',
      'ou2': 'óu',
      'ou3': 'ǒu',
      'ou4': 'òu',
      'a1': 'ā',
      'a2': 'á',
      'a3': 'ǎ',
      'a4': 'à',
      'e1': 'ē',
      'e2': 'é',
      'e3': 'ě',
      'e4': 'è',
      'i1': 'ī',
      'i2': 'í',
      'i3': 'ǐ',
      'i4': 'ì',
      'o1': 'ō',
      'o2': 'ó',
      'o3': 'ǒ',
      'o4': 'ò',
      'u1': 'ū',
      'u2': 'ú',
      'u3': 'ǔ',
      'u4': 'ù',
      'v1': 'ǖ',
      'v2': 'ǘ',
      'v3': 'ǚ',
      'v4': 'ǜ',
  }
  converted = ''

  npinyins = numbered.split('/')
  for npinyin in npinyins:
    for p in pinyin_table:
      if npinyin.endswith(p):
        npinyin = npinyin.replace(p, pinyin_table[p])
        break
    converted += npinyin + '/'

  return converted.strip('/')


zh = []

with open('./zh_freq.txt') as f:
  for l in f:
    word = l.split()[1]
    tone = l.split()[4] if len(l.split()) > 4 else ''
    tone = pin2yin(tone)
    zh.append(tuple([word, tone]))

cjk = {}
with open('./CJK.json') as j:
  for i in json.load(j):
    cjk[i['char']] = i['tran']


zh_trans = []

for word in zh:
  if word[0] in cjk:
    print(
        '{' + f'"word": "{word[0]}", "tone":"{word[1]}", "value": "{cjk[word[0]]}"'+'},')
