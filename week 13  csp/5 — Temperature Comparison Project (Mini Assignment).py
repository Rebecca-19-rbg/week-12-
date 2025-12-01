# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.



# Prints whether it’s cold, warm, or hot using comparison operators.



# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:

temp = float(input("What is today's tempurature? "))

if temp >= -10 and temp < 51:
    print("It's cold")
elif temp >= 50 and temp < 81:
    print("It's warm")
elif temp >= 80  and temp < 111:
    print("It's hot")

if temp < -10 or temp > 110:
    print("Extreme temperature warning!")

