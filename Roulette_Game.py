#Importing needed libraries
import random

#Terminating Progrmam Variables
Continue = True

#Global Variables
AmountOfBets = int
UserInput = int
roll = int
MoneyBetAmount = int
SingleBetNumber = int
CustomNumberInput = int
WinBalance = int
TotalBalance = 1000
counter = 1
isWin = False
UserInputLoop = True
SingleBetLoop = True
MoneyBetLoop = True
ContinueLoop = True
CustomInputLoop = True
ListInputLoop = True
CustomForLoop = True
Custom=[]

#Variables for bet selection
BetSelectionGreen = 1
BetSelectionRed = 2 
BetSelectionBlack = 3
BetSelctionEven = 4
BetSelectionOdd = 5
BetSelectionLowBet = 6
BetSelectionHighBet = 7
BetSelectionSingle = 8
BetSelectionThree = 9

#Assigning variables for numbers with colors, words
SingleBet = "Single number from 1 to 36"
red = (1,3,5,7,9,12,14,16,18,21,23,25,27,30,32,34,36)
black = (2,4,6,8,10,11,13,15,17,19,20,22,24,26,28,29,31,33,35)
green = 0
even = (2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36)
odd = (1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35)
LowBet = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)
HighBet = (19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36)
UserInput = int
black2 = int

#Rolling the ball
def rollfunc():
    global roll
    roll = random.randint(0,36)
    
#Function for user chosing what they want to bet
def user_bet():
   #Assigning global variables for this function
    global UserInput
    global MoneyBetAmount
    global SingleBetNumber
    global TotalBalance
    global CustomNumberInput
    global counter
    global Custom
    #printing what the colors mean / types of bets that can be made
    print("Roulette Game") 
    print("Made by: Connor Houvardas")
    print("")
    print("Your Balance: ","$",TotalBalance )
    print("")
    print("Types of bets you can make:")
    print("Single Bet = ", SingleBet)
    print("Red = ", red)
    print("Black = ", black)
    print("Green = ", green)
    print("Even = ", even)
    print("Odd = ", odd)
    print("High Bet = ", HighBet)
    print("Low Bet = ", LowBet)
    print("Custom Bet = (You choose the amount of numbers that you bet on")
      
    #Validating UserInput
    while UserInputLoop:
        try: 
             UserInput = int
             print("")
             print("What would you like to bet on?: Green = 1, Red = 2, Black = 3, Even = 4, Odd = 5, LowBet = 6, HighBet = 7, Single Bet = 8, Custom Bet = 9")
             UserInput = int(input())
             while UserInput > 9 or UserInput < 1:
                UserInput = int
                print("")
                print("Something went wrong, try again")
                print("")
                print("What would you like to bet on?: Green = 1, Red = 2, Black = 3, Even = 4, Odd = 5, LowBet = 6, HighBet = 7, Single Bet = 8")
                UserInput = int(input())
             break
        except:
            print("")
            print("Something went wrong, try again.")
            UserInput = int

    #Code for putting custom amount of bets into a list (UserInput = 9)
        #Input
    if UserInput == 9:
        while CustomInputLoop:
            try:
                CustomNumberInput = int
                print("")
                print("How many numbers would you like to bet on? (From 2-36)")
                CustomNumberInput = int(input())
                while CustomNumberInput > 36:
                    print("")
                    print("The number you selected is higher than 36.")
                    print("")
                    print("How many numbers would you like to bet on? (From 2-36)")
                    CustomNumberInput = int(input())
                while CustomNumberInput < 2:
                    print()
                    print("")
                    print("The number you have selected is lower than 2.")
                    print("")
                    print("How many numbers would you like to bet on? (From 2-36)")
                    CustomNumberInput = int(input())
                break
            except:
                print("")
                print("Something went wrong, try again")
                CustomNumberInput = int
        #Loop / List / Needed Variables
    counter = 1
    Custom=[]
    if UserInput == 9:
        while counter <= CustomNumberInput:
            try:
                print("")
                print("--------------------------------------------")
                print("")
                print("This is number:", counter, "out of", CustomNumberInput)
                print("Enter a number:")
                CustomNumbersInput = int(input()) 
                if CustomNumbersInput > 36:
                    print("The number you chose is too high. Try again")
                if CustomNumbersInput < 0:
                    print("The number you chose is too low. Try again")
                if CustomNumbersInput in Custom:
                    print("You already chose this number. Try again")
                if CustomNumbersInput>=0 and CustomNumbersInput<=36 and CustomNumbersInput not in Custom:
                    Custom.append(CustomNumbersInput)
                    counter = counter+1
                print("")
                print("Numbers chosen:", Custom)
            except:
                print("Something went wrong, try again")

    #Data Validation / Input for Chosing bet number for UserInput 8
    if UserInput == 8:
        while SingleBetLoop:
            try:
                print("")
                print("Chose a number between 1 and 36")
                SingleBetNumber = int(input())
                while SingleBetNumber > 36 or SingleBetNumber < 1:
                    SingleBetNumber = int
                    print("")
                    print("You entered an invalid number, try again")
                    print("")
                    print("Choose a number between 1 and 36")
                    print("")
                    SingleBetNumber = int(input())
                break
            except:
                print("Invalid input, try again")
                
    #Amount of money user bet
    while MoneyBetLoop:
        try:
            print("--------------------------------------------")
            print("")
            print("Enter the amount you want to bet (Maximum of $",TotalBalance,")")
            MoneyBetAmount = int(input())
            while MoneyBetAmount > TotalBalance or MoneyBetAmount < 1:
                if MoneyBetAmount > TotalBalance:
                    MoneyBetAmount = int
                    print("")
                    print("Please enter an amount to bet that is lower than or equal to your Balance")
                    print("")
                    print("Please enter a new number")
                    print("")
                    MoneyBetAmount = int(input())
                if MoneyBetAmount < 1:
                    MoneyBetAmount = int
                    print("")
                    print("Please enter an amount to bet that is greater than 0")
                    print("Your balance is: $", TotalBalance)
                    print("")
                    print("Please enter a new number")
                    MoneyBetAmount = int(input())
            break
        except:
           print("")
           print("Something went wrong, Try again")
    print("")
    print("You bet: $", MoneyBetAmount)
