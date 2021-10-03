# File: HWgamesWithTiesLOGANP.py
# Programmer: Logan P.
# Date: 2.16.21

#Description: Revising the program for a team's winning percentage
# calucation to include possibilities for sports that allow games
# to end in ties. The program needs to ask the user for the team
# name, and the number of games won, lost and tied. The program should
# display the name of the team and its percentage of games won.

#Get user input for the name of team and its competition data (ie.
# games won, lost and tied).

teamName = input("What is the team's name? ")
gamesWon = int(input("How many games did the team win? "))
gamesLost = int(input("How many games did the team lose? "))
gamesTied = int(input("How many games ended in a tie? "))


#Calculate the winning percentage.

winningPercentage = (gamesWon + (gamesTied / 2))/(gamesWon + gamesLost + gamesTied)


#Report the team's winning percentage back to the user.
print()
printReport = "The " + teamName + " have a {0:5.2%} winning average"
print(printReport.format(winningPercentage))
