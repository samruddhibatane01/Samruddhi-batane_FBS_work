s1=int(input('Enter first side:'))
s2=int(input('Enter second side:'))
s3=int(input('Enter third side:'))

if(s1 + s2 > s3) and (s1 + s3 > s2) and (s2 + s3 > s1):
    print('It is a valid Triangle.')
else:
    print('It is not a valid Triangle.')