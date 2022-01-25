#importing needed libraries
import math
import statistics
#global variables
CalcSelect = int
areaofshapes = True
noequal = True
UnitCheck = str
NameShapeVar = True
Continue = True
userchoice = True

#Selecting what type of calculation user wants to do
def CalculationSelection():
    global CalcSelect
    calcselectinput = True
    print("Advanced Calculator")
    print("By: Connor Houvardas")
    print("")
    print("What would you like to calculate?")
    print("1 = Simple Operations (Addition, Subtraction, Multiplcation, Division)")
    print("2 = Square Root")
    print("3 = Exponents")
    print("4 = Area of a shape")
    print("5 = Perimeter of shape")
    print("6 = Slope")
    print("7 = Volume")
    print("8 = Mean")
    print("9 = Mode")
    print("10 = Median")
    print("11 = Y Intercept given a point on line and the slope (Finish this)")
    print("")
    print("From the options above what would you like to calculate? ")
    #Selecting what user wants to calculate (with data validation)
    while calcselectinput:
        try:
            CalcSelect = int(input("Enter your selection here: "))
            while CalcSelect < 1 or CalcSelect > 11:
                if CalcSelect > 11:
                    print("The number you entered is too high.")
                elif CalcSelect < 1:
                    print("The number you entered is too low.")
                CalcSelect = int(input("Enter your selection here: "))
            break
        except: 
            print("Something went wrong, try again")
            print("Invalid response.")

def simpleoperations():
    UserInput1 = str
    simpleop = True
    while simpleop:
        try:
           print("")
           print("What would you like to calculate?")
           print("Addition, Subtraction, Multiplcation, Division")
           UserInput1 = str(input("Choose which calculation you would like to make: ")).lower()
           while UserInput1 != "addition" and UserInput1 != "subtraction" and UserInput1 != "multiplcation" and UserInput1 != "division":
               print("")
               print("Invalid Input")
               print("What would you like to calculate?")
               print("Addition, Subtraction, Multiplcation, Division")
               UserInput1 = str(input("Choose which calculation you would like to make: ")).lower()
           if UserInput1 == "subtraction":     #maybe make these lists if I have time left.
                #subtract=[]
                print("")
                print("Enter the first number you would like to subtract")
                sub1 = int(input("Enter the first number here: "))
                print("")
                print("Enter the second number you would like to subtract")
                sub2 = int(input("Enter the second number here: "))
                subtraction = sub1 - sub2
                print("")
                print(sub1, "-", sub2, "=", subtraction)
                print("Final Answer = ",subtraction)
           if UserInput1 == "addition":
                print("")
                print("Enter the first number you would like to add")
                add1 = int(input("Enter the first number here: "))
                print("Enter the second number you would like to add")
                add2 = int(input("Enter the first number here: "))
                addition = add1 + add2
                print("")
                print(add1, "+", add2, "=", addition)
                print("Final Answer = ", addition)
           if UserInput1 == "multiplcation": 
                print("")
                print("Enter the first number you would like to multiply")
                mul1 = int(input("Enter the first number here: "))
                print("Enter the second number you would like to multiply")
                mul2 = int(input("Enter the second number here: "))
                multiplcation = mul1 * mul2
                print("")
                print(mul1, "*", mul2, "=", multiplcation)
                print("Final Answer = ", multiplcation)
           if UserInput1 == "division":
                print("")
                print("Enter the first number you would like to divide")
                div1 = float(input("Enter the first number here: "))
                print("Enter the second number you would like to divide")
                div2 = float(input("Enter the second number here: "))
                division = div1 / div2
                print("")
                print(div1, "÷", div2, "=", division)
           break
        except:
            print("")
            print("Something went wrong, try again")
            print("Invalid input")

# Calculalting square root (With data validation)
def squareroot():
    print("")
    print("You have selected square root")
    print("")
    sqrttrue = True
    while sqrttrue:
        try:
            squarerootinput = int(input("Enter a number to square root: "))
            while squarerootinput < 0:
                print("The number you entered is too low, try again.")
                squarerootinput = int(input("Enter a number to square root: "))
            break
        except:
            print("Something went wrong, try again")
            print("Invalid response")
    sqrt = squarerootinput ** 0.5   
    print("square root:", sqrt)

