s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}

print('Set 1:', s1)
print('Set 2:', s2)

s1.difference_update(s2)
print(type(s1))
print('Set 1 after removing intersection:', s1)