#!/usr/bin/python2

from random import shuffle

def fill_server(capacity, videos):
    curr = 0
    ret = set()
    indices = list(enumerate(videos))
    shuffle(indices)
    for i, size in indices:
        if curr + size > capacity:
            continue
        ret.add(i)
        curr += size
    return ret
    
if __name__ == '__main__':
    vids = [44,3,6,54, 12, 43, 22, 1, 50, 12]
    result = fill_server(64, vids)
    print result
    print sum(map(lambda x: vids[x], result))
