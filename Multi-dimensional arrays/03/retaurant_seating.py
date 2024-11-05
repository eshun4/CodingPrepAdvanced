"""
Your task is to write a piece of code that will transpose the given seating arrangement matrix. 
"""

def transposeRestaurantSeating(seatingArrangement):
    # one-liner transposition to be implemented
    return [[seatingArrangement[j][i] for j in range(len(seatingArrangement))] for i in range(len(seatingArrangement[0])) ]

# Example Seating Arrangement
original_seating = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# TODO: Call the function to transpose the seating and print each row of the transposed seating.

print(transposeRestaurantSeating(original_seating))