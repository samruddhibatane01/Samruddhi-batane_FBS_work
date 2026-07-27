num=int(input('Enter number:'))
temp=num
sum=0

while(num>0):
    digit = num % 10

    fact=1
    for i in range(1,digit + 1):
        fact =fact * i
    sum = sum + fact
    num = num // 10

if(sum == temp):
    print('It is a Strong Number.')
else:
    print('It is not a Strong Number.')