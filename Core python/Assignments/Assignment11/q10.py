l = [10, 15, 22, 33, 40, 51]

for i in range(len(l) -1, -1, -1):
    if l[i] % 2 == 0:
        l.pop(i)

print('List after removing even numbers:', l)