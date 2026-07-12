#take input for P, T and R
p=int(input('Enter Principal amount:'))
t=int(input('Enter Time:'))
r=int(input('Enter Rate of Interest:'))

#perform calculation
amount = p*(1 + (r/100))**t
CI = amount - p

#display result
print(CI)
print("Compound Interest:", CI)
print("Compound Interest is " + str(CI))
print(f'Compound Interest is {CI}.')