# Write all your codes for Day 4 here.
# COMMENT out the previous task before going on to the next task
# print("hello from day4")

import random
########################################################################
# Task 1a:
# counter = 0
# while counter <= 9:
#     print (counter)
#     counter += 1

# Task 1b:
# counter = 5
# while counter <= 32:
#     print (counter)
#     counter +=1

# Task 1c:
# counter = 50
# while counter >= 1:
#     print (counter)
#     counter -= 1

########################################################################
# Task 2:
# def lose():
#     print ("You have no more lives left, you lose.")
#     exit()

# def wrong():
#     print ("That's wrong.")
#     print (f"You have {str (lives)} live(s) left.")
#     print ()

# r1 = "needle"
# lives = 15
# user = ""
# print ("For all answers, use lowercase letters, and the answer is always a single word.")
# print (f"You have {str (lives)} lives.")
# print ("0/5 Riddles.")
# print ()
# while not user == r1:
#     user = input ("Riddle 1: What has an eye, but cannot see? ")
#     if not user == r1:
#         lives -= 1
#         if lives == 0:
#             lose ()
        
#         wrong ()

# print ("That's correct!")
# r2 = "sponge"
# print ("1/5 Riddles.")
# print ()
# while not user == r2:
#     user = input ("Riddle 2: What is full of holes but still holds water? ")
#     if not user == r2:
#         lives -= 1
#         if lives == 0:
#             lose ()
        
#         wrong ()

# print ("That's correct!")
# r3 = "egg"
# print ("2/5 Riddles.")
# print ()
# while not user == r3:
#     user = input ("Riddle 3: What has to be broken before you can use it? ")
#     if not user == r3:
#         lives -= 1
#         if lives == 0:
#             lose ()
        
#         wrong ()

# print ("That's correct!")
# r4 = "river"
# print ("3/5 Riddles.")
# print ()
# while not user == r4:
#     user = input ("Riddle 4: What runs but never walks, has a mouth but never talks, has a head but never weeps, and has a bed but never sleeps? ")
#     if not user == r4:
#         lives -= 1
#         if lives == 0:
#             lose ()
        
#         wrong ()

# print ("That's correct!")
# r5 = "cold"
# print ("4/5 Riddles.")
# print ()
# while not user == r5:
#     user = input ("Riddle 5: What can you catch but not throw? ")
#     if not user == r5:
#         lives -= 1
#         if lives == 0:
#             lose ()
        
#         wrong ()

# print ("5/5 Riddles.")
# print ("You won!")

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