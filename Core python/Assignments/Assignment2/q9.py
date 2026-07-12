#take input for two numbers
num1=int(input('Enter First Number:'))
num2=int(input('Enter Second Number:'))

#swapping without third variable
#python technique
num1, num2 = num2, num1

#display result
print(f'Before swapping: num1 = {num1}, num2 = {num2}.')
print(f'After swapping: num1 = {num2}, num2 = {num1}.')