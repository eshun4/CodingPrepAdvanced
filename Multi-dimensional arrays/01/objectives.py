"""
This section deep-dives into multi-dimensional arrays in Python.

Navigate their creation.
How to Modify and access them.
Explore the common syntax associated with these structures.

Re-visit nested loops, with break and continue statments.

# Creating a 2D array

array = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# We access array elements using indices
print(array[1][0]) #Outputs: 4

# Array indices in python are zero-based.

# Updating an element
array[0][1] = 'New Code'

# Finding the number of rows
num_floors = len(array)
Output = 3

# Adding a new row to our array
array.append(['Unit-1', 'Unit-2', 'Unit-3'])

# removing an element
array[1].remove('New Code')

# Traversing a multi-dimensional array

array = [["Apt 101", "Apt 102", "Apt 103"], 
         ["Apt 201", "Exit Floor", "Apt 203"], 
         ["Apt 301", "Apt 302", "Apt 303"]]
# Loop through 2D array
for floor in array:
    for unit in floor:
        print(unit, end =', ')
    print()

Prints:
Apt 101, Apt 102, Apt 103, 
Apt 201, Exit Floor, Apt 203, 
Apt 301, Apt 302, Apt 303, 


# Break in nested loop
for floor in array:
    for unit in floor:
        if unit == 'Exit Floor':
            break
        print(unit, end =', ')
    print()

Prints:
Apt 101, Apt 102, Apt 103, 
Apt 201, 
Apt 301, Apt 302, Apt 303, 


# Continue in nested loop
for floor in array:
    for unit in floor:
        if unit == 'Exit Floor':
            continue
        print(unit, end =', ')
    print()
"""
