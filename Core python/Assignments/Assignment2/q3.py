#take input for feets and inches
feets=float(input('Enter distance in feets:'))
inches=float(input('Enter distance in inches:'))

#converts feets in inches
inches=inches+(feets*12)
#convert inches in centimeters
centimeters=inches*2.54
#find meters and centimeters
meters = centimeters // 100
centimeters = centimeters % 100

#display result
print(meters)
print(centimeters)
print(f'Distance is {meters}m and {centimeters}cm.')
