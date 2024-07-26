########################################################################################
# Dateiname:       09_primenum.py  [2-9]                                               #
# ------------------------------------------------------------------------------------ #
# Implementierung: https://www.programiz.com/python-programming/examples/prime-number  #
# Algorithmus:     https://de.wikipedia.org/wiki/Primzahlgenerator#Trivialer_Generator #
#                  (ganzzahl. Div.) https://www.matheretter.de/wiki/division-mit-rest  #
# Ein-/Ausgabe:    num=407 / not prime; num=719 / prime number                         #
# Beschreibung:    Test einer eingegebenen ganzen Zahl auf Primzahl                    #
# Lernziele:       (Rest einer) ganzzahligen Division (%, //), for .. break .. else    #
# Anmerkungen:                                                                         #
########################################################################################

# DEBUGGING switch
DEBUG_INFO = True

# Zu testende Zahl
num = 31

# take input from the user
# num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   # Ganzzahlige Division mit Rest, siehe 
   # https://www.matheretter.de/wiki/division-mit-rest 
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           if DEBUG_INFO: 
              print(i,"*",num//i,"is",num)
           break # we immediately leave the loop if we find num not to be prime
   else:
       # A for loop can have an optional else block as well. 
       # The else part is executed if the items in the sequence used in for loop exhausts. 
       # break statement can be used to stop a for loop. In such case, the else part is ignored.
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")


def myFunction(zahl):
    print("In Funktion: ", zahl)


for i in range(1,50):
    myFunction(i)