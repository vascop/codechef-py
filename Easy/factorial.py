n = int(raw_input())

for i in range(n):
    number = int(raw_input())

    temp = res = number / 5

    while temp >= 5:
        temp = temp / 5
        res += temp
    
    print res