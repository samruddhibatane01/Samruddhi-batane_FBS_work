def chkPallindrome():
    num = int(input('Enter number:'))
    temp = num
    rev = 0

    while(temp):
        d = temp % 10
        temp = temp // 10
        rev = rev * 10 + d

    if(num == rev):
        print('The number is Pallindrome')
    else:
        print('The number is not Pallindrome')

chkPallindrome()