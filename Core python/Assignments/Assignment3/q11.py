totalprice = 0

age1 = int(input('Enter the age of first person:'))
tkprice1 = float(input('Enter the Ticket Price of first person:'))
 
if (age1 < 12):
    totalprice = totalprice + (tkprice1 * 0.70)
elif(age1 > 59):
    totalprice = totalprice + (tkprice1 * 0.50)
else:
    totalprice = totalprice + tkprice1
#first person ends here


age2 = int(input('Enter the age of Second person:'))
tkprice2 = float(input('Enter the Ticket Price of second person:'))

if (age2 < 12):
    totalprice = totalprice + (tkprice2 * 0.70)
elif(age2 > 59):
    totalprice = totalprice + (tkprice2 * 0.50)
else:
    totalprice = totalprice + tkprice2
#second person ends here


age3 = int(input('Enter the age of Third person:'))
tkprice3 = float(input('Enter the Ticket Price of third person:'))

if (age3 < 12):
    totalprice = totalprice + (tkprice3 * 0.70)
elif(age3 > 59):
    totalprice = totalprice + (tkprice3 * 0.50)
else:
    totalprice = totalprice + tkprice3
#third person ends here


age4 = int(input('Enter the age of Fourth person:'))
tkprice4 = float(input('Enter the Ticket Price of fourth person:'))

if (age4 < 12):
    totalprice = totalprice + (tkprice4 * 0.70)
elif(age4 > 59):
    totalprice = totalprice + (tkprice4 * 0.50)
else:
    totalprice = totalprice + tkprice4
#fourth person ends here


age5 = int(input('Enter the age of Fifth person:'))
tkprice5 = float(input('Enter the Ticket Price of fifth person:'))

if (age5 < 12):
    totalprice = totalprice + (tkprice5 * 0.70)
elif(age5 > 59):
    totalprice = totalprice + (tkprice5 * 0.50)
else:
    totalprice = totalprice + tkprice5
#fifth person ends here

print(f'Total price to pay for a Trip of five people is {totalprice}.')
