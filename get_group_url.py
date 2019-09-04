# coding=utf-8
import os
import sys

mode_msg = '''
    0 normal
    1 print sitename group delimiter
    2 print sitename group delimiter with url count
'''
if len(sys.argv) < 2:
    print("python "+sys.argv[0]+" [bkfile]")
    print(mode_msg)
    exit()

f = open(sys.argv[1])
L = [l.strip() for l in f]
L = list(set(L))


mode = 0
if len(sys.argv) == 3:
    mode = int(sys.argv[2])


def get_sitename(l):
    if 'http' not in l:
        return ''
    line = l.split('http')
    return line[1].split('/')[2]


url_group = {}
for l in L:
    key = get_sitename(l)
    if url_group.get(key) is None:
        url_group[key] = []
    url_group[key].append(l)


# for k, v in sorted(url_group.items(), key=lambda d: len(d[1]), reverse=True):
for k, v in sorted(list(url_group.items()), key=lambda d: len(d[1]), reverse=True):
    # print k,len(v)
    if mode == 1:
        if len(v) > 2:
            print("## "+k)
    elif mode == 2:
        if len(v) > 2:
            print("## %s %d" % (k, len(v)))

    for vv in v:
        print(vv)
