n = 5
total = 2 * n - 1   

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=' ')

    start = i if i < n else n - 1
    gap = total - i - start
    for j in range(gap):
        print(' ', end=' ')

    for j in range(start, 0, -1):
        print(j, end=' ')

    print()