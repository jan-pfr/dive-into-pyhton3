class Angestellter:
    Name = None
    Wochenstunden = None
    Jahresgehalt = None


    def __init__(self, Name, Wochenstunden, Jahresgehalt):
        self.Name = Name
        self.Wochenstunden = Wochenstunden
        self.Jahresgehalt = Jahresgehalt

    def __str__(self):
        return f'Angestellter {self.Name}, {self.Wochenstunden} Wochenstunden, {self.Jahresgehalt}€ Jahresgehalt'

    def Gehaltsanpassung(self, addValue):
        self.Jahresgehalt = self.Jahresgehalt + addValue

Mitarb1 = Angestellter('Hans Wurst', 35, 50000)
print(Mitarb1)

while Mitarb1.Jahresgehalt <= 70000:
     addValue = Mitarb1.Jahresgehalt * 0.03
     Mitarb1.Gehaltsanpassung(addValue)
     print(f' Neues Gehalt: {Mitarb1.Jahresgehalt}')
