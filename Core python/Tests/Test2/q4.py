#Write a program to calculate the total cost of painting the interior of a building with four equal sized walls.

area = float(input("Enter area of one wall: "))
cost = float(input("Enter painting cost per unit area: "))

total = 4 * area * cost
print("Total painting cost =", total)