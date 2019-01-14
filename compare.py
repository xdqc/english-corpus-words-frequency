import os
import collections
import math
import itertools
import csv
from pandas import DataFrame, ExcelWriter


def make_order(filename):
    words = {}
    with open(filename) as f:
        index = 0
        for line in f:
            index += 1
            words[line.strip()] = math.log(index)
            if index >= compare_size:
                break
    return words


def compare_corpus(first_corpus, second_corpus, writer):
    down_words = make_order(corpus_dir+second_corpus)
    up_words = make_order(corpus_dir+first_corpus)

    diff = {}

    num_commons = 0
    total_distance = 0

    for word in down_words:
        if word in up_words:
            diff[word] = down_words[word] - up_words[word]
            num_commons += 1
            total_distance += abs(diff[word])
        else:
            diff[word] = -math.log(len(up_words)) - \
                (math.log(len(down_words)) - down_words[word])

    for word in up_words:
        if word not in down_words:
            diff[word] = math.log(len(down_words)) + \
                (math.log(len(up_words)) - up_words[word])

    diff = sorted(diff.items(), key=lambda kv: kv[1], reverse=True)

    df = DataFrame({
        'total': compare_size,
        'commons': num_commons,
        'dist_sum': total_distance,
        'dist_avg': total_distance/num_commons,
        'similarity': num_commons*num_commons/compare_size/total_distance
    }, index=[0])

    df_name = first_corpus.split('_')[1][:4] + '_' + second_corpus.split('_')[1][:4]
    # print(df)

    df2 = DataFrame(diff, columns=['Word', 'Distance'])
    df = df.append(df2, ignore_index=True, sort=False)

    df.to_excel(writer, sheet_name=df_name, index=False)
    writer.save()

    return {
        'title': df_name,
        'total': compare_size,
        'commons': num_commons,
        'dist_sum': total_distance,
        'dist_avg': total_distance/num_commons,
        'similarity': num_commons*num_commons/compare_size/total_distance
    }

compare_size = 20000
corpus_dir = './corpus_f_all/'

files = os.listdir(corpus_dir)

writer = ExcelWriter('test.xlsx')

df = DataFrame()
for pair in itertools.combinations(files, 2):
    df = df.append(DataFrame(compare_corpus(*pair, writer), index=[0]), sort=False, ignore_index=True)
    print(df)

df.to_excel(writer, sheet_name='summary', index=False)
writer.save()
