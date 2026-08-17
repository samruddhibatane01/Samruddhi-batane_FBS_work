str = input('Enter a string: ')

count = 0
vowels = 'aeiouAEIOU'

for ch in str:
    if ch in vowels:
        count = count + 1

print('Number of Vowels in the String:', count)