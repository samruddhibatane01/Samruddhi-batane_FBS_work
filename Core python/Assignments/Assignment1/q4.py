#take inputs for P, T and R
p=int(input('Enter Principal amount:'))
t=int(input('Enter Time:'))
r=int(input('Enter rate of interest:'))

#perform calculation
SI=(p*t*r)/100

#display result
print(SI)
print("Simple Interest:", SI)
print("Simple Interest is " + str(SI))
print(f'Simple Interest is {SI}.')