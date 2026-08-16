def sumDigits(num):
    if(num > 0):
        d = num % 10
        return d + sumDigits(num // 10)
    else:
        return 0

num = 12345
res = sumDigits(num)
print(res)