#!/usr/bin/python2

def output_format(fname, solution):
    filtered = filter(lambda x: len(x) > 0, solution)
    with open(fname, 'wb') as f:
        f.write("%d\n" % len(filtered))
        for c, videos in enumerate(solution):
            if len(videos) > 0:
                f.write("%i %s\n" % (c, ' '.join(map(lambda x: str(x), videos))))
        
if __name__ == '__main__':
    from sys import argv

    fname = '/dev/stdout'
    if len(argv) >= 2:
        fname = argv[1]
    output_format(fname, [set((1,2)), set(), set((3,)), set((4,4,3,3,2,5,2)), set(), set()])
