import math

V = lambda a , b , c : a * b * c * (1 / 3)                                                  #Berechnung des Volumens der Pyramide mit einer Lamda-Funktion

def funcdo( l, b, h):                                                                       #Definition einer Funktion zum Berechnen der Diagonalen und der Oberfläche mit anschließender Ausgabe
    d = lambda l , b , h : math.sqrt(l ** 2 + b ** 2 + h ** 2)           
    O = lambda l , b , h : 2 * (l * b + l * h + b * h)
    print(d(l , b , h))
    print(O(l , b , h))

while True:
    l,b,h = input("Länge, Breite, Höhe jeweils mit einem Leerzeichen getrennt nacheinander eintragen.").split()
    try:
        l = float(l)
        b = float(b)
        h = float(h)
        if l > 0 and b > 0 and h > 0:                                                       #Test ob die eingegebenen Werte gültig sind wenn ja kommt der Break und somit das Ende der While True
            break
        elif l == 0 or b == 0 or h == 0:                                                    #Untersortieren der Fehlermeldungen je nach Kriterium
            print("One of the given numbers equals zero")
        else:
            print("One of the given numbers is negative")
    except:
        print("There is a string Error")

print(V(l , b , h))                                                                         #Aufrufen der vorher definierten Funktion
funcdo(l,b,h)