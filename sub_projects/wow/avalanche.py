from nltk.stem import SnowballStemmer
import re

overrides_defensive = {
    # defensive
    'calligraph': 'calligraph',    # ~call
    'importan': 'importan',        # ~import
    'importun': 'importun',        # ~import
    'incred': 'incred',            # ~incr
    'informal': 'informal',        # ~inform
    'inferior': 'inferior',        # ~infer
    'interes': 'interes',          # ~inter
    'interpr': 'interpr',          # ~interp
    'internal': 'internal',        # ~intern
    'internat': 'internat',        # ~intern
    'represen': 'represent',       # ~repr
    'persua': 'persua',            # ~per
    'politic': 'politic',          # ~polit
    'true': 'true',                # ~true
    'trust': 'true',               # ~trust
    # remidiate
    'astrin': 'astrin',            # ~astr
    'artif': 'artif',              # ~art
    'communic': 'communic',        # ~commun
    'complain': 'complain',        # ~compl
    'compla': 'compla',            # ~compl
    'comply': 'comply',            # ~compl
    'complia': 'comply',           # ~compl
    'complex': 'complic',          # ~compl
    'complic': 'complic',          # ~compl
    'contempor': 'contempor',      # ~contemp
    'continent': 'continent',      # ~contin
    'contract': 'contract',        # ~contra
    'carous': 'carous',            # ~care
    'expectora': 'expectorat',     # ~expect
    'explic': 'explic',            # ~expl
    'imperi': 'imperi',            # ~imper
    'impera': 'imperi',            # ~imper
    'improvis': 'improvis',        # ~improv
    'incomplet': 'incomplet',      # ~income
    'labo': 'lab',                 # ~mar
    'marin': 'marin',              # ~mar
    'magnif': 'magnif',            # ~magn
    'manif': 'manif',              # ~man
    'perform': 'perform',          # ~perfor
    'preced': 'preced',            # ~prec
    'provis': 'provis',            # ~prov
    'signif': 'signif',            # ~sign
    'specif': 'specif',            # ~spec
    'soldier': 'soldier',          # ~sold
    'transport': 'transport',      # ~transp
    'transform': 'transform',      # ~transf
    'understand': 'understand',    # ~stand
}


