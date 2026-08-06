n = int(input('Enter number of students:'))
total_per = 0
for i in range(1, n + 1):
    print('Student', i)

    sum = 0
    for j in range(1, 6):
        marks = int(input('Enter marks of subject' + str(j) + ':'))
        sum = sum + marks

    per = sum / 5
    print('Percentage of student', i, '=', per)

    total_per = total_per + per

avg = total_per / n
print('\nAverage percentage of all students = ', avg)