n = int(input('How many Fibonacci numbers you want:'))
a = -1
b = 1

for i in range(n):
    c = a + b
    print(c)

    a=b
    b=c