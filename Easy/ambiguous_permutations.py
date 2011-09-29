import sys

while True:
    size = int(sys.stdin.readline())

    if size == 0:
        exit(0)
    else:
        vec = [int(x) for x in sys.stdin.readline().split()]
        new = list(vec)

        j = 1
        for i in vec:
            new[i-1] = j
            j += 1

        if vec == new:
            print "ambiguous"
        else:
            print "not ambiguous"
    