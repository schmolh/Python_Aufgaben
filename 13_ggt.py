######################################################################################
# Dateiname:       13_ggt.py  [3-13]                                                 #
# ---------------------------------------------------------------------------------- #
# Implementierung: https://www.programiz.com/python-programming/examples/hcf         #
# Algorithmus:     (Def) 13_ggt_Def.JPG                                              #
#                  13_ggt_Euklid_iterativ, 13_ggt_Euklid_rekursiv, 13_ggt_Simple     #
#                  (Def) https://de.wikipedia.org/wiki/Euklidischer_Algorithmus      #
# Ein-/Ausgabe:    num1=54, num2=24 / hcf=6                                          #
# Beschreibung:    GGT zweier Zahlen (engl. highest common factor HCF)               #
# Lernziele:       Funktionen; if __name__ == "__main__"; (Rekursion)                #
#                  Importmodul timeit (optional)                                     #
# Anmerkungen:     https://www.data-science-architect.de/__name____main__/           #
######################################################################################

# define the HCF function using Euklidian iterative algorithm
# In der iterativen Variante, siehe https://de.wikipedia.org/wiki/Euklidischer_Algorithmus#Iterative_Variante
def Euklid_iterative(x, y):

   while(y != 0): 
       h = x % y
       x = y
       y = h
   return x


# define the same HCF function using recursion, see 
# https://de.wikipedia.org/wiki/Euklidischer_Algorithmus#Rekursive_Variante
def Euklid_recursive(x, y):
    if y == 0:
        return x
    else:
        return Euklid_recursive(y, x % y)


# define the same HCF function using a straight forward simple version
# see https://www.inf-schule.de/algorithmen/grundlagen/eigenschaften/effizienz/algorithmen 
def Euklid_simple(x, y):
    while x > 0 and y > 0:
        if x >= y:
            x = x - y
        else:
            y = y - x
    return x+y


# define Euklid_iterative() using a short version of the algorithm
# In der iterativen Variante, siehe https://de.wikipedia.org/wiki/Euklidischer_Algorithmus#Iterative_Variante
def Euklid_short(x, y):
    
   while(y): # short for while (y != 0)
       x, y = y, x % y # short for x = y; y = x % y (full: h = x % y; x = y; y = h)

   return x


# define the same HCF function using a straight forward alternative version
def Euklid_alternative(x, y):

    # choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(2, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
            
    return hcf


# if __name__ wird benötigt, um 12_ggt (bzw. ggt_module) als Modul von anderen Python-Modulen aus
# aufrufen zu können (in unserem Beispiel von 13_ggt_run.py). Dabei werden lediglich die Funktionen
# weiter oben verwendet, nicht jedoch der Code ab if __name__
# Wird dagegen 12_ggt.py direkt von der Konsole aus aufgerufen, so wird zunächst der Code nach 
# if __name__ ausgeführt. Dieser ruft wiederum die oben definierten Funktionen nacheinander auf.
# Weitere Infos: https://www.data-science-architect.de/__name____main__/
if __name__ == "__main__":
    import timeit  # used to measure execution times of the different functions (see below)

    # Start of main program (using already defined input values)
    num1 = 54 
    num2 = 24

    # take input from the user instead
    # num1 = int(input("Enter first number: "))
    # num2 = int(input("Enter second number: "))

    start = timeit.timeit()
    print("The H.C.F. of", num1,"and", num2,"is", Euklid_simple(num1, num2), "(using simple 'Wechselwegnahme' algorithm)")
    end = timeit.timeit()
    print("     Elapsed time: {0:0.4f} sec".format(end - start))

    start = timeit.timeit()
    print("The H.C.F. of", num1,"and", num2,"is", Euklid_iterative(num1, num2), "(using iterative Euklidian algorithm)")
    end = timeit.timeit()
    print("     Elapsed time: {0:0.4f} sec".format(end - start))

    start = timeit.timeit()
    print("The H.C.F. of", num1,"and", num2,"is", Euklid_recursive(num1, num2), "(using recursive Euklidian algorithm)")
    end = timeit.timeit()
    print("     Elapsed time: {0:0.4f} sec".format(end - start))