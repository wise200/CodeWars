def solve(a, b):
    return a * b + \
           a * b * (a + b - 2) // 2 + \
            a * (a - 1) * b * (b - 1) // 4 + \
            a * (a - 1) * (a - 2) * b // 6 + \
            a * b * (b - 1) * (b - 2) // 6


if __name__ == '__main__':
    [x, y] = [int(x) for x in input().split(' ')]
    print(solve(x, y))
