l1 = ['apple', 'banana', 'apple', 'mango', 'banana', 'apple']

unique_words = set(l1)
print('Unique Words:', unique_words)

for word in unique_words:
    print(word, ':', l1.count(word))