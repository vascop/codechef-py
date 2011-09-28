n, k = raw_input().split()
n = int(n)
k = int(k)

div = 0

for i in range(n):
    new = int(raw_input())
    if (new % k) == 0:
        div += 1

print div