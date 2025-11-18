# ### Joaquin Flores, Rebecca Love 

list1 = {"joaquin", "rebecca", "jon", "jay", "julian", "joe", "lexi", "joe"}

numbers = [10, 8, 6, 3, 7, 11, 5]

for number in numbers:
    if number >= 0 and number <= 5:
        print(f"student is OK")
    elif number >= 6 and number <= 10:
        print(f"student gets a WARNING")
    else:
        print(f"student is FLAGGED")

name = input("What is your name? ")

minutes = 0 

if name in list1:
    minutes = int(input("How many minutes were you gone for? "))

    if minutes >= 0 and minutes <= 5:
        print((name), "is OK")
    elif minutes >= 6 and minutes <= 10:
        print((name), "gets a WARNING")
    else:
        print((name), "is FLAGGED")
else:
    print("Your name is not in the list")

if minutes > 10:
    print("Student has an automatic flag.")

average = sum(numbers) / len(numbers)
print("The average time in the hallway is:", average, "based on the original list.")

maxi = max(numbers)
print("The maximum time in the hallway is", maxi, "minutes based on the original list.")


