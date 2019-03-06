from collections import Counter


def solve(line):
    d = Counter(line)
    p1 = ''.join(f'{key}[{d[key]}]' for key in sorted(d.keys(), key=lambda x: -ord(x)) if d[key] < 10).replace(' ', '_')
    p2 = ''.join(f'{key}[{d[key]}]' for key in sorted(d.keys(), key=lambda x: ord(x)) if d[key] >= 10).replace(' ', '_')
    return p1 + ';' + p2


if __name__ == '__main__':
    print(solve(input()))
