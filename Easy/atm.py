x, y = raw_input().split()

withdraw = int(x)
balance = float(y)

invalid = withdraw % 5
new_balance = balance - withdraw - 0.5

if new_balance >= 0 and invalid == 0:
    print "%.2f" % new_balance
else:
    print "%.2f" % balance

    