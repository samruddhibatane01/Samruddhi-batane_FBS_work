n = int(input('Enter n: '))

di = dict.fromkeys(range(1, n + 1))

for x in di.keys():
    di[x] = x * x

print('Dictionary:', di)
