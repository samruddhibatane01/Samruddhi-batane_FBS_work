str = input('Enter a string: ')
n = int(input('Enter index to remove: '))

print('Original String:', str)

new_str = str[:n] + str[n + 1:]

print('String after removing character at index', n, ':', new_str)