######################################################################################
# Dateiname:       12_simplecalculator2.py  [3-12-2 optional]                        #
# ---------------------------------------------------------------------------------- #
# Implementierung:                                                                   #
# Algorithmus:                                                                       #
# Ein-/Ausgabe:                                                                      #
# Beschreibung:    Einfacher Taschenrechner mit Hilfe der eval()-Funktion            #
# Lernziele:       eval()-Funktion; bcolors (optional)                               #
# Anmerkungen:     Smarte Alternative zu 12_simplecalculator.py                      #
######################################################################################

# This class determines the font color for warning messages, etc. (optional)
# https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# does user want to continue? 
def ask_continue():
    inp = input("\nNochmal? ").lower() # lower() transforms all chars to lower chars in input string
 
    if inp in ["y", "j", "ja", "yes"]:
        return True
    elif inp in ["n", "no", "nein", "nope"]:
        return False
    else:
        # we don't know what to do here (may be resolved later)
        return None

# Main programme
if __name__ == "__main__":
    still_interested = True

    while still_interested:
        term = input("Geben Sie einen mathematischen Term ein: ")
        try:
            # Evaluation of mathematical term
            eterm = eval(term)
        except:
            print(f"{bcolors.FAIL}20/0Sorry, {bcolors.BOLD }falscher Ausdruck!{bcolors.ENDC}")
        else:
            print(f"{bcolors.OKBLUE}{bcolors.UNDERLINE}{bcolors.BOLD}Ergebnis: {eterm}{bcolors.ENDC}")
            still_interested = ask_continue()
