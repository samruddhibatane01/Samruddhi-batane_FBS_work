#with passing parameter (with input)
#without returing value (without parameters / arguments)
def addition(num1, num2):     #formal parameters / arguments

    sum = num1 + num2

    print(f'Addition of {num1} and {num2} is {sum}.')


n1 = int(input('Enter number 1:'))
n2 = int(input('Enter number 2:'))

addition(n1, n2)   #Actual parameters / arguments