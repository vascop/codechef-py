import sys

triangles = int(sys.stdin.readline())

for triangle in range(triangles):
    lines = int(sys.stdin.readline())
    mysum = []

    linesread = 0
    for line in range(lines):
        read = [int(x) for x in sys.stdin.readline().split()]
        i = 0
        last_sum = [x for x in mysum]
        for number in read:
            if linesread == 0:
                mysum.append(number)
            elif i+1 > linesread:
                mysum.append(last_sum[i-1]+number)
            else:
                lmax = last_sum[i]+number
                if i > 0:
                    if last_sum[i-1]+number > lmax:
                        lmax = last_sum[i-1]+number
                mysum[i] = lmax
                
            i += 1
        linesread += 1

    print max(mysum)

# NOT FAST ENOUGH