#take inputs for two numbers
num1=int(input('Enter First Number:'))
num2=int(input('Enter Second Number:'))

#swappig using third value
temp = num1
num1 = num2
num2 = temp

#display result
print(f'Before Swapping: num1 = {num1}, num2 = {num2}. ')
print(f'After Swapping: num1 = {num2}, num2 = {num1}.')