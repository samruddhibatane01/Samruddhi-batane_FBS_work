#Write a program to accept basic salary of n employees (n accepted from user). If basic salary is below 20000 then DA=10%, TA=12% and HRA=15%, otherwise DA=15%, TA=18% and HRA=20%. Calculate the total salary of each employee and also the total salary of all employees.

n = int(input("Enter number of employees: "))

total_salary_all = 0

for i in range(n):
    basic_salary = float(input(f"Enter basic salary of employee {i + 1}: "))

    if basic_salary < 20000:
        da = basic_salary * 10 / 100
        ta = basic_salary * 12 / 100
        hra = basic_salary * 15 / 100
    else:
        da = basic_salary * 15 / 100
        ta = basic_salary * 18 / 100
        hra = basic_salary * 20 / 100

    total_salary = basic_salary + da + ta + hra
    total_salary_all += total_salary

    print(f"Total salary of employee {i + 1} = {total_salary}")

print(f"Total salary of all employees = {total_salary_all}")