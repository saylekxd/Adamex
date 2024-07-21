data = ['Ola', 'Rafał', 23, 45, 'Daniel', 89, 78, 5]
print(len(data)) #długość listy 8

#wskazując zakres od : do, z pominięciem do!
print(data[0:3]) #'Ola', 'Rafał', 23]
print(data[2:4]) # [23, 45]

print(data[5:]) # [89, 78, 5]

print(data[::2]) #pobieranie co 2 elementu

data[2] = 'Paweł' 
data[3] = 'Ania' #przypisanie do istniejącego elementu listy nowej wartości

del(data[1]) #kasowanie elementu, skasowany 'Rafał"

print(45 in data) #sprawdzenie czy dana wartość istnieje w liście z operatorem in

if 'Ola' in data:
    print('Ola jest w liście data')

for v in data:  
    print (v) #użycie pętli do iteracji, czyli wyświetlania wszystkich elementów z listy

#Listy w listach i odwoływanie się w nich do elementów
data = [['one', 'two', 'three'],['dodge', 'pontiac', 'ford']]

print(data[0][0]) 
print(data[1][2])

#Łączenie list za pomoca operatora konkatanacji czyli +
data1 = ['Ola', 'Ania']
data2 = ['Rafał', 'Kasia','Paweł']

names = data1 + data2

print(names) # połączone dwie listy 

#Wyświeltanie listy kilka razy dzięki *
multiData = data1 * 3 
print(multiData)

# -----------------------------------------


