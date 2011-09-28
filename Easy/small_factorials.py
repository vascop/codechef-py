n = int(raw_input())

for i in range(n):
    number = int(raw_input())
    answer = 1
    for j in range(1, number+1):
        answer *= j
    print answer

