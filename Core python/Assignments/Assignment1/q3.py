#take inputs for two numbers
num1=int(input('Enter first number:'))
num2=int(input('Enter second number:'))

#perform calculation
quotient = num1 // num2
remainder = num1 % num2

#display result
print(quotient)
print(remainder)
print("Quotient:", quotient)
print("Remainder:", remainder)
print("Quotient is " + str(quotient))
print("Remainder is " + str(remainder))
print(f'Quotient and Remainder is {quotient} and {remainder}.')