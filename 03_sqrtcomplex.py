######################################################################################
# Dateiname:       03_sqrtcomplex.py  [1-3 optional]                                 #
# ---------------------------------------------------------------------------------- #
# Implementierung: https://www.programiz.com/python-programming/examples/square-root #
# Algorithmus:                                                                       #
# Ein-/Ausgabe:    num=1+2j / num_sqrt=1.272+0.786j                                  #
# Beschreibung:    Quadratwurzel einer komplexen Zahl                                #
# Lernziele:       Importmodul                                                       #
# Anmerkungen:     eval-Funktion zur Konvertierung einer Eingabe (optional)          #
######################################################################################

# Find square root of real or complex numbers
# Import the complex math module
import cmath

# change this value for a different result
#num = 1+2j
num = 7

# uncommment to take input from the user
# eval function to convert to complex number 
# num = eval(input('Enter a number: '))

num_sqrt = cmath.sqrt(num) 
# with f-string formatting
print(f'The square root of {num} is {num_sqrt.real:0.3f}+{num_sqrt.imag:0.3f}j')
# and slightly older formatting
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))