"""
Great work so far! Now, let's bring everything together. 
You're involved in the management of an apartment building. 
Your task is to create a representation of an apartment building
in code, update the name of one apartment, and then print the
updated building, floor by floor. Use multidimensional arrays and loop through them for this task.

In this exercise, we will continue to explore multidimensional arrays using Python.

"""

# TODO: Create a multidimensional list representing an apartment building with 3 floors
# and 3 apartment units on each floor.

apartment_buildings = [
    ["Apt 101", "Apt 102", "Apt 103"],
    ["Apt 201", "Apt 202", "Apt 203"],
    ["Apt 301", "Apt 402", "Apt 303"],
]

# TODO: Update the name of one of the apartments to "Vacant".
apartment_buildings[2][2] = "Vacant"

# TODO: Print out all the apartment names in the building, one floor at a time.
for floor in apartment_buildings:
    for apt in floor:
        print(apt, end=" ")
        