# -*-coding:utf-8 -*-
import random

def shuffle(lol, seed):
    '''
    lol :: list of list as input
    seed :: seed the shuffling

    shuffle inplace each list in the same order
    '''
    for l in lol:
        random.seed(seed)
        random.shuffle(l)

def minibatch(l, bs):
    '''
    l :: list of word idxs
    return a list of minibatches of indexes
    which size is equal to bs
    border cases are treated as follow:
    eg: [0,1,2,3] and bs = 3
    will output:
    [[0],[0,1],[0,1,2],[1,2,3]]
    '''
    out  = [l[:i] for i in range(1, min(bs,len(l)+1) )]
    out += [l[i-bs:i] for i in range(bs,len(l)+1) ]
    assert len(l) == len(out)
    return out


def contextwin(l, win):
    '''
    win :int,窗口大小，只能为奇数且大于等于1
     l : array containing the word indexes of a sentence
    the function will return a list of list of indexes corresponding
    to context windows surrounding each word in the sentence
    a sample:
            x = array([0, 1, 2, 3, 4], dtype=int32)
            contextwin(x, 3) =>  [[-1, 0, 1],
                                 [ 0, 1, 2],
                                 [ 1, 2, 3],
                                 [ 2, 3, 4],
                                 [ 3, 4,-1]]
    '''
    assert (win % 2) == 1          # 如果assert后面的表达式为真，则继续向下执行
    assert win >= 1
    l = list(l)

    lpadded = int(win/2) * [-1] + l + int(win/2) * [-1]
    out = [lpadded[i:i+win] for i in range(len(l))]

    assert len(out) == len(l)
    return out

