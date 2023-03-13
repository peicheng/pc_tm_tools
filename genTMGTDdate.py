# coding=utf-8
import os
import sys
import datetime
import calendar
"""
    Gen TM GTD Date
    ============
    given month and gen GTD prifix

    ex.
    genTMGTDdate.py 1304 1 
    return
        * 130401 (一
        * 130402 (二
        ...
"""
#print sys.argv[0],sys.argv[1]
chtweeklist = ['一', '二', '三', '四', '五', '六', '日']
if len(sys.argv) < 2:
    print("""
    python genTMGTDdate.py 1304 [0] [+r|-r]
                           monthprifix weekstartday
    python3 genTMGTDdate.py 2303 2 +r
    """)
    print('len', len(sys.argv))
    exit()
reverse_flag = True
if len(sys.argv) >= 3:
    option = sys.argv[2]
    for s in sys.argv:
        if s == '+r':
            reverse_flag = False
prefixstr = "* "+sys.argv[1]
startchtweek = int(datetime.datetime.strptime(
    sys.argv[1]+'01', "%y%m%d").weekday())

startchtweek, monthday = calendar.monthrange(
    int(sys.argv[1][:2]), int(sys.argv[1][2:]))
if len(sys.argv) >= 3:
    mode = sys.argv[2]
L = []
for i in range(1, monthday+1):
    #print i
    if startchtweek == 7:
        startchtweek = 0
    # print prefixstr+str(i).zfill(2)+' ('+chtweeklist[startchtweek]
    if mode == '2':
        L.append('GTD '+'{}.{}.'.format(prefixstr[2:4],prefixstr[4:6])+str(i).zfill(2)+' '+str(startchtweek+1))
    else:
        L.append(prefixstr+str(i).zfill(2)+' ('+chtweeklist[startchtweek]+str(startchtweek))
    startchtweek = startchtweek + 1
    # print(startchtweek)
if reverse_flag:
    L = reversed(L)

for l in L:
    print(l)
