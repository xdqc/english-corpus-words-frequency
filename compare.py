import os
import math
import collections
import itertools
from pandas import DataFrame, ExcelWriter


def make_order(filename, compare_size):
    words = {}
    with open(filename) as f:
        for index, line in enumerate(f, start=1):
            words[line.strip()] = math.log(index)
            if index >= compare_size:
                break
    return words


def output_diff(diff: list, up_corpus, down_corpus):
    print('\n\n----')
    print('####', up_corpus.split('_')[
          1][:4] + '-' + down_corpus.split('_')[1][:4])
    print()
    down_words = []
    for word in diff:
        if 2 < word[1] < 9:
            print('>'+word[0])
        elif -9 < word[1] < -2:
            down_words.insert(0, word)
    print('\n')
    for word in down_words:
        print('>'+word[0])


def compare_corpus(first_corpus, second_corpus, compare_size, corpus_dir, writer):
    down_words = make_order(corpus_dir+second_corpus, compare_size)
    up_words = make_order(corpus_dir+first_corpus, compare_size)

    diff = {}

    num_commons = 0
    total_distance = 0
    total_distance_sqr = 0
    total_words = math.ceil((len(up_words) + len(down_words)) / 2)
    ln_up = math.log(len(up_words))
    ln_down = math.log(len(down_words))

    for word in down_words:
        if word in up_words:
            diff[word] = down_words[word] - up_words[word]
            num_commons += 1
            total_distance += abs(diff[word])
            total_distance_sqr += diff[word] * diff[word]
        else:
            diff[word] = -ln_up - (ln_down - down_words[word])

    for word in up_words:
        if word not in down_words:
            diff[word] = ln_down + (ln_up - up_words[word])

    diff = sorted(diff.items(), key=lambda kv: kv[1], reverse=True)

    # output_diff(diff, first_corpus, second_corpus)

    df_name = first_corpus.split(
        '_')[1][:4] + '_' + second_corpus.split('_')[1][:4]

    df = DataFrame({
        'title': df_name,
        'total': total_words,
        'commons': num_commons,
        'common_pct': num_commons/total_words,
        'dist_sum': total_distance,
        'dist_sqrsum': total_distance_sqr,
        'dist_avg': total_distance/num_commons,
        'similarity': num_commons/total_distance_sqr
    }, index=[0])

    # df2 = DataFrame(diff, columns=['Word', 'Distance'])
    # df2 = df.append(df2, ignore_index=True, sort=False)
    # df2.to_excel(writer, sheet_name=df_name, index=False)
    # writer.save()

    return df


def compare_batch(corpus_dir, compare_size, writer):
    files = sorted(os.listdir(corpus_dir))

    df = DataFrame()
    for pair in itertools.combinations(files, 2):
        df = df.append(compare_corpus(*pair, compare_size, corpus_dir, writer),
                       sort=False, ignore_index=True)

    print(df)
    df.to_excel(writer, sheet_name=corpus_dir.split(
        '_')[2][:-1]+str(compare_size), index=False)
    writer.save()


def __main__():
    writer = ExcelWriter('test.xlsx')
    dirs = [
        './corpus_g_new/',
        './corpus_f_n/',
        './corpus_f_all/',
        './corpus_f_webster/',
        './corpus_f_oxford/'
    ]
    sizes = [10000, 20000, 99999]

    for prod in itertools.product(dirs, sizes, repeat=1):
        print(prod)
        compare_batch(*prod, writer)


__main__()
