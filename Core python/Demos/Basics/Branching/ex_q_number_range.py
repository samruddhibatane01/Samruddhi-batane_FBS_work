num = int(input('Enter number:'))
if(num > 0):
    if(num > 50):
        if(num > 100):
            if(num > 150):
                if(num > 250):
                    print('The number is greater than 250.')
                else:
                    print('The number is between the range 150 - 250.')
            else:
                print('The number is between the range 100 - 150.')
        else:
            print('The number is between the range 50 - 100.')
    else:
        print('The number is between the range 0 - 50.')
else:
    print('The number is less then 0.')