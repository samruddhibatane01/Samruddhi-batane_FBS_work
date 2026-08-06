start = int(input('Enter starting number:'))
end = int(input('Enter ending number:'))
print('Armstrong numbers within the given range are:')

num = start
while(num <= end):
    temp = num
    sum = 0

    while(temp > 0):
        digit = temp % 10
        sum = sum + (digit * digit * digit)
        temp = temp // 10

    if(sum == num):
        print(num)
    num = num + 1