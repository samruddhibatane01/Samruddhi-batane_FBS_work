l1 = [10, 20, 30, 20, 10, 20]

num = int(input('Enter number to search:'))
count = 0

for i in l1:
    if i == num:
        count = count + 1

if count > 0:
    print(num, 'is present', count, 'times')
else:
    print(num, 'is not present in the list')