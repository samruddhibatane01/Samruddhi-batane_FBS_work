userid=input('Enter UserID:')
password=input('Enter password:')
if(userid == 'admin') and (password == '1234'):
    print('Login Successful.')
else:
    print('Invalid User ID or Password.')