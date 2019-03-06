password = input()
key = 0
for i, c in enumerate(password):
    if i % 2 == 0:
        key += ord(c)
    else:
        key -= ord(c)

while key < 32:
    key += 32

while key > 126:
    key -= 16

while True:
    x = input()
    if x == '':
        break
    ans = []
    for c in x:
        ans.append(hex(ord(c) * key)[2:])

    print(','.join(ans))
