l1 = [10, 50, 20, 5, 40]

n = len(l1)
for i in range(n):
    for j in range(n - i - 1):
        if l1[j] > l1[j + 1]:
            l1[j], l1[j + 1] = l1[j + 1], l1[j]

print('Sorted list =', l1)
print('Second Largest:', l1[-2])