#take input 
basic=int(input('Enter Basic Salary:'))

#given
da = 0.10 * basic
ta = 0.12 * basic
hra = 0.15 * basic

#calculate total salary
total_salary = basic + da + ta + hra

#display result
print(total_salary)
print("Basic Salary:", basic)
print("DA:", da)
print("TA:", ta)
print("HRA:", hra)
print(f'Total Salary of Employee is {total_salary}.')