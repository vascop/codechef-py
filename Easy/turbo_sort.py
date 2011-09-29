from sys import stdin

n = stdin.readline()

x = map(int, stdin.readlines())
x.sort()

for j in x:
    print j
