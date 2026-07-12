#take inputs for a, b and c
a = float(input('Enter value of a:'))
b = float(input('Enter value of b:'))
c = float(input('Enter value of c:'))

#calculate discriminant
d = (b * b) - (4 * a * c)

#calculate roots
root1 = (-b + d**0.5)/(2*a)
root2 = (-b - d**0.5)/(2*a)

#display result
#print(root1)
#print(root2)
#print("First root:", root1)
#print("Second root:", root2)
print("First root is " + str(root1))
print("Second root is " + str(root2))
print(f'Roots of the Quadratic equation are {root1} and {root2}.')

