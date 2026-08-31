di = {'id':101, 'name':'ABC', 'dept':'IT'}

print('Original Dictionary:', di)

key = input('Enter key to remove: ')

res = di.pop(key, 'Key not found.')

print('Removed Value:', res)
print('Dictionary after removing key:', di)