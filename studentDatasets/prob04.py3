
for x in range(int(input())):
    rate = float(input()) * .01
    amt = float(input())
    pretax = amt / (1.0+rate)
    tax = pretax * rate
    print('On your ${:.2f} purchase, the tax amount was ${:.2f}'.format(amt,tax))