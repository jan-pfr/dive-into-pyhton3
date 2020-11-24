Zahlen = []
for x in range(2, 101):
    Zahlen.append(x)
print(f"Das sind alle Zahlen von 2 - 100, inklusive Primzahlen: {Zahlen}")
def createListe(vielfache):
    liste = []
    for i in range(vielfache, 101):
        y = i * vielfache
        if y >= 101:
            break
        else:
            liste.append(y)
            try: Zahlen.remove(y)
            except: pass
    return liste
vielfache = []
for z in range(2, 11):
    vielfache.append(createListe(Zahlen, z))
print(f"Das ist die Liste mit den Primzahlen von 2 bis 100: {Zahlen}")