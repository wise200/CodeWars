def get_digit(n, index):
    sign = 1
    pi = 3
    for x in range(2, n * 2 + 1, 2):
        pi += sign * 4 / x / (x + 1) / (x + 2)
        sign *= -1
    print(pi)
    return str(pi)[index + 1]


if __name__ == '__main__':
    print(get_digit(int(input()), int(input())))
