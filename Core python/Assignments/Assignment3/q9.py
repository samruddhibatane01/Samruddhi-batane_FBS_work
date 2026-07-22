s1=int(input('Enter marks of subject 1:'))
s2=int(input('Enter marks of subject 2:'))
s3=int(input('Enter marks of subject 3:'))
s4=int(input('Enter marks of subject 4:'))
s5=int(input('Enter marks of subject 5:'))

total = s1 + s2 + s3 + s4 + s5
per=total/500 * 100

if(per >= 60):
    print('First Class.')
elif(per >= 50):
    print('Second Class.')
elif(per >= 40):
    print('Third Class.')
else:
    print('Fail')