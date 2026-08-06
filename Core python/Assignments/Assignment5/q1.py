correct_id = 'admin'
correct_password = '1234'

attempts = 3

while(attempts > 0):
    userid = input('Enter user ID:')
    password = input('Enter password:')
    if(userid == correct_id) and (password == correct_password):
        print('Login Successful')
        break
    else:
        attempts = attempts - 1
        print('Incorrect user ID or Password')

        if(attempts == 0):
            print('Program Terminated')
        else:
            print('Try again. Attempts left:', attempts)
