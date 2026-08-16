l1 = [10, 15, 22, 33, 40, 51, 60]

even = []
odd = []

for i in l1:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print('Even Elements:', even)
print('Odd Elements:', odd)