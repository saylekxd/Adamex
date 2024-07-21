# SET - zestaw to nieuporządkowany zbiór unikalnych wartości 

""" Zestaw nie pozwala na dodanie zduplikowanych elementów, jest iterowalny, zmienny, nie posiada pozycji elementów - indeksu. Jego odmianą jest frozenset, który jest niezmienny, tj. niemutowalny. Zestaw zapisywany jest za pomocą nawiasów klamrowych i wartości po przecinku."""

set = {0, 4, 8, 12, 16}

#dodawanie
set.add(20)

#usunięcie
set.discard(8)

set.add(20) #wartość już jest, więc zostaje pominięta

for value in set:
    print(value)

#Frozenset = podobny do set z tą różnicą, że raz utworozny nie może mieć jakichkolwiek zmain 

set = {0, 4, 8, 12, 16}
frozen = frozenset(set)


