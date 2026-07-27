n = int(input('Enter number:'))
print('Odd Numbers up to', n, 'are:')
for i in range(1, n+1):
    if(i % 2 != 0):
        print(i)
