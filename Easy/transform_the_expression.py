n = int(raw_input())

for i in range(n):
    expression = raw_input()
    out = []
    operators = []

    for j in expression:
        if j == ')':
            out.append(operators.pop())
        elif j >= 'a' and j <= 'z':
            out.append(j)
        elif j == '+' or j == '-' or j == '*' or j == '/' or j == '^':
            operators.append(j)

    print ''.join(out)