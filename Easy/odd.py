from math import log

n = int(raw_input())

for i in range(n):
    number = int(raw_input())
    print int(pow(2, int(log(number, 2))))