#Powers and Exponents of numbers (With data validation)
def exponents():
    print("")
    print("You have selcted exponents")
    basetrue = True
    expotrue = True
    #Recieving base number from user
    while basetrue:
        try:
            print("")
            base = int(input("Enter a base number: "))
            while base < 0:
                print("Invalid response, try again.")
                print("You cannot enter a negative number")
                base = int(input("Enter a base number: "))
            break
        except:
            print("Something went wrong, try again")
            print("Invalid response")
    #Receiving exponent from user
    while expotrue:
        try:
            print("")
            exponent = int(input("Enter an exponent: "))
            while exponent < 0:
                print("You cannot enter a negative number.")
                print("")
                exponent = int(input("Enter an exponent: "))
            break
        except:
            print("Something went wrong, try again")
            print("Invalid response")

    
    finalexponent = base ** exponent
    print("Exponent: ", finalexponent)
            
#Calculating area of shapes
def areaofshapes():
    
    #You selected:
    print("You selected: Area of shapes")
    print("")
    #Checking what units the user wants to use before calculating
    global UnitCheck
    global areaofshapes 
    global noequal
    global NameShapeVar
    
    while areaofshapes:
        try:
            while UnitCheck != "cm" and UnitCheck != "km" and UnitCheck != "m":           
                print("What unit would you like to use? CM, M, KM:")
                UnitCheck = str(input()).lower()
            break
        except:
            print("")
            print("Something went wrong, Try again")
#User Choosing if they want to calculate area of circle, square, rectangle, or triangle
    while NameShapeVar:
        try:
            nameofshape = str
            while nameofshape != "circle" and nameofshape != "square" and nameofshape != "rectangle" and nameofshape != "triangle":
                print("")
                print("What shape would you like to calculate the area of? ")
                print("Your options are: Square, Rectangle, Triangle or Circle")
                nameofshape = str(input("Enter the shape here: ")).lower()
            break
        except:
            print("Something went wrong, try again")
    #Code for area of rectangle
    if nameofshape == "rectangle":
        rectangleL = True
        rectangleW = True
        while rectangleL: #L means length
            try:
                print("")
                print("Enter the length of the rectangle")
                L = int(input("Enter the length here: "))
                while L < 1:
                    print("")
                    print("The number you entered is too low (Less than 1). Enter a valid number")
                    L = int(input("Enter the length here: "))
                break
            except:
                print("")
                print("Something went wrong, Try again")
                print("Invalid response")
        while rectangleW: #W means width
            try:
                print("")
                print("Enter the width of the rectangle")
                W = int(input("Enter the width: "))
                while W < 1:
                    print("")
                    print("Number you entered is too low (Less than 1). Enter a valid number")
                    W = int(input("Enter the width: "))
                break
            except:
                print("")
                print("Something went wrong, Try again")
                print("Invalid response")
        print("")
        print("The area of this rectangle is: ", L * W, UnitCheck)
    
        #area of square
    elif nameofshape == "square":
        square = True
        print("")
        while square:
            try:
                print("Enter the length of the square")
                SideL = int(input("Enter the side length of the square here: "))
                while SideL < 1:
                    print("")
                    print("Enter the length of the square")
                    SideL = int(input("Enter the side length of the square here: "))
                break
            except:
                print("")
                print("Something went wrong, Try again")
                print("Invalid response")
        print("The area of this square is: ", SideL ** 2, UnitCheck)
    #area of triangle
    elif nameofshape == "triangle":
        print("")
        Height = int(input("Enter the height of the triangle here: "))      #add data validation at some point here
        Base = int(input("Enter the base of the triangle here:"))
        print("")
        print("The area of this triangle is: ", Base * Height / 2, UnitCheck)
    #area of circle
    elif nameofshape == "circle":
        print("")
        Radius = float(input("Enter the radius of the circle here: "))
        print("")
        print("The area of this circle is: ", Radius ** 2 * 3.14, UnitCheck)

