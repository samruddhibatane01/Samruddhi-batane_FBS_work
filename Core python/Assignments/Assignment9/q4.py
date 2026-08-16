def series(n):
    if(n > 0):
        return n + series(n - 1)
    else:
        return 0

n = 10
res = series(n)
print(res)