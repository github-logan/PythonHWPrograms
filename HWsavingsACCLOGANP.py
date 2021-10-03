'''FILE name: HWsavingsACCLOGANP.py
CSC-171 Spring 2021
Programmed by: Logan P.
Date: 4.17.21
Program Description: This "Savings Account" program requests the user to input
their current savings account balance and the desired amount of money to be
withdrawn. The program calculates what the new balance would be if the withdrawal
is accepted (ie.the new balance is a positive number), and then displays to the
user their new balance or that the withdrawal has been denied. The program loops
until the user no longer desires to make a transaction. If the new (final) balance
is less than $150, the user is also informed, before the program ends.
'''


def main():
    currentBalance = float(input('Enter current balance: ')) #obtain balance info from user
    amountWithdrawn = float(input('Enter amount of withdrawal: ')) #obtain withdrawal info from user
    function1 = newBalance(currentBalance, amountWithdrawn)
    function2 = transactionLoop(function1)

def newBalance(x, y):
#calculate new balance based on inputs
    newBalance = x - y
    if y > x:
        print('Withdrawal denied.')
    else:
        x = newBalance
        print(f'The new balance is: ${x:,.2f}.')
    return x

def transactionLoop(updatedBalance):
#determine if additional transactions are desired by user
    currentBalance = updatedBalance
    proceed = str(input('Would you like to make another transaction? Y or N: '))
    userResponse = proceed.upper()
#while loop for main process
    while userResponse.startswith('Y'):
        newWithdrawal = float(input('Enter amount of withdrawal: '))
        if newWithdrawal > currentBalance:
            print('Withdrawal denied.')
            proceed = str(input('Would you like to change your withdrawal amount? Y or N: '))
            userResponse = proceed.upper()
        else:
            newBalance = currentBalance - newWithdrawal
            currentBalance = newBalance
            print(f'The new balance is: ${currentBalance:,.2f}.')
            if newBalance == 0:
                userResponse = ('no')
            else:
                proceed = str(input('Would you like to make another withdrawal? Y or N: '))
                userResponse = proceed.upper()
#final output
    else:
        print(f'Thank you. Your final balance is ${currentBalance:,.2f}. Have a nice day.')
        if currentBalance < 150:
            print('Low Balance Warning: Your balance is below $150.')


main()
