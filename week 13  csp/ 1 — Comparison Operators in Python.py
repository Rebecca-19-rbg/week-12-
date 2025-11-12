# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3
b = 4

print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= b)   # False
print(a <= b)   # True


#predict the output of the following comparisons:
10 > 5            # True
7 == 2 * 3 + 1    # True
8 != 8            # False
4 <= 2 + 2        # True

# Write 3 examples that result in True and 3 that result in False.

10 > 5
7 * 2 <= 10 + 16
10 == 5 * 2

9 != 9
7 >= 5
11 == 10

# Create a simple grade-checking condition:

# practice problem :
# where a student must check if their score is greater than or equal to 60 to pass a test.# The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"

user = input("What is your username? ")

print("Hello,", user)

# asking for valid password

password = input("What is your password? ")


if len(password) >= 8 and any(char.isdigit() for char in password):
  print("Password is valid.")
else:
     print("Password is invalid. ")

# asking for students score 

grade = int(input("What was your score on the test? "))

if grade >= 90 and grade <= 100:
    print("Congrats, you got an A!")
elif grade >=80 and grade <=89:
    print("You got a B!")
elif grade >=70 and grade <=79:
    print("You got a C")
elif grade >=60 and grade <=69:
    print("You got a D.")
else:
    print("You failed, try again.")


