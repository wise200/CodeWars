NUMBERS = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'ELEVEN', 'TWELVE']


def get_string(s):
    numbers = [int(x) for x in s.split(' ')]
    letters = []
    for x in numbers[:-1]:
        for letter in NUMBERS[x]:
            letters.append(letter)
    return s[-4:] + '. ' + ' '.join(sorted(letters))


if __name__ == '__main__':
    print(get_string(input()))
