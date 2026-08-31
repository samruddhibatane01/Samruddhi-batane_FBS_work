str = input('Enter a string: ')

words = str.split()
di = {}

for w in words:
    di[w] = di.get(w, 0) + 1

print('Word Frequency:', di)