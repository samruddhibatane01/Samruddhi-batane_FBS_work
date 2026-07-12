#take input 
num=int(input('Enter a three-digit number:'))

#perform calculation
d1 = num % 10
num = num // 10

d2 = num % 10
num = num // 10

d3 = num % 10
num = num // 10

sum_of_digits = d1 + d2 + d3

#display result
print(sum_of_digits)
print(f'The Sum of three-digit number is {sum_of_digits}. ')