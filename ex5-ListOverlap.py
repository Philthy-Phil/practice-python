__author__ = 'phil.ezb'

import random

# hard coded lists
# list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# random num list
list_a = random.sample(range(0, 100), 20)
list_b = random.sample(range(0, 100), 20)

# set() to prevent duplicates
list_total = set(list_a + list_b)
list_common = []

# loop through total and compare
for num in list_total:
    if (num in list_a) and (num in list_b):
        list_common.append(num)

# output
print(list_common)
