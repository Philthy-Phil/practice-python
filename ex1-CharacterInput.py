import datetime

name = input("what's ur name? ")
age = int(input("what's ur age? "))
set_year = 100
end_year = str(datetime.datetime.now().year + set_year - age)
num = int(input("what's your lucky number? "))

print(num*f"{name}, you'll turn {set_year} years old in {end_year}.\n")
