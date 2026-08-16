l1 = [10, 20, 30, 20, 40, 20]

num = int(input('Enter element to remove:'))
result = []

for i in l1:
    if i != num:
        result.append(i)

print('List after removal:', result)