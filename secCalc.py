# Ziel: gib die Zahl der Sekunden an einem Tag an


SekundenProMinute = 60
Minuten= 60
Stunden= 24
SekundenProStunde = SekundenProMinute * Minuten
SekundenProTag = SekundenProStunde * Stunden

print(SekundenProMinute)
print(SekundenProStunde)
print(SekundenProTag)

str1 = "Ein Tag enthält exakt: "
str2 = " Sekunden."

print(str1 + str(SekundenProTag) + str2) 

'''
print(17 % 3 )

cubes = [1, 8, 27, 65, 125] # something's wrong here
cubes[3] = 4 ** 3 # replace the wrong value
cubes.append(7 ** 3) # and the cube of 7
print(cubes)
for i, v in enumerate( cubes):
 	print(i, v)



knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
 	print(k, v)



# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
	print(w, len(w))
'''
	
n = 12
count = 0
# while-Schleife: solange Kriterium erfüllt ist, wird Schleife durchlaufen
while count < 10: 
	n = n + count
	print(n)
	# Wert der Variablen count wird um 1 erhöht
	count = count + 1



import pandas as pd

df = pd.read_csv('data1.csv')
y=df["Calories"].mode()
print("y: ",y, " Type: ", type(y))
x = df["Calories"].mode()[0]
print("x: ",x, " Type: ", type(x))

df["Calories"].fillna(x, inplace = True)

print(df.to_string())

