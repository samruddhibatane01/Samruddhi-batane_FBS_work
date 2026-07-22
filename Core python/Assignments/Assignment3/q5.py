a1=int(input('Enter first angle:'))
a2=int(input('Enter second angle:'))
a3=int(input('Enter third angle:'))

if(a1 == a2 == a3):
    print('It is an Equilateral Triangle.')
elif(a1 == a2 or a2 == a3 or a1 == a3):
    print('It is an Isosceles Triangle.')
else:
    print('It is a Scalene Triangle.')