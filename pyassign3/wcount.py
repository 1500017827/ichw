#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Zhou Xu-yuan "
__pkuid__  = "1500017827"
__email__  = "1500017827@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def turn_txt(c):
    """
    This function remove all things from the given text except English words or whitespace
    :param c: the given text
    :return: a text created from the given text that only has English words or whitespace in it,
             which has type string
    """
    i = ''
    for j in range(len(c)):
        m = str(c[j])
        if 97 <= ord(m) <= 122:
            i += m
        elif 65 <= ord(m) <= 90:
            i += chr(ord(m)+32)
        else:
            i += ' '
    return i


def is_allalpha(s):
    """
    This function checks if the given parameter is an English word
    :param s: any input which has type string
    :return: True if s is an English word, False if s is not an English word
    """
    b = [s[i].isalpha for i in range(len(s))]
    return all(b)


def wcount(l, t=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line.
    """
    al_wd_str = turn_txt(l)
    t_lst = al_wd_str.split()
    t_wd = list(filter(is_allalpha, t_lst))
    wd_set = list(set(t_wd))
    wd_count = [t_wd.count(i) for i in wd_set]
    wd_f_lst = list(zip(wd_set, wd_count))
    sort_t = sorted(wd_f_lst, key=lambda kv: kv[1], reverse=True)
    print('word', ' '*7, 'frequency')
    for i in range(t):
        a = len(sort_t[i][0])
        print(sort_t[i][0], str(sort_t[i][1]).rjust(18-a))

    pass


if __name__ == '__main__':

    if len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
