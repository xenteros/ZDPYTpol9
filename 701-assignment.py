import urllib.request
from typing import *
import re
import json


def download_file(url: str):
    data = urllib.request.urlopen(url)

    with open(url.split('/')[-1], 'w', encoding='utf-8') as f:
        for line in data:
            line = line.decode('utf-8').strip()
            f.write(line)
            f.write('\n')


def count_words(file_path: str) -> Dict[str, int]:
    d = dict()
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            for word in line.split(' '):
                regex = re.compile('[^AaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnŃńOoÓóPpRrSsŚśTtUuWwYyZzŹźŻż]')
                word = regex.sub('', word).lower()
                if word not in d:
                    d[word] = 0
                d[word] += 1

    return d


def count_letters(d):
    res = dict()
    for word in d:
        if word == '':
            continue
        letter = word[0]
        if letter not in res:
            res[letter] = 0
        res[letter] += d[word]

    return res


def yield_lines_containing(regex):
    with open('pan-tadeusz.txt', 'r', encoding='utf-8') as f:
        for line in f:
            words = re.findall(regex, line)
            if len(words) > 0:
                yield line


if __name__ == '__main__':
    url = 'https://wolnelektury.pl/media/book/txt/pan-tadeusz.txt'
    # download_file(url)
    d = count_words('pan-tadeusz.txt')
    jsn = json.dumps(d)
    with open('count.json', 'w', encoding='utf-8') as f:
        f.write(jsn)

    print(count_letters(d))

    import numpy as np
    # import matplotlib.pyplot as plt
    #
    # plt.bar(*zip(*count_letters(d)), height=20000, color='g')
    # plt.show()

    for line in yield_lines_containing(r'Mickiewicz'):
        print(line)