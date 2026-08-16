l1 = [10, 50, 20, 5, 40]

largest = l1[0]
second = l1[0]

for i in l1:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print('Second Largest:', second)