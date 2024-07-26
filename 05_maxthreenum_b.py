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
debug=True
# fixed values of num1, num2 and num3
if debug==True:
    num1 = 10
    num2 = 14
    num3 = 12
else:
    # or values taken from the user
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))

mylist=[num1, num2, num3]
print("Unsorted   ",mylist)
mylist.sort(reverse=False)

print("Sorted List",mylist)
