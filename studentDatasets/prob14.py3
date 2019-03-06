def solve(a, b, n):
    result = [a]
    for _ in range(n - 1):
        result.append(b)
        a, b = b, a + b
    return [str(x) for x in result]


if __name__ == '__main__':
    f1, f2, num = int(input()), int(input()), int(input())
    print(','.join(solve(f1, f2, num)))