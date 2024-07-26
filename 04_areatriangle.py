########################################################################################
# Dateiname:       04_areatriangle.py  [1-4]                                           #
# ------------------------------------------------------------------------------------ #
# Implementierung: https://www.programiz.com/python-programming/examples/area-triangle #
# Algorithmus:     https://www.mathelounge.de/531812/artikel-satz-des-heron            #
#                  https://de.wikipedia.org/wiki/Satz_des_Heron                        #
# Ein-/Ausgabe:    a=5,b=6,c=7 / area=14.70                                            #
# Beschreibung:    Fläche eines Dreiecks (Satz des Heron)                              #
# Lernziele:       Flussdiagramm (Algorithmus)                                         #
# Anmerkungen:     Tagesprojekt (optional)                                             #
########################################################################################

# Fixed values for simplicity
a = 5
b = 6
c = 7

# Uncomment below to take inputs from the user
# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))
# c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

# Printing results using f-string formatting
print(f'The area of the triangle is {area:0.2f}')

# Below we show the slightly older formatting
# print('The area of the triangle is {:0.2f}'.format(area))

# And the old formatting for information purpose
# print('The area of the triangle is %0.2f' % area)
