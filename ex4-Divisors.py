__author__ = 'phil.ezb'

num = int(input("type in a number: "))
numRange = range(1, num + 1)
noRemainders = []

for n in numRange:
    if (num%n == 0):
        noRemainders.append(n)

print(f'valid possible divisors for {num}:\n',noRemainders)