def perimeterofshape():
    #This section of code is perimeter of shape
    options = True
    while options:
        try:
            print("You selected: Perimeter of shape")
            print("")
            print("What shape would you like to find the perimeter of? ")
            print("Your options are: Square, Rectangle, Triangle or Circle")
            nameofshape = str(input("Enter the shape here: ")).lower()
            while nameofshape != "square" and nameofshape != "rectangle" and nameofshape != "triangle" and nameofshape != "circle":
                print("What shape would you like to find the perimeter of? ")
                print("Your options are: Square, Rectangle, Triangle or Circle")
                nameofshape = str(input("Enter the shape here: ")).lower()
            break
        except:
            print("Something went wrong, try again")
            print("Invalid response.")
    square = True
    if nameofshape == "square":
        while square:
            try:
                Side = float(input("What is the side length of the square?: "))
                print("")
                while Side < 1:
                    print("The number you entered is too low. Try again")
                    Side = float(input("What is the side length of the square?: "))
                break
            except:
                print("Something went wrong, try again")
                print("Invalid response")          
        print("The perimeter of this square is: ", Side * 4)
    
    rectangleL = True
    rectangleW = True
    if nameofshape == "rectangle":
        while rectangleW:
            try:
                print("")
                Width_Side = float(input("What is the Width of the rectangle?: "))
                print("")
                while Width_Side < 1:
                    print("Enter a number thats higher than 0")
                    print("")
                    Width_Side = float(input("What is the Width of the rectangle?: "))
                    print("")
                break
            except:
                print("Something went wrong, try again")
                print("Invalid response")
        
        while rectangleL:
            try:
                print("")
                Length_Side = float(input("What is the Length of the rectangle?: "))
                while Length_Side < 1:
                    print("Enter a number thats higher than 0.")
                    print("")
                    Length_Side = float(input("What is the Length of the rectangle?: "))
                break
            except:
                print("Something went wrong, try again")
                print("Invalid response")

        print("")
        WidthCalc = Width_Side * 2
        LengthCalc = Length_Side * 2
        print("The perimeter of this rectangle is: ", WidthCalc + LengthCalc)
    
    if nameofshape == "triangle":
        sideA_validation = True
        while sideA_validation:
            try:
                print("")
                SideA = float(input("Enter side A: "))
                while SideA < 1:
                    print("Enter a number that is higher than 0")
                    print("")
                    SideA = float(input("Enter side A: "))
                break
            except:
                print("Something went wrong, try again")
                print("Invalid response")
                    
        sideB_validation = True
        while sideB_validation:
            try:
                print("")
                SideB = float(input("Enter side B: "))
                while SideB < 1:
                    print("Enter a number that is higher than 0")
                    print("")
                    SideB = float(input("Enter side B: "))
                break
            except:
                print("Something went wrong, try again")
                print("Invalid response")

        sideC_validation = True
        while sideC_validation:
            try:
                print("")
                SideC = float(input("Enter side C: "))
                while SideC < 1:
                    print ("Enter a number that is higher than 0")
                    print("")
                    SideC = float(input("Enter side C: "))
                break
            except:
                print("Something went wrong, try again")
                print("Invalid response")              
        print("The perimeter of this triangle is: ", SideA + SideB + SideC)

    if nameofshape == "circle":
        Radius = float(input("Enter the Radius of the circle: "))
        final_float = Radius * 2 * (math.pi)
        shorter_float = round(final_float, 3)
        print("The perimeter of this circle is: ", shorter_float)

#Calculating the volume of shapes

def Volume():
    #User choosing which shape they would like the volume calculated
    options = True
    while options:
        try:
            print("You selected: Volume")
            print("")
            print("What shape would you like to find the Volume of? ")
            print("Your options are: Cube, Cone, Sphere")
            nameofshape = str(input("Enter the shape here: ")).lower()
            while nameofshape != "cube" and nameofshape != "cone" and nameofshape != "sphere":
                print("What shape would you like to find the Volume of? ")
                print("Your options are: Cube, Cone, Sphere")
                nameofshape = str(input("Enter the shape here: ")).lower()
            break
        except:
            print("Something went wrong, try again")
            print("Invalid response.")
    
    #Required inputs for calculating cube
    if nameofshape == "cube":
        cubeval = True
        while cubeval:
            try:
                print("")
                userinput = int(input("What is the side length of the cube?: "))
                while userinput < 1:
                    print("")
                    print("Invalid input, try again")
                    print("")
                    userinput = int(input("What is the side length of the cube?: "))
                    if userinput >= 1: 
                        break
                break
            except:
                print("Something went wrong, try again")
                print("Invalid response.")
        
        #Calculating final answer for cube
        cube = userinput ** 3
        shorter_cube = round(cube, 5)
        print("V = ", shorter_cube)

    #Required inputs for calculating cone
    if nameofshape == "cone":
        conevalradius = True
        conevalheight = True
        #Radius of cone
        while conevalradius:
            try:
                print("")
                radius = int(input("What is the radius of the cone?: "))
                while radius < 1:
                    print("")
                    print("Invalid Input, try again")
                    print("")
                    radius = int(input("What is the radius of the cone?: "))
                    if radius >= 1:
                        break
                break
            except:
                print("")
                print("Something went wrong, try again")
                print("Invalid response")
         #Height of cone
        while conevalheight:
            try:
                print("")
                height = int(input("What is the height of the cone?: "))
                while height < 1:
                    print("")
                    print("Invalid Input, try again")
                    print("")
                    height = int(input("What is the height of the cone?: "))
                    if height >= 1:
                        break
                break
            except:
                print("")
                print("Something went wrong, try again")
                print("Invalid response")

        #Calculating final answer for volume of cone
        cone = math.pi * radius ** 2 * height / 3
        shorter_cone = round(cone, 5)
        print("V = ", shorter_cone)

    if nameofshape == "sphere":
        sphereradval = True
        while sphereradval == True:
            try:
                print("")
                radius = int(input("What is the radius of the sphere?: "))
                while radius < 1:
                    print("")
                    print("Invalid Input, Try again")
                    print("")
                    radius = int(input("What is the radius of the sphere?: "))
                    if height >= 1:
                        break
                break
            except:
                print("")
                print("Something went wrong, try again")
                print("Invalid response")
        
        sphere = 4 / 3 * math.pi * radius ** 3
        shorter_sphere = round(sphere, 5)
        print("V = ", shorter_sphere)


