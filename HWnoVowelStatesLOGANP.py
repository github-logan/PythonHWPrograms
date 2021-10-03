'''FILE name: HWnoVowelStatesLOGANP.py
CSC-171 Spring 2021
Programmed by: Logan P.
Date: 5.2.21

Program Description: This program opens a file 'States.txt' and prepares a new file which is temporarily named
'noVowelStates.txt' but will later be updated to 'States.txt' replacing the original file. Once the file is opened
the program looks for all states that begin with a vowel and writes them to the new file. Then the program deletes
the original file and replaces it with the new file that only contains the states which begin with a vowel. To confirm
that the program ran, the updated list of states is displayed for the user.
'''


import os

def main():
    file = "States.txt"
    removeNoVowelStates()
    removeReplaceOldFile()
    displayUpdatedFile(file)

#input: retrieve list of states; process: identify states that begin with vowel; Note: 'Y' is not included in vowel
# list because a) no states start w/ 'Y' and b) if one did, 'Y' would be acting as a consonant and not a vowel
def removeNoVowelStates():
    vowel = ('A', 'E', 'I', 'O', 'U')
    infile = open("States.txt", 'r')
    outfile = open("noVowelStates.txt", 'w')
    for state in infile:
        if state.startswith(vowel):
            outfile.write(state)
    infile.close()
    outfile.close()

#output: delete and replace old file with the new file containing the list of states that begin with a vowel
def removeReplaceOldFile():
    os.remove("States.txt")
    os.rename("noVowelStates.txt", "States.txt")

#display contents of file to user to confirm program ran correctly
def displayUpdatedFile(file):
    infile = open(file, 'r')
    for line in infile:
        print(line, end="")
    infile.close()


main()
