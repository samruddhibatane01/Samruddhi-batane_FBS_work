#take input for 5 subjects
sub1=int(input('Enter marks of Maths:'))
sub2=int(input('Enter marks of Science:'))
sub3=int(input('Enter marks of English:'))
sub4=int(input('Enter marks of History:'))
sub5=int(input('Enter marks of Marathi:'))

#perform calculation
total_marks=sub1 + sub2 + sub3 + sub4 + sub5
percentage=(total_marks/400)*100

#display result
print(total_marks)
print(percentage)
print("Total marks:",total_marks)
print("Percentage:",percentage)
print("Total marks are " + str(total_marks))
print("Percentage is " + str(percentage))
print(f'Total marks are {total_marks}.')
print(f'Percentage is {percentage}%.')
