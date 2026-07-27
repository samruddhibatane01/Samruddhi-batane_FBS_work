num=int(input('Enter number:'))
temp = num
sum = 0

n=len(str(num))

while(num>0):
    digit = num % 10
    sum = sum + (digit ** n)
    num = num // 10
if(sum == temp):
    print('Armstrong Number')
else:
    print('Not an Armstrong Number')