# Making the bet selection work
# Green = 1, Red = 2, Black = 3, Even = 4, Odd = 5, LowBet = 6, HighBet = 7, Single Bet = 8)
def typeofbet():
    global isWin
    global roll
    if UserInput == BetSelectionGreen:
        if roll == 0: 
            isWin == True
        else:
            isWin = False
    elif UserInput == BetSelectionRed:
        if roll == (1) or (3) or (5) or (7) or (9) or (12) or (14) or (16) or (18) or (21) or (23) or (25) or (27) or (30) or (32) or (34) or (36):
            isWin = True
        else: 
            isWin = False
    elif UserInput == BetSelectionBlack:
        if roll == (1) or (3) or (5) or (7) or (9) or (12) or (14) or (16) or (18) or (21) or (23) or (25) or (27) or (30) or (32) or (34) or (36):
            isWin = True
        else: 
            isWin = False
    elif UserInput == BetSelctionEven:
        if ((roll % 2) == 0):
            isWin = True
        else: 
            isWin = False
    elif UserInput == BetSelectionOdd:
        if ((roll % 2) == 1):
            isWin = True
    elif UserInput == BetSelectionLowBet: 
        if roll <= 18 and roll > 0:
            isWin = True
        else: isWin = False
    elif UserInput == BetSelectionHighBet: 
        if roll >= 19 and roll < 37:
            isWin = True
        else: isWin = False
    elif UserInput == BetSelectionSingle:
        if roll == SingleBetNumber:
            isWin = True
        else: isWin = False
    elif UserInput == 9:
        #needs to only get one right to win.
        if roll in Custom:
            isWin = True
        else: 
            isWin = False

