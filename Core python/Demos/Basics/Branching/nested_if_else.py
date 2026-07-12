gender = input('Enter gender(m/f):')
age = int(input('Enter age:'))
if(gender == 'f'):
    if(age>=18):
        print('Girl is eligible for Marriage.')
    else:
        print('Girl is not eligible for Marriage.')
else:
    if(age>=21):
        print('Boy is eligible for Marriage.')
    else:
        print('Boy is not eligible for Marriage.')