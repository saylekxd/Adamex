#Mutowalność vs niemutowalność 

""""Type w Python można podzielić na dwie kategorie: mutowalne oraz niemutowalne. 

Mutowalne to takie których wartość można zmienić,natomiast typy niemutowalne to wartość której nie można zmienić.

Do rozważań wykorzystamy specjalna funkcję id(), która zwraca unikalany identyfikator dla każdego przekazanego obiektu, w praktyce jest to liczba całkowita określająca miejsce w pamięci, gdzie przechowywana jest wartość. Pamiętajmy, że w Python wszystko jest obiektem, np. liczby całkwoite, float, tuple, itd."""

a = 1 
b = 2 

print(id(a))
print(id(b))

"""Kolejny przykłąd pokazuje niemutowalność liczb całkowitych - tak samo zachowują się float,bool, str, Tuple, frozenset, czyli ich wartośći nie można zmienic. Jakiekolwiek operacje na nich tworzą nową wartosć w pamięci."""

a = 1
addr1 = id(a)

a += 1
addr2 = id(a)

print(addr1)
print(addr2)

#Obiekty mutowalne mogą być zmienione z zachowaniem tego samego miejsca w pamięci (list, set, dict). 

listData = ['a', 'b']
addr3 = id(listData)

listData += ['c', 'd']
addr4 = id(listData)

print(addr3)
print(addr4)
print(addr3 == addr4)
