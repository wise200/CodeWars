def toString(n):
    return '{:04d}'.format(n)

def fits(n):
    base = int(toString(n)[2:])
    sqr = int(toString(n)[:2])
    return base**2 == sqr

def cont(n, defs, maybes):
    string = toString(n)
    for c in string:
        if c not in defs and c not in maybes:
            return False
    for c in defs:
        if c not in string:
            return False
    return True

string  = ''
for x in range(3):
    string += input()

string = input()[1] + string


defs = []
maybes = []

for x in range(len(string)):
    if string[x] == 'C':
        defs.append(str(x))
    if string[x] == 'U':
        maybes.append(str(x))

solves = []

for x in range(1,10000):
    if fits(x) and cont(x, defs, maybes):
        solves.append(toString(x))

if len(solves) == 0:
    print('COULD NOT DETERMINE CODE')
elif len(solves) == 1:
    print('CODE IS ' + solves[0])
elif len(solves) <= 3:
    for s in solves:
        print('POSSIBLE MATCH: ' + s)
else:
    print('WILL NOT WIN BET')
