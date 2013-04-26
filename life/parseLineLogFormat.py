#coding=utf-8
"""
    
    13.04.27 01:22:48 Peicheng Liao <peicheng5 (a) gmail.com> 
    =========================
    Goal:
        Parse Line log to readable format
    usage:
        python parseLineLogFormat.py [FILE]
        ex:

    inputformat
    00:12 PC lalalla
    output:
        lalalala
"""
import sys,os
if len(sys.argv)<2:
    print '''Goal:
        Parse Line log to readable format
    usage:
        python parseLineLogFormat.py [FILE]
        ex:
    '''
    exit()
f=open(sys.argv[1])
lines=f.readlines()
lines=[l.strip() for l in lines]
for l in lines:
    print ''.join(l.split(' ')[2:])
