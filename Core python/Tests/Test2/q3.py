#A farmer has a field which is half circle shaped and the rest rectangle. He needs to do fencing for the entire field using barbed wire 5 times. The circular section has radius 20 m, and the rectangle length is 50 m and breadth is 40 m. If the cost of barbed wire is Rs 35/m, calculate the total cost of fencing the field.

import math

r = 20
length = 50
breadth = 40
rate = 35
rounds = 5

perimeter = (2 * length) + breadth + (math.pi * r)

total_cost = perimeter * rounds * rate

print("Perimeter of field =", perimeter)
print("Total fencing cost = Rs.", total_cost)