startwith_3 = {
    'axe',
    'bag',
    'dew',
    'duo',
    'egg',
    'ego',
    'fly',
    'god',
    'gun',
    'ice',
    'pay',
    'six',
    'tip',
    'urs',
    'use',
    'vex',
    'wet',
}
startwith_4 = {
    'acid',
    'alim',
    'anil',
    'anim',
    'back',
    'bapt',
    'base',
    'bath',
    'benz',
    'blue',
    'book',
    'bulb',
    'camp',
    'carb',
    'cask',
    'chem',
    'clap',
    'coit',
    'cosm',
    'cyan',
    'damp',
    'dodg',
    'door',
    'dram',
    'drip',
    'dump',
    'face',
    'fair',
    'fire',
    'friz',
    'full',
    'fung',
    'gear',
    'gold',
    'good',
    'grit',
    'hair',
    'half',
    'hand',
    'hard',
    'hawk',
    'heir',
    'help',
    'high',
    'iron',
    'isol',
    'jasm',
    'just',
    'kick',
    'kill',
    'king',
    'know',
    'lact',
    'last',
    'lazu',
    'like',
    'line',
    'live',
    'long',
    'look',
    'love',
    'luck',
    'milk',
    'mind',
    'move',
    'name',
    'nitr',
    'octo',
    'open',
    'parl',
    'phon',
    'pick',
    'pict',
    'play',
    'prim',
    'rain',
    'rock',
    'roll',
    'roof',
    'room',
    'rupt',
    'saff',
    'serv',
    'shoe',
    'shot',
    'side',
    'size',
    'slow',
    'snow',
    'spac',
    'stay',
    'step',
    'stud',
    'sure',
    'swim',
    'tank',
    'time',
    'topo',
    'town',
    'tumo',
    'turn',
    'tute',
    'valu',
    'wait',
    'wear',
    'west',
    'wild',
    'work',
}
startwith_5 = {
    'admin',
    'apart',
    'avail',
    'aviat',
    'belie',
    'birth',
    'blood',
    'board',
    'brain',
    'break',
    'catch',
    'check',
    'chick',
    'civil',
    'clear',
    'close',
    'cloth',
    'coast',
    'colon',
    'color',
    'comed',
    'court',
    'creat',
    'crock',
    'cross',
    'crypt',
    'doubl',
    'dream',
    'eagle',
    'educa',
    'energ',
    'exult',
    'feder',
    'field',
    'figur',
    'force',
    'found',
    'futur',
    'grand',
    'green',
    'guard',
    'habit',
    'heart',
    'homeo',
    'house',
    'human',
    'inher',
    'labor',
    'large',
    'learn',
    'liais',
    'light',
    'maint',
    'manag',
    'medic',
    'middl',
    'music',
    'natur',
    'night',
    'north',
    'novel',
    'obtru',
    'offer',
    'offic',
    'order',
    'organ',
    'paint',
    'photo',
    'pious',
    'plant',
    'point',
    'power',
    'press',
    'psych',
    'quadr',
    'quest',
    'regul',
    'reich',
    'round',
    'scien',
    'score',
    'sheep',
    'shirt',
    'short',
    'south',
    'sound',
    'speak',
    'sport',
    'steep',
    'still',
    'store',
    'stren',
    'synth',
    'techn',
    'think',
    'thoro',
    'topic',
    'total',
    'train',
    'varan',
    'visit',
    'water',
    'where',
    'white',
    'woman',
    'world',
}
startwith_6 = {
    'action',
    'author',
    'breast',
    'cataly',
    'chance',
    'change',
    'christ',
    'church',
    'common',
    'consid',
    'curcum',
    'democr',
    'factor',
    'fanfar',
    'ground',
    'health',
    'hospit',
    'ingrat',
    'length',
    'market',
    'moment',
    'mother',
    'number',
    'person',
    'planet',
    'privat',
    'record',
    'respon',
    'school',
    'season',
    'second',
    'spectr',
    'spider',
    'spirit',
    'system',
    'tradit',
    'travel',
    'weight',
    'window',
    'yellow',
}
startwith_7 = {
    'brother',
    'collect',
    'conceiv',
    'command',
    'current',
    'element',
    'respect',
    'process',
    'station',
    'support',
}


