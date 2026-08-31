l1 = [10, 20, 30, 40, 50]
target = int(input('Enter target sum: '))

s = set(l1)
pairs = set()

for num in l1:
    complement = target - num
    if complement in s and num != complement:
        pairs.add((min(num, complement), max(num, complement)))

print('Pairs with sum', target, ':', pairs)