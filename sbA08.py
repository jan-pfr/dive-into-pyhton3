class Angestellter:
    Name = None
    Wochenstunden = None
    Jahresgehalt = None
    def __init__(self, Name, Wochenstunden, Jahresgehalt):
        self.Name = Name
        self.Wochenstunden = Wochenstunden
        self.Jahresgehalt = Jahresgehalt
        print(f'{self.Name} wurde eingestellt; Gehalt: {self.Jahresgehalt}€; Arbeitszeit: {self.Wochenstunden} Stunden')
    def __str__(self):
        return f'Angestellter {self.Name}s Gehalt beträgt {self.Jahresgehalt}€.'
    def Gehaltsanpassung(self, addValue):
        self.Jahresgehalt = self.Jahresgehalt + addValue
        self.Jahresgehalt = round(self.Jahresgehalt, 2)

Mitarb1 = Angestellter('Hans Wurst', 35, 50000)
i = 0

while Mitarb1.Jahresgehalt <= 70000:
     rise = Mitarb1.Jahresgehalt * 0.03
     Mitarb1.Gehaltsanpassung(rise)
     print(f' Neues Gehalt: {Mitarb1.Jahresgehalt}')
     i = i + 1

print(f'{Mitarb1.Name} ist nun {i} Jahre in der Firma.')
print(Mitarb1)
