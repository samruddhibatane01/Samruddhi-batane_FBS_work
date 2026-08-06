print('Prime numbers from 1 to 100 are:')
for num in range(1, 101):
    if(num > 1):
        prime = 1

        for i in range(2, num):
            if(num % i == 0):
                prime = 0
                break

        if(prime == 1):
            print(num)