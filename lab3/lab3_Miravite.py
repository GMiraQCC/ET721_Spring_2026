"""
Gabriel Miravite
Feb 3, 2026
"""


print("=========== Example 1: Setup of Conditional Statement ===========")
# conditional statements control the flow of the program
age = 11
if(age >= 21 and age <= 100):
    print("You are an adult!")
elif(age < 21 and age >= 12):
    print("You are a teen!")
elif(age < 12 and age > 0):
    print("You are a kid!")
else:
    print("Unable to read age")


print("\n=========== Example 2: For Loop ===========")
# for loop to print from 9 to 1, decrement of 1
for n in range(9, 0, -1):
    print(n)


print("\n=========== Example 3: For Loop in a List ===========")
numbers = [3,6,1,-8,9,-5]
count_negative = 0
for m in numbers:
    if m<0:
        count_negative += 1
else:
    print(f"There is/are {count_negative} negative numbers.")
# in a for-else code block, the else statement will run only after all the iterations in the for loop are complete
# I'm not sure that "else" is needed b/c the program runs the same w/o it


print("\n=========== Example 4: While Loop as a Counter ===========")
# while loop to print from -3 to 5, inclusive, increment of 2
# output --> -3 -1 1 3 5
x = -3
while x <= 5:
    print(x)
    x += 2


print("\n=========== Example 5: While Loop to Validate an Input ===========")
# program collects a number from the user, determines if the number is even/odd, then prints the result
# program asks if another number will be tested
# if user types 'y' or 'Y', the program runs again
# if user types any other character, the program will stop
decision_user = 'y'
user_number = 0

while True:
    user_number = int(input("Enter a number: "))
    if user_number%2 == 0 and user_number!=0:
        print(f"{user_number} is EVEN.")
    elif user_number == 0:
        print("The number is zero.")
    else:
        print(f"{user_number} is ODD.")
    
    decision_user = input("Do you want another run? Enter y or Y for yes: ")
    if decision_user != 'y' and decision_user != 'Y':
        break


print("\nEnd of Examples, Start of EXERCISES")


print("\n=========== EXERCISE 1: Validate a Number Between 1 & 9 ===========")
# Instructions: use 'while' loop to validate that the 'user_number' is between 1 and 9
while True:
    user_number = int(input("Enter a number between 1 and 9: "))
    if(user_number < 1 or user_number > 9):
        print(f"{user_number} is NOT a valid number between 1 and 9. Try again!")
    else:
        print(f"{user_number} is a valid number between 1 and 9. Thank you.")
        break

print("\n=========== EXERCISE 2: Guess the Number, Three Attempt Limit ===========")
# Instructions: use loop to allow the user to guess the number three times. If the user guesses the number before the third attempt, the program should end (break).
mystery_num = 5
for n in range(0, 3, 1):
    guess = int(input("Guess a number between 1 & 10: "))
    if(guess == mystery_num):
        print(f"You guessed correctly! The number is {mystery_num}.")
        break
    else:
        print("That is not the correct number. Try again! You have 3 tries in total.")