###############################################################################################
# Dateiname:    05_maxthreenum.py  [1-5]                                                      #
# ------------------------------------------------------------------------------------------- #
# Implement.:   https://www.programiz.com/python-programming/examples/largest-number-three    #
# Algorithmus:  Maximum3.pdf                                                                  #
# Ein-/Ausgabe: num1=10,num2=14,num3=12 / largest=14                                          #
# Beschreibung: Max. dreier ganzen Zahlen                                                     #
# Lernziele:    Bedingte Anweisung / Verzweigung (if .. elif .. else)                         #
# Anmerkungen:                                                                                #
###############################################################################################
DEBUG=True
# fixed values of num1, num2 and num3
if DEBUG:
    num1 = 10
    num2 = 14
    num3 = 12
    num4 = 2
else:
    # or values taken from the user
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))
    num4 = int(input("Enter third number: "))

myList=[num1, num2, num3, num4]
myList.sort(reverse=True)

print(myList)

# f-string formatting
print(f"The largest number between {num1}, {num2} {num3} is {largest}.")

# Slightly older formatting, note that 'd' in '{0:d} etc. can be omitted, see https://pyformat.info/#simple
# print("The largest number between {0:d}, {1:d} and {2:d} is {3:d}".format(num1, num2, num3, largest))

# No formatting
# print("The largest number between",num1,",",num2,"and",num3,"is",largest)