#Calculating slope given 2 points might be wrong figure that out later
def SlopeCalculator():
    x1validation = True
    y1validation = True
    x2validation = True
    y2validation = True
    
    while x1validation:
        try:
            print("")
            x1 = float(input("Enter x1: ", ))
            break
        except:
            print("Something went wrong, try again")
            print("Invalid response")
    
    while y1validation:
        try:
            print("")
            y1 = float(input("Enter y1: ", ))
            break
        except:
            print("Something went wrong, try again")
            print("Invalid response")
            
    while x2validation:
        try:
            print("")
            x2 = float(input("Enter x2: ", ))
            break
        except:
            print("Something went wrong, try again")
            print("Invalid response")

    while y2validation:
        try:
            print("")
            y2 = float(input("Enter y2: ", ))
            break
        except: 
            print("Something went wrong, try again")
            print("Invalid response")

    m1 = y2 - y1 
    m2 = x2 - x1
    m = m1 / m2
    m_short = round(m, 4)
    print("The slope is = ", m_short)

#Calculating Y-Intercept given point on line and slope
def Calculating_Y_Intercept():
    print("")
    print("___________________________")
    print("You are now calculating: Y Intercept")
    print("")
    userchoice = True
    while userchoice == True:
        try:
            #UserInputs
            print("______________________________________________________________________________________________________")
            numberinputx = int(input("Enter x value of point: "))
            print("")
            numberinputy = int(input("Enter y value of point: "))
            print("")
            fraction_check = str(input("Is your slope a fraction?: ")).lower()
            if fraction_check != "yes" or fraction_check != "y" or fraction_check != "n" or fraction_check != "no":
                while fraction_check != "yes" and fraction_check != "y" and fraction_check != "n" and fraction_check != "no":
                    print("Something went wrong, try again")
                    fraction_check = str(input("Is your slope a fraction?: ")).lower()
                    print("")
                    if fraction_check == "yes" or fraction_check == "y" or fraction_check == "n" or fraction_check == "no":
                        break
            if fraction_check == "yes" or fraction_check == "y":
                print("")
                slopeinputn = int(input("Enter numerator"))
                print("")
                slopeinputd = int(input("Enter denominator"))
            elif fraction_check == "no" or fraction_check == "n":
                print("")
                slope = int(input("Enter slope: "))
            break
        except:
            print("")
            print("Something went wrong, try again")
            print("Invalid Input")
    #Y Intercept Calculation
    #b = y - slope * x
    if fraction_check == "no" or fraction_check == "n":
        b = numberinputy - slope * numberinputx
        print("")
        print("Y Intercept = ", b)
    elif fraction_check == "yes" or fraction_check == "y":
        b = numberinputy - slopeinputn//slopeinputd * numberinputx
        print("Y Intercept = ", b)
    

#FINISH  THIS UP BY THE END OF THE DAY

