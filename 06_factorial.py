###########################################################################################
# Dateiname:       06_factorial.py  [2-6]                                                 #
# --------------------------------------------------------------------------------------- #
# Implementierung: https://www.programiz.com/python-programming/examples/factorial        #
# Algorithmus:     (Def) https://de.serlo.org/mathe/1765/fakult%C3%A4t                    #
#           (Pseudocode) https://atechdaily.com/posts/algorithm-for-factorial-number      #
# Ein-/Ausgabe:    number=7 / fact=5040                                                   #
# Beschreibung:    Fakultät (engl. factorial) einer Zahl                                  #
# Lernziele:       Debugging (Haltepunkte, Einzelschritt; Debugging-Switch), for, range() #
# Anmerkungen:     factorial.pdf (Debugging-Anleitung)                                    #
###########################################################################################

# DEBUGGING switch
DEBUG_INFO = True

"""
Weitere Debugging-Möglichkeiten mit 
- Ausführen > Haltepunkte umschalten (Haltepunkte setzen/entfernen)
- Ausführen und debuggen > Variablen (Beobachtung sämtlicher Variablen)
                         > Überwachen (Beobachtung spezieller Variablen)
"""

# uncomment to take input from the user
#number = int(input("Enter a number: "))

# or fixed value: change the value for a different result
number = 7

# Init result to be calculated
fact = 1

# check if the number is negative or zero
if number < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif number == 0:
    print("The factorial of 0 is 1")
else:
    # the range operator builds iteration: 1 ... (num+1) will yield in 1 ... 8
    # 'for' iteration always omits last entry in iteration, see 
    # https://pynative.com/python-range-function/ 
	# Test der Range-Funktion im interaktiven Fenster: 
    if DEBUG_INFO: print(list(range(1, number+1))) # print the output list of the range-Funktion
    # Output with num=7: [1, 2, 3, 4, 5, 6, 7]

    for i in range(1,number + 1):
        if DEBUG_INFO: 
            print("factorial =", fact, "*", i, end=" = ")
        fact = fact*i
        if DEBUG_INFO: 
            print(fact)

    print(f"Die Fakultät von {number} ist {fact}") # newest f-string formatting
    #print("The factorial of",number,"is",fact) # no formatting
    #print("The factorial of {:5d} is {:5d}".format(number, fact))  # slightly older formatting