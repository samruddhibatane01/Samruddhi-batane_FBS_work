def check_armstrong(num):
    original = num
    temp = num
    digits = 0

    while temp > 0:
        digits = digits + 1
        temp = temp // 10

    temp = num
    s = 0
    while temp > 0:
        digit = temp % 10
        s = s + digit ** digits
        temp = temp // 10

    if original == s:
        print(original, 'is an Armstrong Number')
    else:
        print(original, 'is not an Armstrong Number')

num = int(input('Enter a number: '))

check_armstrong(num)