def solve(a, b, c, d):
    if a == 'X':
        return int(c) * int(b) / int(d)
    if b == 'X':
        return int(a) * int(d) / int(c)
    if c == 'X':
        return int(a) * int(d) / int(b)
    return int(c) * int(b) / int(a)


if __name__ == '__main__':
    print(f'{solve(input(), input(), input(), input()):.1f}')