def stem(w: str, aggressive=False):
  ss = SnowballStemmer('english')
  s = w.lower()

  # Remove prefix
  if aggressive:
    s = re.sub(r'^(back)([a-z]{3,})$', r'\2', s, 1)
    s = re.sub(r'^(counter)([a-z]{3,})$', r'\2', s, 1)
    s = re.sub(r'^(dis)([^ctpms][a-z]{2,})$', r'\2', s, 1)
    s = re.sub(r'^(down)([a-z]{3,})$', r'\2', s, 1)
    s = re.sub(r'^(en)([lfhjnps][a-z]{3,})$', r'\2', s, 1)
    s = re.sub(r'^(im)(per[^aeiou][a-z]{2,})$', r'\2', s, 1)
    s = re.sub(r'^(im)(p[ao](ss|st|t|l|v)[a-z]{2,})$', r'\2', s, 1)
    s = re.sub(r'^(inter)([^einv][a-z]{2,})$', r'\2', s, 1)
    s = re.sub(r'^(in)([abeiloprw][a-z]{2,})$', r'\2', s, 1)
    s = re.sub(r'^(male)([^a][a-z]{3,})$', r'\2', s, 1)
    s = re.sub(r'^(mis)([^est][a-z]{3,})$', r'\2', s, 1)
    s = re.sub(r'^(multi)([^pt][a-z]{3,})$', r'\2', s, 1)
    s = re.sub(r'^(omni)([a-z]{3,})$', r'\2', s, 1)
    s = re.sub(r'^(out)([a-z]{3,})$', r'\2', s, 1)
    s = re.sub(r'^(post)([ghnpsw][a-z]{2,})$', r'\2', s, 1)
    s = re.sub(r'^(pre)([behjmnor][a-z]{2,})$', r'\2', s, 1)
    s = re.sub(r'^(over)([a-z]{3,})$', r'\2', s, 1)
    s = re.sub(r'^(re)([iou][a-z]{3,})$', r'\2', s, 1)
    s = re.sub(r'^(side)([a-z]{4,})$', r'\2', s, 1)
    s = re.sub(r'^(sub)([^jsl][a-z]{3,})$', r'\2', s, 1)
    s = re.sub(r'^(trans)([^cgimpvl][a-z]{2,})$', r'\2', s, 1)
    s = re.sub(r'^(up)([^p][a-z]{3,})$', r'\2', s, 1)
    if (not s.startswith('understand')):
      s = re.sub(r'^(under)([a-z]{3,})$', r'\2', s, 1)
      s = re.sub(r'^(un)([^i][a-z]{3,})$', r'\2', s, 1)

  for overide in overrides_defensive:
    if s.startswith(overide):
      return overrides_defensive[overide]

  if aggressive:
    if s[:7] in startwith_7:
      return s[:7]
    if s[:6] in startwith_6:
      return s[:6]
    if s[:5] in startwith_5:
      return s[:5]
    if s[:4] in startwith_4:
      return s[:4]
    if s[:3] in startwith_3:
      return s[:3]

    # startwith stem
    s = re.sub(r'^(aqu)([ae]|if)[a-z]+$', r'\1', s, 1)
    s = re.sub(r'^(ast)e?ro[a-z]+$', r'\1r', s, 1)
    s = re.sub(r'^(audi)[oeb][a-z]+$', r'\1', s, 1)
    s = re.sub(r'^(bed)[^aeiou][a-z]+$', r'\1', s, 1)
    s = re.sub(r'^(calc)[^u][a-z]+$', r'\1', s, 1)
    s = re.sub(r'^(cardi)[aon][a-z]+$', r'\1i', s, 1)
    s = re.sub(r'^(cave)[^aoun][a-z]*$', r'\1', s, 1)
    s = re.sub(r'^(chart)[^r][a-z]+$', r'\1', s, 1)
    s = re.sub(r'^(chin)[ae][a-z]*$', r'\1a', s, 1)
    s = re.sub(r'^(class)(ic|y)[a-z]*$', r'\1c', s, 1)
    s = re.sub(r'^(cult)[^er][a-z]+$', r'\1', s, 1)
    s = re.sub(r'^(cycl)[^a][a-z]+$', r'\1', s, 1)
    s = re.sub(r'^(dat)[au][a-z]*$', r'\1a', s, 1)
    s = re.sub(r'^(dan)[cs][^ky][a-z]*$', r'\1c', s, 1)
    s = re.sub(r'^(din)[en][a-z]+$', r'\1e', s, 1)
    s = re.sub(r'^(dog)[^m][a-z]+$', r'\1', s, 1)
    s = re.sub(r'^(eas)[eiy][a-z]+$', r'\1', s, 1)
    s = re.sub(r'^(geni)[eou][a-z]+$', r'\1', s, 1)
    s = re.sub(r'^(per)?(hap)[pls][a-z]*$', r'\2', s, 1)
    s = re.sub(r'^a?(head)[a-z]*$', r'\1', s, 1)
    s = re.sub(r'^(home)[^o][a-z]+$', r'\1', s, 1)
    s = re.sub(r'^(hydr[ao])[a-z]+$', r'\1', s, 1)
    s = re.sub(r'^(hung)[re][a-z]+$', r'\1r', s, 1)
    s = re.sub(r'^(impl)(ic|id|y)[a-z]*$', r'\1c', s, 1)
    s = re.sub(r'^(implo)[sd][a-z]+$', r'\1d', s, 1)
    s = re.sub(r'^(jur)[iyo][a-z]+$', r'\1i', s, 1)
    s = re.sub(r'^(lamp)[^aeour][a-z]+$', r'\1', s, 1)
    s = re.sub(r'^(law)[^rn][a-z]+$', r'\1', s, 1)
    s = re.sub(r'^(meth)[ay][a-z]+$', r'\1', s, 1)
    s = re.sub(r'^(main)[^t][a-z]+$', r'\1', s, 1)
    s = re.sub(r'^(mark)[^e][a-z]+$', r'\1', s, 1)
    s = re.sub(r'^(oat)[^h][a-z]*$', r'\1', s, 1)
    s = re.sub(r'^(ox)(i|yg|ya)[a-z]+$', r'\1i', s, 1)
    s = re.sub(r'^(real)[^l][a-z]+$', r'\1', s, 1)
    s = re.sub(r'^(rect)[^o][a-z]+$', r'\1', s, 1)
    s = re.sub(r'^(rever)[iey][a-z]*$', r'\1r', s, 1)
    s = re.sub(r'^(sex)[^at][a-z]*$', r'\1', s, 1)
    s = re.sub(r'^(show)[^e][a-z]*$', r'\1', s, 1)
    s = re.sub(r'^(statu)[^ts][a-z]*$', r'\1s', s, 1)
    s = re.sub(r'^(test)[ie][cs][a-z]*$', r'\1c', s, 1)
    s = re.sub(r'^(top)[^aioph][a-z]+$', r'\1', s, 1)
    s = re.sub(r'^(tru)(e|st)[a-z]*$', r'\1e', s, 1)
    s = re.sub(r'^(uni)[tf][eiy][a-z]+$', r'\1', s, 1)
    s = re.sub(r'^(viv)[^e][a-z]+$', r'\1', s, 1)
    s = re.sub(r'^(wind)[^o][a-z]+$', r'\1', s, 1)
    s = re.sub(r'^(writ)[^h][a-z]+$', r'\1', s, 1)
    # s = re.sub(r'^(tele[^o])[a-z]+$', r'\1', s, 1)
    if s != w:
      return s

  if len(s) > 6:
    s = re.sub(r'[rfmz]$', 'i', s, 1)
    s = re.sub(r'[^ao]l$', 'i', s, 1)
    s = re.sub(r'a[ct]$', 'i', s, 1)
    s = re.sub(r'^([^cprst][a-z]+i)[ct]$', r'\1', s, 1)
  if len(s) > 7:
    s = re.sub(r'n$', 'i', s, 1)
    s = re.sub(r't$', 'i', s, 1)
    s = re.sub(r'[^eui]c$', 'i', s, 1)
    s = re.sub(r'ive$', 'i', s, 1)
    s = re.sub(r'ily$', 'i', s, 1)
    s = re.sub(r'ist$', 'i', s, 1)
    s = re.sub(r'[aeo]ry$', 'i', s, 1)
    # s = re.sub(r'ment$', '', s, 1)
  if len(s) > 7 and aggressive:
    s = re.sub(r'air$', '', s, 1)
    s = re.sub(r'ship$', '', s, 1)
    s = re.sub(r'shop$', '', s, 1)
    s = re.sub(r'gram$', '', s, 1)
    s = re.sub(r'less$', '', s, 1)
    s = re.sub(r'phobi[ac]$', '', s, 1)
    s = re.sub(r'(graph)(i?)$', '', s, 1)
    s = re.sub(r'([a-z]+)([ao])logy?$', r'\1\2', s, 1)
  if aggressive:
    s = re.sub(r'([a-z]{4,})[aeiou]$', r'\1', s, 1)
    s = re.sub(r'([a-z]{4,}[lmn])an$', r'\1', s, 1)
    s = re.sub(r'([a-z]{4,})[f][a-z]*$', r'\1', s, 1)
    s = re.sub(r'([a-z]{3,}[^aeiout])ic$', r'\1', s, 1)
    s = re.sub(r'([a-z]{3,}an)[ct]$', r'\1', s, 1)
    s = re.sub(r'([a-z]{3,}[^euirm])al$', r'\1', s, 1)
    s = re.sub(r'([a-z]{3,})mat$', r'\1m', s, 1)
    s = re.sub(r'([a-z]{3,})tur$', r'\1t', s, 1)
    s = re.sub(r'([a-z]{2,}en)[ct]$', r'\1t', s, 1)
    s = re.sub(r'([a-z]{2,}[^ai])ous$', r'\1e', s, 1)
    s = re.sub(r'([a-z]{2,}[aeiou][^wp])er$', r'\1', s, 1)
    s = re.sub(r'([a-z]+)(i|sc|f|et)(en)[ctd]$', r'\1\2\3', s, 1)
    s = re.sub(r'([a-z]+[^cgpte]r)(in|us|id|ic|et|iet|ious)$', r'\1', s, 1)

  return ss.stem(s)


def i_stem(w: str, aggressive=False):
  s = stem(w, aggressive)
  max_it = 10
  while w != s and max_it > 0:
    w = s
    s = stem(s, aggressive)
    max_it -= 1
    if max_it < 1:
      print('!!!', w, s)
  return s

