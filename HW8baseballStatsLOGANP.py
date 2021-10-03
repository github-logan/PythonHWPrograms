'''
FILE name: HW8baseballStatsLOGANP.py
CSC-171 Spring 2021
Programmed by: Logan P.
Date: 5.8.21


Program Description: Using the file WSWinner.txt, this program requests a date from the user
and provides the winning team of the World Series for that year. The user can make as many
requests as desired, and can finish looking up the trivia by typing "0". The program uses
a dictionary to retrieve this information from the text file, and adds entries for 1904 and
1994 when no series was held (entry = "Not Played"). When the user is finished, the program
creates a subset and displays the winners for the past 10 years (2009 - 2019).

'''

def main():
    instructions()
    worldSeriesDic = createNewDictionary()
    reportTrivia(worldSeriesDic)
    createDictionarySubset(worldSeriesDic)

def instructions():
    print('''You can use this program to select a year between 1903 and 2019 to display
the team that won the World Series for that year.
When you are finished looking up teams, you can type "0".''')
    print()

def createNewDictionary():
    infile = open('WSWinners.txt', 'r') #input from file
    WSDict = {} #creates empty dictionary
    for line in infile:
        key, value = line.rstrip().split(',')
        WSDict[key] = value
    infile.close()
    WSDict['1904'] = 'Not Played.' #adds entries for years without game
    WSDict['1994'] = 'Not Played.'
    return WSDict

def reportTrivia(worldSeriesDic): #output from dictionary based on user input/response
    choice = input('''Select a year between 1903 - 2019. Note that the World Series was not
played in 1904 and 1994.
Type "0" when you are finished looking up trivia: ''')
    while choice != '0':
        print('The winner for the World Series were the: ' + worldSeriesDic[choice])
        print()
        choice = input('''Select another year or type "0" if you're finished: ''')
    if choice == '0':
        print('The Winners for 2009 - 2019 were: ')

def createDictionarySubset(worldSeriesDic): #pulls info from full dictionary to make the recent winners listing
    mainDictionary = worldSeriesDic
    pastDecade = ['2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
    subSet = {k:v for k,v in mainDictionary.items() if k in pastDecade}
    print(subSet)


main ()
