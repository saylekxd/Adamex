#Tuples 
""""Krotka to uporządkowana sekwencja danych, niezmienna kolekcja tworzona za pomoca nawiasów okrągłych oraz elementów oddzielonych przecinkiem. Krotkę najlepiej wyborazić sobie jako rekord w bazie odnośnie użytkownika; jego login, email, datę rejestracji itd."""

data = ("one", "two", "three")
print(type(data)) #<class 'tuple'>

#(bez nawiasów)
cars = "GMC", "Pontiac", "Ford" 

#pusta typles musi mieć nawiasy
names = ()

#zawierająca tylko jeden element musi mieć ppo nim przecinek
fighters = ("F16",)

#Tuples jest niemutowalna, czyli nie można zmieniać jej wartości (!)
data = ("one", "two", "three")
#data[1] = "test" 
#del data

# ------------------------------------


