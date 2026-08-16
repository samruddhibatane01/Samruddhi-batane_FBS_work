def leap_year(year):
    if year % 400 == 0:
        print('Year Is Leap Year')
    elif year % 100 == 0:
        print('Year Is Not Leap Year')
    elif year % 4 == 0:
        print('Year Is Leap Year')
    else:
        print('Year Is Not Leap Year')

y = int(input('Enter year:'))

leap_year(y)