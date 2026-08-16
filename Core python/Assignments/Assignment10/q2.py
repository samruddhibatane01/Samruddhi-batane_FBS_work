l1 = [10, 50, 20, 5, 40]

maxi = l1[0]
mini = l1[0]

for i in l1:
    if i > maxi:
        maxi = i
    if i < mini:
        mini = i

print('Maximum:', maxi)
print('Minimum:', mini)