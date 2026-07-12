#take inputs for hours, minutes and seconds
hours=int(input('Enter hours:'))
minutes=int(input('Enter minutes:'))
seconds=int(input('Enter seconds:'))

#perform calculation
total_seconds = (hours * 3600) + (minutes * 60) + seconds

#display result
print(total_seconds)
print("Total Seconds:", total_seconds)
print("Total Seconds are " + str(total_seconds))
print(f'Total Seconds are {total_seconds}.')