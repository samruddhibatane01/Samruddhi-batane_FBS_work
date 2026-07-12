#take input for radius of a circle
radius=int(input('Enter radius of circle:'))

#perform calculation
area= 3.14 * radius * radius
circumference= 2 * 3.14 * radius

#display result
print(area)
print(circumference)
print("Area of Circle:", area)
print("Circumference of Circle:", circumference)
print("Area of Circle is " + str(area))
print("Circumference of Circle is " + str(circumference))
print(f'Area and Circumference of Circle are {area} and {circumference}.')