config = {
    "website" : "example.com",
    "dbType" : "mysql",
    "dbUser" : "admin",
    "dbPassword" : "12345"
}

print(len(config))

print(config["dbType"])

for key, value in config.items():
    print("Klucz w config: " + key + " z wartością " + value)

for key in config:
    print(key + " " + (config[key]))

print((config[key]))