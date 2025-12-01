#EXAMPLES 

fruits =     ("apples", "oramge", "banana", "coconut")
vegetables = ("celery", "carrots", "potatoes")
meats =      ("chicken", "fish", "turkey")

groceries = (fruits, vegetables, meats)

print(groceries[2][2])
print(groceries[2][1])

for collection in groceries:
    for food in collection:
        print(food)


num_pad = (1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#")

for row in num_pad:
    for num in row:
        print(num, end="")
    print()



# Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(matrix[1][2])    # 6

# # List comprehension
# first_col = [row[0] for row in matrix]
# print(first_col)       # [1, 4, 7]



# Practice Problems:

# Build a matrix variable containing 3 lists of 3 numbers each.
list1 = (3, 2, 1)
list2 = (6, 5, 4)
list3 = (9, 8, 7)

matrix_examp = (list1, list2, list3)


# Print the first list.
print(matrix_examp[0])

# Print the second item from the third list.
print(matrix_examp[2][1])

# Use a list comprehension to extract the last item from each sub-list.
last_item = [row[2] for row in matrix_examp]
print(last_item)

# Challenge: Create a new list containing squares of numbers from 1–10 using a comprehension.

squares = [x**2 for x in range (1,11)]
print(squares)
