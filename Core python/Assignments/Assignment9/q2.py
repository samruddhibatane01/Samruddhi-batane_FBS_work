def armstrong(num, digits):
    if(num > 0):
        d = num % 10
        return d ** digits + armstrong(num // 10, digits)
    else:
        return 0

num = 153
digits = len(str(num))
res = armstrong(num, digits)

if(res == num):
    print('The number is Armstrong')
else:
    print('The number is not Armstrong')