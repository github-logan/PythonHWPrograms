'''FILE name: HWsummerRdgLOGANP.py
CSC-171 Spring 2021
Programmed by: Logan P.
Date: 4.18.21
Program Description: This program opens a summer reading list file and displays
it for the user. Then it re-opens the file for writing and adds three more books
to the list (appending them to the end). Next, it prompts the user to indicate when
they are ready to view the updated list (this way both lists don't just appear
super fast all at once). Finally, it displays the updated list to the user.
'''

def main():
    file = "summerReading.txt"
    print('Current Summer Reading List:\n')
    displayWithForLoop(file)
    addTitles(file)
    print('\r')
    userPrompt = checkToProceed()
    displayUpdatedList(file)

def displayWithForLoop(file):
    infile = open(file, 'r')
    for line in infile:
        print(line, end="")
    infile.close()

def addTitles(file):
    outfile = open(file, 'a')
    logansBooks = ["Dracula\n", "Harry Potter\n", "White Fang\n"]
    outfile.writelines(logansBooks)
    outfile.close()

def checkToProceed():
    confirm = input('Type "1" when you are ready to view the updated list: ')
    while confirm != '1':
        confirm = input('\nType "1" when you are ready to view the updated list: ')
    else:
        print('\nUpdated Summer Reading List:\n')


def displayUpdatedList(file):
    infile = open(file, 'r')
    for line in infile:
        print(line, end="")
    infile.close()


main ()
