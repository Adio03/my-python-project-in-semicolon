import datetime

year =int(input("enter your birth year: "))
currentYear= datetime.datetime. now()
current = currentYear.year - year
print(current)