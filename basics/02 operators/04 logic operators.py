#Operatory logiczne

"""Operatory logiczne umożliwaja łączenie wielu porównań, aby uzyskać jedną ostateczną wartosć logiczną: True albo False. ZWykle stosowane są w instrukcjach warunkowych oraz pętlach.

Operator and zwraca wartość True, jeśli obie strony wyrażenia mają wartość true"""

print(True and True)
print(True and False)
print(False and False)

print( 8 > 3 and 3 == 3) #True, bo obie strony zwracają True
print(4 >= 4 and 1 >= 10)

if 5 == 5 and 10 > 4:
    print("True, bo oba warunki są spełnione")

"Operator logiczny or zwraca wartosć True, jeśli przynajmniej jedna ze stron zwróci True; czyli or zwróci False jeśli obie strony mają False."

print( True or True) #True
print(True or False) #True
print(False or False) #False

print(3 < 5 or 7 == 7) #True
print(10 == 11 or 2 < 1) #False

if "Ania" == "Ania" or 10 == 1:
    print("Ania to Ania")

"Operator not odwraca wartość logiczną; jeśli była True to staje się False i na odwrót."

print (not True) #False
print(not False) #True

print(not (10 == 10)) #False
print(not(4 < 1)) #True
print (not(5 == 5 and 3 > 1)) #False

taskCompleted = False #Pamiętaj, żeby pisać False lub True z dużej litery

if not taskCompleted:
    print("Zadanie nie zostało wykonane.")
