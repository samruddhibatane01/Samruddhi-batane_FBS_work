#take input 
num=int(input('Enter a three-digit number:'))

#perform calculation
d1 = num % 10
num = num // 10

d2 = num % 10
num = num // 10

d3 = num % 10
num = num // 10

reverse = d1 * 100 + d2 * 10 + d3

#display result
print(f'Reverse three-digit number is {reverse}.')