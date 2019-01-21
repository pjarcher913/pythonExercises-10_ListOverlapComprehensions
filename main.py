# Created by:   Patrick Archer
# Date:         20 January 2019
# Copyright to the above author. All rights reserved.

"""

Directions - COMPLETE
Randomly generate two lists and write a program that returns a list that contains only the elements that are common
between the lists (without duplicates).

"""

import random

# ################################################# start_funcs

def commonElementFinder(list1, list2):

    commonElementsList = []

    for y in range(len(list1)):
        for z in range(len(list2)):
            # check if the selected elements' values in the two lists are equivalent
            if (list1[y] == list2[z]):
                # check if common value is already present in the results list or not
                if list1[y] not in commonElementsList:
                    commonElementsList.append(list1[y])

    # sort list to be ascending
    commonElementsList.sort()

    return commonElementsList

# ################################################# end_funcs/start_main

msg = "randomly generate two lists and write a program that returns a list that contains only the elements that are" \
      "common between the lists (without duplicates)."

print("This application " + msg)

# generate a random integer between 1 and 100 to determine list sizes
listSize_a = random.randint(1, 25)
listSize_b = random.randint(1, 25)
randIntRange = random.randint(1, 100)

# initialize lists to prepare for randomization protocols
a = []
b = []

for n1 in range(1, listSize_a):
    a.append(random.randint(1, 100))
for n2 in range(1, listSize_b):
    b.append(random.randint(1, 100))

# returns a list that contains only the elements that are common between the lists
resultingList = commonElementFinder(a, b)
resultingList.sort()

print("\nList A: ")
print(a)
print("\nList B: ")
print(b)
print("\nValues Contained in Both Lists: ")
print(resultingList)

# ################################################# end_main



