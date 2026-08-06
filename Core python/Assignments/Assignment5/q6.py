n = int(input('Enter value of n:'))
count = 0
num = 1
print('First', n, 'prime numbers are:')

while(count < n):
    num = num + 1
    
    prime = 1
    for i in range(2, num):
        if(num % i == 0):
            prime = 0
            break

    if(prime == 1):
        print(num)
        count = count + 1

     