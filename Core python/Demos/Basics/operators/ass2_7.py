#find the sum of three-digits number.
num=379
#temp = num  #to store original number

d1 = num % 10
num = num // 10
print(num)

d2 = num % 10
num = num // 10
print(num)

d3 = num % 10
num = num // 10
print(num)

sum = d1 + d2 + d3
print(sum)