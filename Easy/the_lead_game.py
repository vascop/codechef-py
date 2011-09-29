from sys import stdin
from math import fabs

rounds = int(stdin.readline())

scores = []
lead = 0
nmax = 0

for i in range(rounds):
    scores = [int(x) for x in stdin.readline().split()]

    lead += scores[0]-scores[1]
    
    if fabs(lead) > nmax:
        nmax = fabs(lead)
        smax = lead

    player = 1 if smax > 0 else 2

print "%d %d" % (player, nmax)