n = int(input('Enter number:'))
print('Integers that are not divisible by 2 and 3 upto the given number are:')

for i in range(1,n+1):
    if(i % 2 != 0) and (i % 3 != 0):
        print(i)