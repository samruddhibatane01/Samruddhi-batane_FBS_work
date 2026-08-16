l1 = [10, 15, 22, 33, 40, 51]

result = []

for i in l1:
    if i % 2 != 0:
        result.append(i)

print('List after removing even numbers:', result)