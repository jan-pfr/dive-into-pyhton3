n = True
while 1:
    try:
        h = input("Höhe: ")
        h = int(h)
        h = float(h)
    except ValueError: print("Die Eingabe erfordert eine Zahl oder Float")
    print(h)

l = input("Länge: ")
b = input("Breite: ")