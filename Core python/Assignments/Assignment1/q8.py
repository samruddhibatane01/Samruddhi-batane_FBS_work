#take input for days
days = int(input('Enter number of days:'))

#Calculate years, weeks and days
years = days // 365
days = days % 365
weeks = days // 7
days = days % 7

#display result
print(years)
print(weeks)
print(days)
print("Years:", years)
print("Weeks:", weeks)
print("Days:", days)
print("Years are " + str(years))
print("Weeks are " + str(weeks))
print("Days are " + str(days))
print(f'Years:{years}, Weeks:{weeks} and Days:{days}.')