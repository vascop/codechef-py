from sys import stdin
from collections import defaultdict

n, k = (int(x) for x in stdin.readline().split())

d = defaultdict(bool)
count = 0

for click in xrange(k):
    action = stdin.readline()
    if action.startswith('CLI'):
        _, tweet = action.split()
        d[tweet] = not d[tweet]
        if d[tweet]:
            count += 1
        else:
            count -= 1
    else:
        d = defaultdict(bool)
        count = 0
    print count
