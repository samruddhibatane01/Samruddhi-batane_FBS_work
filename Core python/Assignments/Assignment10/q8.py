l1 = [10, 20, 30, 40]

dup = []

for i in l1:
    dup.append(i)

print('Original List:', l1)
print('Duplicate List:', dup)

dup[0] = 999
print('After modifying duplicate ->')
print('Original List:', l1)
print('Duplicate List:', dup)

