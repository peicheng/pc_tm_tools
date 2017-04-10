#coding=utf-8
"""
    14.07.02 21:51:52 Peicheng Liao <peicheng5 (a) gmail.com>
    =========================
    Goal:
        list dir's ext and mkdir for ext
        move same ext to ext dir

"""
import os,sys
from datetime import datetime
d=datetime.now()
today=d.strftime('%y%m%d_%s')

print len(sys.argv),today
dir_prefix=today+'_back'
min_files_size=2
if len(sys.argv) < 2 :
    print 'python mvFiles.py [DIR]'
    print '''
    Goal:
        list dir's ext and mkdir for ext
        move same ext to ext dir
    '''
    exit()
rootdir=sys.argv[1]

extDict={}
files=[f for f in os.listdir(rootdir) if os.path.isfile(os.path.join(rootdir,f)) ]

for f in files:
    print f
    ext=f.split('.')[-1]
    ext=ext.lower()
    if extDict.get(ext):
        extDict[ext].append(f)
    else:
        extDict[ext]=[]
        extDict[ext].append(f)

for k,v in extDict.items():
    if len(v) > min_files_size:
        print k,len(v)
        dirname=dir_prefix+'_'+k
        print 'mkdir ',dirname
        os.makedirs(rootdir+'/'+dirname)
        for f in v:
            oldfn=rootdir+'/'+f
            newfn=rootdir+'/'+dirname+'/'+f
            print '\tmove ',oldfn,'to',newfn
            os.renames(oldfn,newfn)


