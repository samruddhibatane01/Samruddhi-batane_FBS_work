def chkPrime(num, i):
    if(num < 2):
        return 0
    if(i > num ** 0.5):
        return 1
    if(num % i == 0):
        return 0
    else:
        return chkPrime(num, i + 1)

num = 29
res = chkPrime(num, 2)

if(res == 1):
    print('The number is Prime')
else:
    print('The number is not Prime')