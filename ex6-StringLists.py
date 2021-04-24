__author__ = 'phil.ezb'

txt = input("Enter something: ")
revtxt = txt[::-1]

print(f'entered: {txt}')
print(f'reversed: {revtxt}')

if(txt == revtxt):
    print("hey it's a palindrom!")
else:
    print("sry this isn't a palindrom!")
    