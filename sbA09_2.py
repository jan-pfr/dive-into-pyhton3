class Angestellter:
    Name = None
    Wochenstunden = None
    Jahresgehalt = None

    def __init__(self, Name, Wochenstunden, Jahresgehalt):
        self.Name = Name
        self.Wochenstunden = Wochenstunden
        self.Jahresgehalt = Jahresgehalt
        #print(f'{self.Name} wurde eingestellt; Gehalt: {self.Jahresgehalt}€; Arbeitszeit: {self.Wochenstunden} Stunden')

    def __str__(self):
        return f'Angestellter {self.Name}s Gehalt beträgt {self.Jahresgehalt}€.'

    def Gehaltsanpassung(self, addValue):
        self.Jahresgehalt = self.Jahresgehalt + addValue
        self.Jahresgehalt = round(self.Jahresgehalt, 2)


class Tarifmitarbeiter(Angestellter):
    KSchutz = True

    def __init__(self, Name, Wochenstunden, Jahresgehalt):
        self.Name = Name
        self.Wochenstunden = Wochenstunden
        self.Jahresgehalt = Jahresgehalt


class ATMitarbeiter(Angestellter):
    KSchutz = False

    def __init__(self, Name, Wochenstunden, Jahresgehalt):
        self.Name = Name
        self.Wochenstunden = Wochenstunden
        self.Jahresgehalt = Jahresgehalt
        print(f'{self.Name} wurde eingestellt; Gehalt: {self.Jahresgehalt}€; Arbeitszeit: {self.Wochenstunden} Stunden')


Mitarb1 = ATMitarbeiter('Hans Wurst', 35, 50000)
print(Mitarb1)
