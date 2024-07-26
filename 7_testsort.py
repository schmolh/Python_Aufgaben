#############################################################################################
# Dateiname:       19_sortwords.py  [3-18 optional]                                         #
# ----------------------------------------------------------------------------------------- #
# Implementierung: https://www.programiz.com/python-programming/examples/alphabetical-order #
# Algorithmus:                                                                              #
# Ein-/Ausgabe:                                                                             #
# Beschreibung:    Alphabetische Sortierung von Wörtern einer Zeichenkette                  #
# Lernziele:       String-Manipulation (lower(), split(), sort())                           #
# Anmerkungen:                                                                              #
#############################################################################################

DEBUG_INFO = True

# change this value for a different result
my_str = "Hello this Is an Example With cased letters"
# uncomment to take input from the user
my_input = input("Enter a string: ").lower()

# You may want to execute sort function on all lower cased words
my_str_lower = my_str.lower()

if my_str_lower.__contains__(my_input):
   print("ist im string enthalten")
else:
   print("ist NICHT im string enthalten")

#my_str_low = my_str

# breakdown the string into a list of words
words = my_str_low.split()

if DEBUG_INFO:
   print(my_str)
   print("Initial unsorted words:") 
   print(words)

# sort the list
words.sort()

# display the sorted words

print("Final sorted words:")
print(words)

# Alternative Ausgabe
"""
for word in words:
   print(word, end=', ')
"""