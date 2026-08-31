di = {'id':101, 'name':'ABC', 'dept':'IT'}

key = input('Enter key to check: ')

if key in di.keys():
    print('Key exists in the dictionary')
else:
    print('Key does not exist in the dictionary')