
def encode(c):
    if not (c.isdigit() or c.isalpha()):
        return '0x25' + hex(ord(c))[2:]
    return c


url = input()
ans = 'https' + encode(':') + encode('/') * 2
found = True
i = 8
while url[i] != '/':
    ans += url[i]
    i += 1
for i in range(i,len(url)):
    ans+= encode(url[i])
print(ans)