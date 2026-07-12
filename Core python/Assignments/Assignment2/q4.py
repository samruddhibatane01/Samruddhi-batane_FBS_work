#take inputs for height and base
height=float(input('Enter height of Triangle:'))
base=float(input('Enter base of Triangle:'))

#take inputs for length and breadth
length=float(input('Enter length of rectangle:'))
breadth=float(input('Enter breadth of rectangle:'))

#perform calculation
area_of_triangle = 0.5 * base * height
area_of_rectangle = length * breadth

#display result
print(area_of_triangle)
print(area_of_rectangle)
print(f'Area of Triangle is {area_of_triangle}.')
print(f'Area of Rectangle is {area_of_rectangle}.')