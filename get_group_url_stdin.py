# coding=utf-8
import os
import sys

mode_msg = '''
    0 normal
    1 print sitename group delimiter
    2 print sitename group delimiter with url count
'''
if len(sys.argv) < 2:
    print("python " + sys.argv[0] + " [bkfile]")
    print(mode_msg)
    exit()

L = []
for line in sys.stdin:
    line = line.strip()
    L.append(line)

# f = open(sys.argv[1])
# L = [l.strip() for l in f]
L = list(set(L))


mode = 2
if len(sys.argv) > 1:
    mode = int(sys.argv[1])


def get_sitename(l):
    if 'http' not in l:
        return ''
    line = l.split('http')
    try:
        return line[1].split('/')[2]
    except Exception:
        return ''


def group_non_group_list(L):

    pass


url_group = {}
for l in L:
    key = get_sitename(l)
    if url_group.get(key) is None:
        url_group[key] = []
    url_group[key].append(l)

non_group_list = []
# for k, v in sorted(url_group.items(), key=lambda d: len(d[1]), reverse=True):
for k, v in sorted(list(url_group.items()), key=lambda d: len(d[1]), reverse=True):
    # print k,len(v)
    if mode == 1:
        if len(v) > 2:
            print("## " + k)
    elif mode == 2 or mode == 3:
        if len(v) >= 2:
            print("## %s %d" % (k, len(v)))

    for vv in v:
        if mode == 3 and len(v) < 2:
            non_group_list.append(vv)
        else:
            print(vv)

# print(non_group_list[:2])
