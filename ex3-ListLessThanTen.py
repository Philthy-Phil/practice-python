a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x = []
ui = "\n*************************"

print("Given list of numbers: ", a)
print(ui)

for num in a:
    if (num < 5):
        print(num, end=", ")
print(ui)

for num in a:
    if (num < 5):
        x.append(num)
print("here are all the numbers < 5: ", x)

print(ui)

usrnum = int(input("what's your number? "))
ulist = []
for num in a:
    if(num < usrnum):
        ulist.append(num)
print("here are all the numbers from a, which are smaller than your input: ", ulist)
