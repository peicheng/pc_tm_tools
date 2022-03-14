import sys
from bigram import pcbigram, gram2freqdict


def MASIdistance(X, Y):
    return 1 - float(len(X.intersection(Y))) / float(max(len(Y), len(X)))


def clustring_by_field(L):
    all_titles = list(set(L))
    clusters = {}
    for title1 in all_titles:
        clusters[title1] = []
        for title2 in all_titles:
            if title2 in clusters[title1] or title2 in clusters and title1 in clusters[title2]:
                continue
            distance = MASIdistance(set(list(title1)), set(list(title2)))

            if distance < 0.5:
                # if distance < 0.3:
                clusters[title1].append(title2)

    #clusters=[clusters[title] for title in all_titles if len(clusters[title])>1]
    # merge
    """
    clustersx=[clusters[title] for title in clusters if len(clusters[title])>1]            
    cluster_con={}
    
    for cluster in clustersx:
        print c
    """
    return clusters


def clustring_by_field2(L):
    all_titles = list(set(L))
    clusters = {}

    all_titles2 = all_titles[:]
    cvalue = {}
    rlook = {}
    for title1 in all_titles:

        clusters[title1] = []  # 建立clusters

        for title2 in all_titles2:
            # print len(all_titles2)
            if title2 in clusters[title1] or title2 in clusters and title1 in clusters[title2]:
                continue
            distance = MASIdistance(set(list(title1)), set(list(title2)))

            if distance < 0.5:
                if title1 != title2:
                    if distance <= cvalue.get(title2, 1):

                        clusters[title1].append(title2)
                        """
                        clusters[rlook.get(title2)].remove(title2)

                        rlook[title2]=title1
                        """
                        if title2 in all_titles:
                            all_titles.remove(title2)
                        '''
                        try:
                            all_titles2.remove(title2)
                            all_titles.remove(title2)
                            all_titles2.remove(title1)
                            all_titles.remove(title1)
                        except:
                            pass
                        '''
                        cvalue[title2] = distance
                        # print 'distance',distance,

    print('')
    #clusters=[clusters[title] for title in all_titles if len(clusters[title])>1]
    # merge
    """
    clustersx=[clusters[title] for title in clusters if len(clusters[title])>1]            
    cluster_con={}
    
    for cluster in clustersx:
        print c
    """
    return clusters


if __name__ == '__main__':
    text = u'中文輸入法 中文輸入'
    tlist = list(text)
    pcout = pcbigram(tlist, 3)
    for l in pcout:
        print(l, ''.join(l).encode('utf-8'))
        # print repr(l)
    print(gram2freqdict(pcout))
    X = set(list(u'彩色人生機'))
    Y = set(list(u'彩色人生高速機'))
    """
    X=set([1,2,3])
    Y=set([3,1,2])
    """
    print(MASIdistance(X, Y))
    # f=open('./gaisrec.udn.asus.title.rec')
    # f=open('./news.title.rec')
    f = open(sys.argv[1])
    titles = [l[:-1].decode('utf-8') for l in f]
    cdict = {}
    cdict = clustring_by_field2(titles)
    countn = 1
    for k, v in cdict.items():
        print(k.encode('utf-8'))
        print('==' * 10)
        for vv in v:

            print(countn, vv.encode('utf-8'))
            countn += 1

        print('---' * 10)
        print('')

    dicttest = {'a': '1', 'b': '2', 'c': '33'}
    for k in dicttest:
        print(k)
