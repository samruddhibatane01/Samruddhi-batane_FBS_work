cp=int(input('Enter Cost Price:'))
sp=int(input('Enter Selling Price:'))

if(sp > cp):
    Profit = sp - cp
    print(f'Profit: {Profit}.')
elif(cp > sp):
    Loss = cp - sp
    print(f'Loss: {Loss}.')
else:
    print('No Profit and No Loss.')
