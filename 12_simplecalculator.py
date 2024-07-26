######################################################################################
# Dateiname:       12_simplecalculator.py  [3-12]                                    #
# ---------------------------------------------------------------------------------- #
# Implementierung: https://www.programiz.com/python-programming/examples/calculator  #
# Algorithmus:                                                                       #
# Ein-/Ausgabe:                                                                      #
# Beschreibung:    Einfacher Taschenrechner mit Hilfe von Funktionen                 #
# Lernziele:       Funktionen; Endlosschleife, Division durch Null (try .. except)   #
# Anmerkungen:     https://www.w3schools.com/python/python_try_except.asp            #
######################################################################################

# This function adds two numbers 
def add(x, y):
    return x + y

# This function subtracts two numbers 
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# The folowing while loop is used to iterate several (infinite) times through operations
while True:
    print("\nSelect operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Take input from the user 
    choice = input("Enter choice (1/2/3/4): ")
    # We have to quit operations, if user enters string different to expected numbers
    if choice not in ["1", "2", "3", "4"]: 
        print("Exit operations.")
        break

    # User enters numbers for operations
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == '1':
        print("-> Addition: ", end="")
        # print(num1,"+",num2,"=", add(num1,num2))
        print(f"{num1} + {num2} = {add(num1, num2)}")

    elif choice == '2':
        print("-> Subtraktion: ", end="")
        # print(num1,"-",num2,"=", subtract(num1,num2))
        print(f"{num1} - {num2} = {subtract(num1, num2)}")

    elif choice == '3':
        print("-> Multiplikation: ", end="")
        # print(num1,"*",num2,"=", multiply(num1,num2))
        print(f"{num1} * {num2} = {multiply(num1, num2)}")

    elif choice == '4':
        print("-> Division: ", end="")
        # print(num1,"/",num2,"=", divide(num1,num2))
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    
        # At least at this point it would be desirable to make a useful hint to the user in case of 
        # division by zero (ZeroDivisionError)
        # Thus the following lines will replace the latter (can already be implemented at divide funtion)
        '''
        if num2 != 0:
            print(num1,"/",num2,"=", divide(num1,num2))
        else:
            print("Devision by zero not allowed!")
        '''
    
        # using smarter try except statements
        # https://www.w3schools.com/python/python_try_except.asp
        '''
        try:
            print(num1,"/",num2,"=", divide(num1,num2))
        except ZeroDivisionError:
            print("Devision by zero not allowed!")
        '''
