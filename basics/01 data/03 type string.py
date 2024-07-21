str = "Hello world!"
print(str);
print( len(str)) #ilość znaków
print( type(str))

print( str[0:5] ) #Hello

strX3 = str * 3
print(strX3)

str2 = str + "and Hello again"
print(str2)

print(str2[6:]) #World! and Hello again!

print(str2[::3]) #HlWl deogn (co trzecia litera)

multiLine = """Pierwesza liina
Druga linia
Trzecia linia
"""

print(multiLine)

multiLine2 = "Pierwsza linia\nDruga linia \nTrzecia \t \"linia\""
print(multiLine2)





