# File: HWRecipeLOGANP.py
# Programmer: Logan P.
# Date: 2.26.21

# Description: This program provides recipe conversion for select ingredients
# for a sugar cookie recipe. The program needs to ask the user to input the
# desired number of cookies (in dozens) that they would like to make, and
# the program should display the required amounts of Flour, Sugar and Butter
# necessary (increasing or decreasing as needed) based on the standard
# ingredient requirements for 4 dozen cookies.

# Get user input for desired amount of cookies in dozens.
userBatch = int(input("How many dozens of sugar cookies would you like to make: "))

# Calculate total number of cookies to be made.

totalCookies = int(userBatch * 12)

# Calculate "multiplier" -- how many times more or less desired dozens amount
# (ie. user batch) is compared to standard amount (ie. user desires 8 dozens,
# this is 2 times more than 4).

standardBatch = 4
multiplier = float(userBatch/standardBatch)

# Calculate necessary increases or decreases in ingredient amounts.
# Ingredients are measured in cups, cups and tablespoons for flour, sugar and
# butter, respectively.

standardFlour = 2.75
userFlour = float(multiplier * standardFlour)
standardSugar = 1.25
userSugar = float(multiplier * standardSugar)
standardButter = 8
userButter = int(multiplier * standardButter)

# Report total number of cookies to be made and the necessary ingredients to do so.
print()
print("To make {0:d} cookies, you will need the following ingredients:".format(totalCookies))
print("{0:.2f} cups of flour".format(userFlour))
print("{0:.2f} cups of sugar".format(userSugar))
print("{0:d} tablespoons of butter".format(userButter))
