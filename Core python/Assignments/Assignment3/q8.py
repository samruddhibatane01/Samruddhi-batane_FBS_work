import random
userId=input('Enter User Id:')
password=input('Enter password:')
if(userId == 'admin') and (password == '12345'):
    captcha=random.randint(1000,9999)
    print(f'Your captcha: {captcha}')
    chuser=int(input('Enter captcha:'))
    if(chuser == captcha):
        print('Login Successful.')
    else:
        print('Invalid captcha.')
else:
    print('User is Invalid.')