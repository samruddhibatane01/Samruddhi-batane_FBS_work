def reverseNum(num, rev):
    if(num > 0):
        d = num % 10
        rev = rev * 10 + d
        return reverseNum(num // 10, rev)
    else:
        return rev

num = 12345
res = reverseNum(num, 0)
print(res)