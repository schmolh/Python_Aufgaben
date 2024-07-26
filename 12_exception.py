import pandas as pd
import os


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


cwd = os.getcwd()

print(cwd)
Filename="Data_dupA.xlsx"
PathFilename=cwd+"\\"+Filename
print(PathFilename)

try:
    df=pd.read_excel(PathFilename)
except Exception as e:
    print("error:", e)
    print("{}Bitte stellen sie sicher, dass das File {} {} {} im der Directory {} {} {} vorhanden ist!{}"
          .format(bcolors.FAIL, bcolors.BOLD , PathFilename, bcolors.FAIL, bcolors.OKBLUE, cwd, bcolors.FAIL, bcolors.ENDC))


