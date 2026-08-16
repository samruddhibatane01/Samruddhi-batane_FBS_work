l1 = [10, 20, 10, 30, 20, 40]

result = []

for i in l1:
    if i not in result:
        result.append(i)

print('List after removing duplicates:', result)