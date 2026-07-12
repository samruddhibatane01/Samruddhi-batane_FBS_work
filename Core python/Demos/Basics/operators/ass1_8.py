#Write a program to convert days into years, weeks and days
#take input for days
days=int(input('Enter days:'))

#perform calculation
years=days//365
#print(years)
days=days%365
#print(days)

weeks = days//7
#print(weeks)
days=days%7
#print(days)

#display result
print(f'Years:{years}, Weeks:{weeks}, Days:{days}.')