# from nltk.metrics import masi_distance
# >> > masi_distance(set([1, 2]), set([1, 2, 3, 4]))

# def ngram(sequence, n=2, **kwargs):
#     for item in ngrams(sequence, 2, **kwargs):
#         yield item


def MASIdistance(X, Y):
    return 1 - float(len(X.intersection(Y))) / float(max(len(Y), len(X)))


def masi_distance(label1, label2):
    """Distance metric that takes into account partial agreement when multiple
    labels are assigned.

    >>> from nltk.metrics import masi_distance
    >>> masi_distance(set([1, 2]), set([1, 2, 3, 4]))
    0.665

    Passonneau 2006, Measuring Agreement on Set-Valued Items (MASI)
    for Semantic and Pragmatic Annotation.
    """

    len_intersection = len(label1.intersection(label2))
    len_union = len(label1.union(label2))
    len_label1 = len(label1)
    len_label2 = len(label2)
    if len_label1 == len_label2 and len_label1 == len_intersection:
        m = 1
    elif len_intersection == min(len_label1, len_label2):
        m = 0.67
    elif len_intersection > 0:
        m = 0.33
    else:
        m = 0

    return 1 - len_intersection / len_union * m


if __name__ == "__main__":
    # """
    # X = set([1, 2, 3])
    # Y = set([3, 1, 2])
    # """
    test_list = [
        [3, 1, 2],
        [1, 1, 2, 3],
        [1],
        [2, 8, 9, 10, 11, 12, 13, 1],
        [1, 2],
        [1, 2, 8],
        [1, 2, 8, 9],
    ]
    test_list_len = len(test_list)
    print(test_list_len)
    print('\n'.join([str((str(idx), str(t))) for idx, t in enumerate(test_list)]))
    print('=')
    for i in range(test_list_len):
        # print(i, test_list_len)
        if i >= test_list_len - 1:
            break
            print(i, test_list[i], test_list[i + 1])
        # print('a', i, i + 1, test_list_len)
        for j in range(test_list_len):
            if i == j:
                continue
            X = set(test_list[i])
            Y = set(test_list[j])
            print(i, j, MASIdistance(X, Y), masi_distance(X, Y), X, Y)
