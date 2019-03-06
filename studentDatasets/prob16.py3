if __name__ == '__main__':
    a = input().split(' ')
    i = 0
    prev = ''
    while i < len(a) - 1:
        word = a[i].lower()
        if word == a[i + 1].lower():
            if (word != 'is' and word != 'had') or prev == word:
                a.pop(i + 1)
            else:
                i += 1
        else:
            i += 1
        prev = word
    print(' '.join(a))
