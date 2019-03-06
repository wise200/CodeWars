rules = [
    'Scissors cuts Paper',
    'Paper covers Rock',
    'Rock crushes Lizard',
    'Lizard poisons Spock',
    'Spock smashes Scissors',
    'Scissors decapitates Lizard',
    'Lizard eats Paper',
    'Paper disproves Spock',
    'Spock vaporizes Rock',
    'Rock crushes Scissors'
]


def solve(p1, p2):
    if p1 == p2:
        return f'TIE, {p1.upper()} does not affect {p2.upper()}'
    for r in rules:
        if p1 in r and p2 in r:
            if r.index(p1) < r.index(p2):
                return f'{p1.upper()} WINS, {r}'
            else:
                return f'{p1.upper()} LOSES, {r}'


if __name__ == '__main__':
    [p1, p2] = input().split(' ')
    print(solve(p1, p2))