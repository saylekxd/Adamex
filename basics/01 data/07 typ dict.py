# Dict - słownik 

"""Dict to zbiór par kluczy oraz wartości; klucze muszą być unikalne i slużą do pobrania wartości. Elementy w dict nie maja kolejności, nie jest to lista"""

contacts = {
    "Ania" : "ania@example.com",
    "Daniel" : "daniel@example.com",
    "Ola" : "ola@example.com"
}

print(contacts["Ania"])

#klucze dostępne w słowniku
print(contacts.keys()) 

#wartości dostępne w słowniku
print(contacts.values())

for key in contacts:
    print(key + " " + (contacts[key]))

for key, value in contacts.items():
    print("Klucz w config: " + key + " z wartością " + value)