#Deciding if user won or lost Fix balance calculation
def deciding_win_or_loss():
    global TotalBalance
    global isWin
    global MoneyBetAmount
    global WinBalance
    
    if isWin == True:
        if UserInput == 9:
            if MoneyBetAmount == TotalBalance:
                CustomListLen = len(Custom)
                MoneyBetAmount = MoneyBetAmount * 36
                MoneyBetAmount = MoneyBetAmount // CustomListLen
                TotalBalance = TotalBalance + MoneyBetAmount
                print("The ball rolled to the number", (roll))
                print("You chose: ", Custom)
                print("")
                print("You won! Your Balance is now : $", TotalBalance)
            elif MoneyBetAmount < TotalBalance:
                TotalBalance = TotalBalance - MoneyBetAmount
                CustomListLen = len(Custom)
                MoneyBetAmount = MoneyBetAmount * 36
                MoneyBetAmount = MoneyBetAmount // CustomListLen
                TotalBalance = TotalBalance + MoneyBetAmount                
                print("The ball rolled to the number", (roll))
                print("Winning numbers: ", Custom)
                print("")
                print("You won! Your Balance is now : $", TotalBalance)
        if UserInput == 8:
            if TotalBalance == MoneyBetAmount:
                TotalBalance = TotalBalance * 36
                print("The ball rolled to the number", (roll))
                print("")
                print("You won! your Balance is now: $", TotalBalance)
            elif MoneyBetAmount < TotalBalance:
                WinBalance = MoneyBetAmount * 36
                TotalBalance = TotalBalance + WinBalance
                print("The ball rolled to the number", (roll))
                print("")
                print("You won! Your Balance is now : $", TotalBalance)
        elif UserInput == 7:
            if TotalBalance == MoneyBetAmount:
                TotalBalance = TotalBalance * 2
                print("The ball rolled to the number", (roll))
                print("")
                print("You won! your Balance is now: $", TotalBalance)
            elif MoneyBetAmount < TotalBalance:
                TotalBalance = TotalBalance - MoneyBetAmount
                WinBalance = MoneyBetAmount * 2
                TotalBalance = TotalBalance + WinBalance
                print("The ball rolled to the number", (roll))
                print("")
                print("You won! your Balance is now: $", TotalBalance)              
        elif UserInput == 6:
            if TotalBalance == MoneyBetAmount:
                TotalBalance = MoneyBetAmount * 2
                print("The ball rolled to the number", (roll))
                print("")
                print("You won! your balance is now: $", TotalBalance)                
            elif MoneyBetAmount < TotalBalance:
                TotalBalance = TotalBalance - MoneyBetAmount
                WinBalance = MoneyBetAmount * 2
                TotalBalance = TotalBalance + WinBalance
                print("The ball rolled to the number", (roll))
                print("")
                print("You won! your balance is now: $", TotalBalance)
        elif UserInput == 5: 
            if MoneyBetAmount == TotalBalance:
                TotalBalance = MoneyBetAmount * 2             
                print("The ball rolled to the number", (roll))
                print("")
                print("You won! your balance is now: $", TotalBalance)
            elif MoneyBetAmount < TotalBalance:
                TotalBalance = TotalBalance - MoneyBetAmount
                WinBalance = MoneyBetAmount * 2
                TotalBalance = TotalBalance + WinBalance
                print("The ball rolled to the number", (roll))
                print("")
                print("You won! your balance is now: $", TotalBalance)
        elif UserInput == 4:
            if TotalBalance == MoneyBetAmount:
                TotalBalance = MoneyBetAmount * 2
                print("The ball rolled to the number", (roll))
                print("")
                print("You won! Your Balance is now: $", TotalBalance)           
            elif MoneyBetAmount < TotalBalance:
                TotalBalance = TotalBalance - MoneyBetAmount
                WinBalance = MoneyBetAmount * 2
                TotalBalance = TotalBalance + WinBalance
                print("The ball rolled to the number", (roll))
                print("")
                print("You won! your balance is now: $", TotalBalance)                
        elif UserInput == 3:
            if TotalBalance == MoneyBetAmount:
                TotalBalance = MoneyBetAmount * 2
                print("The ball rolled to the number", (roll))
                print("")
                print("You won! Your Balance is now: $", TotalBalance)
            elif MoneyBetAmount < TotalBalance:
                TotalBalance = TotalBalance - MoneyBetAmount
                WinBalance = MoneyBetAmount * 2
                TotalBalance = TotalBalance + WinBalance
                print("The ball rolled to the number", (roll))
                print("")
                print("You won! your balance is now: $", TotalBalance)  
        elif UserInput == 2:
            if MoneyBetAmount == TotalBalance:
                TotalBalance = MoneyBetAmount * 2
                print("The ball rolled to the number", (roll))
                print("")
                print("You won! Your Balance is now: $", TotalBalance) 
            elif MoneyBetAmount < TotalBalance:
                TotalBalance = TotalBalance - MoneyBetAmount
                WinBalance = MoneyBetAmount * 2
                TotalBalance = TotalBalance + WinBalance
                print("The ball rolled to the number", (roll))
                print("")
                print("You won! your balance is now: $", TotalBalance)
        elif UserInput == 1: 
            if TotalBalance == MoneyBetAmount:
                TotalBalance = MoneyBetAmount * 36
                print("The ball rolled to the number", (roll))
                print("")
                print("You won! Your Balance is now: $", TotalBalance)              
            elif MoneyBetAmount < TotalBalance:
                TotalBalance = TotalBalance - MoneyBetAmount
                WinBalance = MoneyBetAmount * 36
                TotalBalance = TotalBalance + WinBalance
                print("The ball rolled to the number", (roll))
                print("")
                print("You won! Your Balance is now: $", TotalBalance)         
    else:
        TotalBalance = TotalBalance - MoneyBetAmount
        print("")
        print("The ball rolled to the number", (roll))
        print("")
        print("You lost!")  # you lose the money that you bet
        print("")
        print("Your Balance Is Now: ", "$", TotalBalance)
       
#Asking user if they would like to continue
def WouldYouLikeToContinue():
    global Continue
    global amountoftimesran
    Beginning = str
    print("")
    print("Do you want to keep playing? Y/N")
    Beginning = str(input())
    if Beginning == "Y" or Beginning == "y":
        Continue = True
    elif Beginning == "N" or Beginning == "n":
        Continue = False
    else:
        while Beginning != "Y" or Beginning != "y" or Beginning != "n" or Beginning != "N":
            print("Invalid Input")
            print("")
            print("Do you want to keep playing? Y/N")
            Beginning = str(input())
            if Beginning == "Y" or Beginning == "y":
                Continue = True
                break
            elif Beginning == "N" or Beginning == "n":
                Continue = False
                break
    
#Executing Functions
while Continue == True and TotalBalance > 0:
    rollfunc()
    user_bet()
    typeofbet()
    deciding_win_or_loss()
    WouldYouLikeToContinue()
    if Continue == True:
        if TotalBalance <= 0:
            print("")
            print("You do not have enough funds remaining to continue.")
print("")
input("Press enter to close")