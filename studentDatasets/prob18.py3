def get_index(n, magic):
    x = [i for i in range(n)]
    for i in range(n - 1):
        x.pop(magic * i % len(x))
    return x[0]


numc = int(input())
names = []
cats = []
inp = input()
while inp != 'Magic Number:':
    names.append(inp[:-10])
    temp = []
    for _ in range(numc):
        temp.append(input())
    cats.append(temp)
    inp = input()

magic = int(input())
index = get_index(numc, magic)
print('Your MASH Story:')
for name, cat in zip(names, cats):
    print(f'{name} - {cat[index]}')
