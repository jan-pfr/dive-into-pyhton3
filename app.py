name = "Jan"
surname = "Pfeiffer"
age = 21
notendurchschnitt = 2.3
matrikuliert = True
print("Dein Alter ist " + str(age))
age = input("Ändere dein Alter: ")
message = f"Dein Profil: {name}, {surname} ist {age} Jahre alt, und hat einen Notendurchschnitt von {notendurchschnitt}"
print(message)
print("Länge: " + str(len(message)))
print(message.upper())
print(message.lower())
print(message.find("J"))
print(message.replace("n", "m"))
boolean = "Jan" in message
print(boolean)

geburtsjahr = input("Dein Geburtsjahr: ")
print(type(geburtsjahr))
age = 2020 - int(geburtsjahr)
print(type(age))
print(age)

wight_kg = input("Ihr Gewicht in Kilo: ")
wight_lbs = float(wight_kg) * 2.204
print(wight_lbs)