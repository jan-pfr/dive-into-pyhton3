#### Öffnen der Presliste.txt und Aufteilung in 2 Listen ###

preisliste = open("Preisliste.txt", "r") # Öffnen der Datei im Readmode
produkte = preisliste.readline() # Auslesen der ersten Zeile
produkte = produkte.strip() # Entfernen des 'Enter' Am Ende dieser Zeile
produkte = produkte.split("; ") # Aufspliten und Umwandlung in eine Liste
print(produkte) # Ausgabe zur Überprüfung, dass es sich um eine Liste handelt

preise = preisliste.readline() # Auslesen der zweiten Zeile
preise = preise.split("; ") # Aufspliten und Umwandlung in eine Liste
print(preise)  # Ausgabe zur Überprüfung, dass es sich um eine Liste handelt

preisliste.close() # Ordnungsgerechtes schließen der Datei

#### Öffnen / Erstellen der Datei Ausgabe.txt und Einfügen der Werte in 2 Spalten ####

ausgabe = open("Ausgabe.txt", "w") # Öffnen der Ausgabe im Writemode. Die Datei wird erstellt, wenn sie noch nicht existiert
for x in range(len(produkte)):
    ausgabe.write(f"{produkte[x]} {preise[x]}€\n") # Schreiben der Liste nach Vorgabe

ausgabe = open("Ausgabe.txt", "r")
print(ausgabe.read()) # Ausgabe zur Überprüfung
ausgabe.close()

#### Öffnen der Datei Ausgabe.txt um deren Inhalt zu ectrahieren, zu ändern und in eine neue Datei zu schreiben ####

anzahlZeilen = sum(1 for line in open('Ausgabe.txt')) # Erfassung Anzahl der Zeilen in der Datei

eingabe = open("Ausgabe.txt", "r") # Öffnen der Ausgabe.txt
produkte2 = []
preise2 = []
for y in range(anzahlZeilen): # Aufteilen der Preisliste wieder auf 2 seperate Listen
    tmp = eingabe.readline()

    tmp = tmp.split()
    print(tmp)
    produkte2.append(tmp[0])
    preise2.append(tmp[1])
produkte2[0] = "Wurst"
preise2[0] = "1,99€"
eingabe.close()

ausgabe2 = open("Ausgabe2.txt", "w") # Öffnen der Ausgabe im Writemode. Die Datei wird erstellt, wenn sie noch nicht existiert
for x in range(len(produkte2)):
    ausgabe2.write(f"{produkte2[x]} {preise2[x]}\n") # Schreiben der 2. Liste nach Vorgabe

ausgabe2 = open("Ausgabe2.txt", "r")
print(ausgabe2.read()) # Ausgabe zur Überprüfung
ausgabe2.close()