#Mean median and mode below, median is calculated using a for loop, mode and mean are using while loops.
#Calculating mean
def CalculatingMean():
    mean = [] 
    print("")
    print("___________________________")
    print("You are now calculating: Mean")
    print("")
    userchoice = True
    while userchoice == True:
        mean.sort()
        try:       
            print("______________________________________________________________________________________________________")
            meanlen = len(mean)
            if meanlen > 0:
                print(mean)
            numberinput = int(input("Enter a number: "))
            mean.append(numberinput)
            print("")
            userchoicex = ""
            userchoicex = str(input("Would you like to keep adding numbers? (Y/N)")).lower()
            while userchoicex != "n" and userchoicex != "no" and userchoicex != "y" and userchoicex != "yes":
                print("Invalid input, try again")
                userchoicex = str(input("Would you like to keep adding numbers? (Y/N)")).lower()
            if userchoicex == "y" or userchoicex == "yes":
                userchoice = True 
            elif userchoicex == "n" or userchoicex == "no":
                userchoice = False
            if userchoice == False:   
                break
        except:
            print("")
            print("Something went wrong, try again")
            print("Invalid Input")
    print("")
    print("")
    mean.sort()
    print(mean)
    meanvalue = statistics.mean(mean)
    print("The mean is: ", meanvalue)

def CalculatingMode():
    userchoice = True
    print("")
    print("___________________________")
    print("You are now calculating: Mode")
    print("")
    mode = []
        
    while userchoice == True:
        mode.sort()
        try:
            print("___________________________________________________________")
            modelen = len(mode)
            if modelen > 0:
                print(mode)
            numberinput = int(input("Enter a number: "))
            mode.append(numberinput)
            print("")
            userchoicex = ""
            userchoicex = str(input("Would you like to keep adding numbers? (Y/N)")).lower()
            while userchoicex != "n" and userchoicex != "no" and userchoicex != "y" and userchoicex != "yes":
                print("Invalid input, try again")
                userchoicex = str(input("Would you like to keep adding numbers? (Y/N)")).lower()
            if userchoicex == "y" or userchoicex == "yes":
                userchoice = True 
            elif userchoicex == "n" or userchoicex == "no":
                userchoice = False
            if userchoice == False:   
                break
        except:
            print("")
            print("Something went wrong, try again")
            print("Invalid Input")
    print("")
    print("")
    mode.sort()
    print(mode)
    modevalue = statistics.mode(mode)
    print("The mode is: ", modevalue)

def CalculatingMedian():
    userchoice = True
    print("")
    print("___________________________")
    print("You are now calculating: Median")
    print("")
    count = 1
    median = []
    #add for loop
    while userchoice:
        try:
            forinput = int(input("How many numbers would you like to use?: "))
            while forinput < 1:
                print("")
                print("Invalid response, try again")
                print("Entered number was less than 1.")
                print("")
                forinput = int(input("How many numbers would you like to use?: "))
            break
        except:
            print("")
            print("Something went wrong, try again")
            print("Invalid Input")

    for x in range(forinput):
        print("This is number: ", count)
        try:
            print("___________________________________________________________")
            medianlen = len(median)
            if medianlen > 0:
                count = count + 1
            numberinput = int(input("Enter a number: "))
            median.append(numberinput)
            print("")
        except:
            print("")
            print("Something went wrong, try again")
            print("Invalid Input")

    print("")
    print("")
    median.sort()
    print(median)
    medianvalue = statistics.median(median)
    print("The median is: ", medianvalue)

#Looping the program if user wants to continue
def WouldYouLikeToContinue():
    CalcSelect = int
    global Continue
    Beginning = str
    print("")
    print("Do you want to make another calculation? Y/N")
    Beginning = str(input())
    if Beginning == "Y" or Beginning == "y":
        Continue = True
    elif Beginning == "N" or Beginning == "n":
        Continue = False
    else:
        while Beginning != "Y" or Beginning != "y" or Beginning != "n" or Beginning != "N":
            print("Invalid Input")
            print("")
            print("Do you want to make another calculation? Y/N")
            Beginning = str(input())
            if Beginning == "Y" or Beginning == "y":
                Continue = True
                break
            elif Beginning == "N" or Beginning == "n":
                Continue = False
                break

#^^^^ ADD DIFFERENT UNITS ( M, CM, etc... )

#Executing functions

while Continue == True:
    CalculationSelection()
    if CalcSelect == 1:
        simpleoperations()
    elif CalcSelect == 2:
        squareroot()
    elif CalcSelect == 3:
        exponents()
    elif CalcSelect == 4:
        areaofshapes()
    elif CalcSelect == 5:
        perimeterofshape()
    elif CalcSelect == 6:
        SlopeCalculator()
    elif CalcSelect == 7:
        Volume()
    elif CalcSelect == 8:
        CalculatingMean()
    elif CalcSelect == 9:
        CalculatingMode()
    elif CalcSelect == 10:
        CalculatingMedian()
    elif CalcSelect == 11: 
        Calculating_Y_Intercept()
    WouldYouLikeToContinue()
    
    
print("")
input("Press enter to close")


