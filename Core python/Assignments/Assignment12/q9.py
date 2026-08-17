str = input('Enter a string: ')

words = str.split()
word_count = len(words)

char_count = len(str.replace(' ', ''))

print('Number of Words:', word_count)
print('Number of Characters:', char_count)