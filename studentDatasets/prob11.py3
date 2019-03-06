dims = [int(x) for x in input().split()]

width = dims[0]
height = dims[1]

levels = [None] * height

for x in range(height):
    string = input()
    levels[int(string[:1])] = string[1:]

for x in range(height-1, -1, -1):
    print(str(x) + levels[x])