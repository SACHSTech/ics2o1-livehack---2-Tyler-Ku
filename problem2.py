"""
-------------------------------------------------------------------------------
Name:   problem2.py
Purpose:  a description of your program
 
Author: Ku.T
 
Created:  03, 02, 2021
------------------------------------------------------------------------------
"""
#Greetings
print("Welcome to the Triangle Checker")

#User inputs
first_side = int(input("Enter the length of the first side: "))
second_side = int(input("Enter the length of the second side: "))
third_side = int(input("Enter the length of the third side: "))

#If statements bunched together
if first_side + second_side > third_side or second_side + third_side > first_side or third_side + first_side > second_side:
  print("The figure is a triangle.")

else:
  print("The figure is not a triangle.")