"""
-------------------------------------------------------------------------------
Name:   problem1.py
Purpose:  Check for number of antennae and number of eyes to decide what type of alien is found on Mars
 
Author: Ku.T
 
Created:  03, 02, 2021
------------------------------------------------------------------------------
"""
#Input here
number_of_antenna = int(input("How many antenna does the alien have?: "))
number_of_eyes = int(input("How many eyes does the alien have?: "))

#If statements run through
if number_of_antenna <= 2 and number_of_eyes <= 3:
  print("Life form detected: BrooklynMartian")

if number_of_antenna >= 3 and number_of_eyes <= 4:
  print("Life form detected: AudreyMartian")

if number_of_antenna == 0 and number_of_eyes == 2:
  print("Lifeform detected: MattDamonMartian")

if number_of_antenna <= 6 and number_of_eyes >= 2:
  print("Life form detected: MaxMartian")

else:
  print("Life form not found")