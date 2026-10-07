a1=int(input('Enter first angle:'))
a2=int(input('Enter second angle:'))
a3=int(input('Enter third angle:'))

if(a1 + a2 + a3 == 180): #sum of angles of triangle is 180.
    print(f'It is a valid Triangle.')
else:
    print(f'It is not a valid Triangle.')
