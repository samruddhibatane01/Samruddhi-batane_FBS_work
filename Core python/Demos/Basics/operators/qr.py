#take input for dividend and divisor
Dividend=int(input('Enter Dividend:'))
Divisor=int(input('Enter Divisor:'))

#perform calculation
Q=Dividend//Divisor
R=Dividend%Divisor

#display result
print(f'Quotient is: {Q}, Remainder is: {R}.')
