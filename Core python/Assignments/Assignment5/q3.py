n = int(input('Enter number of passengers:'))
cost = int(input('Enter ticket cost:'))

i = 1
total = 0
while(i <= n):
    print('Passenger', i)

    age = int(input('Enter age:'))
    
    if(age < 12):
        amount = cost - (cost * 30 / 100)
    elif(age > 59):
        amount = cost - (cost * 50 / 100)
    else:
        amount = cost
    print('Ticket amount = ', amount)

    total = total + amount
    i = i + 1

print('Total amount =', total)