# Write all your codes for Day 3 here.
# COMMENT out the previous task before going on to the next task
# print("hello from day3")

import random
########################################################################
# Task 1:
# name = input ("What is your name? ")
# title = input ("What is your title? ")
# command = input ("What command do you want to give to your peasants? ")
# print (title + " " + name + " commands the peasants to " + command + "!")


# name = input ("What is your name? ")
# title = input ("What is your title? ")
# command = input ("What command do you want to give to your peasants? ")
# print (f"{title.capitalize()} {name} commands the peasants to {command}!")

########################################################################
# Task 2:
# name = "Leon"
# num_pens = 20
# print (name + " bought " + str (num_pens) + " pen(s)")

# Bonus:
# name = input ("What is your name? ")
# num_pens = input ("How many pens did you buy? ")
# print (name + " bought " + num_pens + " pen(s)")


# name = "Leon"
# num_pens = 20
# print (f"{name} bought {str (num_pens)} pen(s)")

# Bonus:
# name = input ("What is your name? ")
# num_pens = input ("How many pens did you buy? ")
# print (f"{name} bought {num_pens} pen(s)")

########################################################################
# Task 3:
# CalType = input ('Do you want addition (type "1"), subtraction (type "2"), multiplication (type "3) or division (type "4")? ')
# num1 = input ("What is your first number? ")
# num2 = input ("What is your second number? ")
# if CalType == "1":
#     print (f"{num1} + {num2} = {str (float (num1) + float (num2))}")
# elif CalType == "2":
#     print (f"{num1} - {num2} = {str (float (num1) - float (num2))}")
# elif CalType == "3":
#     print (f"{num1} * {num2} = {str (float (num1) * float (num2))}")
# elif CalType == "4":
#     print (f"{num1} * {num2} = {str (float (num1) / float (num2))}")

########################################################################
# Task 4:
# ItemList = []
# UnitList = []
# CostList = []
# TotalCost = 0
# done = "0"
# while done == "0":
#     item = input ("What item are you buying? (Singular noun) ")
#     unit = input (f"How many {item}s are you buying? ")
#     cost = int (unit) * random.randint (10, 1000) / 100
#     TotalCost = cost + TotalCost
#     cost = f"{cost:.2f}"
#     ItemList.append (item)
#     UnitList.append (unit)
#     CostList.append (cost)
#     done = input ("Is that all? (0 or 1) ")
#     print ()

# TotalCost = f"{TotalCost:.2f}"
# for i in range (len (ItemList)):
#     if UnitList [i] == "1":
#         print (f"The cost of the {ItemList [i]} is ${str (CostList [i])}.")
#     else:
#         print (f"The cost of the {UnitList [i]} {ItemList [i]}s is ${str (CostList [i])}.")

# if len(ItemList) != 1:
#     print (f"The total cost of all the items is ${TotalCost}.")

########################################################################
# Task 5:
# age1 = input ("What is Person A's age? ")
# age2 = input ("What is Person B's age? ")
# age1 = int (age1)
# age2 = int (age2)
# if age1 > age2:
#     print ("Person A is older that Person B.")
# elif age1 == age2:
#     print ("Person A is the same age as Person B.")
# else:
#     print ("Person B is older that Person A.")

########################################################################
# Task 6:
# real_password = "passme"
# for i in range (3):
#     user = input ("What is the password? ")
#     print ()
#     if user == real_password:
#         print ("Access Granted")
#         break
#     else:
#         print ("Access Denied")
#         if i == 2:
#             print ("System has been locked out.")
#             break
#         print ()
#         print ()

########################################################################
# Task 7:
# for i in range (10):
#     print (random.randint (1,100))

########################################################################
# Task 8:
# num1 = random.randint (1, 100)
# num2 = random.randint (1, 100)
# sum = num1 + num2
# user = int (input (f"What is {num1} + {num2}? "))
# if user == sum:
#     print ("You are smart.")
# else:
#     print ("Go and see the principal.")

########################################################################
# Additional exercises:

# Exercise 1:

# Write a program to ask the user to enter a password.

# If the password is correct, say "Access Granted"

# Else, say "Access Denied"

# The user is given a change to enter the password 3 times until the correct password is given.
# If the user fails the 3rd attempt, the program will say "System Locked. I call police."

# password = "passme"
# for i in range (3):
#     user = input ("What is the password? ")
#     if user == password:
#         print ("Access Granted")
#         break
#     else:
#         print ("Access Denied")
#         if i == 2:
#             print ("System Locked. I call police.")
#             break
#         print ("")

##############################################################################
# Exercise 2:

# Write a random number guesser game. in this game, the computer will 
# think of a number between 1 to 100 and the player will guess the number. 

# The player has 7 chances to guess the number.

# After each try, the computer will the player one of the following:
# 1. The player's guess is too big
# 2. The player's guess is too small
# 3. The player's guess is correct! (Game ends)

# If the player did not guess correctly after 7 times, 
# the program will tell the player the answer.

# num = random.randint (1, 100)
# for i in range (7):
#     user = int (input (f"What is your #{str (i + 1)} guess of the number? "))
#     if user == num:
#         print ("You're correct!")
#         break

#     if i == 6:
#         print (f"The number was {num}.")
#         break

#     if user < num:
#         print ("Your guess is too small.")
#     else:
#         print ("Your guess is too big.")
        
##############################################################################