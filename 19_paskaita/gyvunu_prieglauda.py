import datetime

class Gyvunas:

    # init metodas (konstruktorius) yra iškviečiamas objekto kūrimo metu
    # metodas - funkcija deklaruota klases viduje
    # self - leidzia perteikti viso objekto informacija metodui, taip pat suprantame, jog sis veiksmas turi buti vykdomas tam konkrecia objektui
    def __init__(self, gimimo_metai, rusis, vardas, svoris):
        self.gimimo_metai=gimimo_metai
        self.rusis=rusis
        self.vardas=vardas
        self.svoris=svoris
        self.amzius= self.apskaiciuoti_amziu()

    def apskaiciuoti_amziu(self):
        today = datetime.datetime.now()
        return today.year - self.gimimo_metai

class GyvunuPrieglauda():
    def __init__(self, pavadinimas):
        self.pavadinimas=pavadinimas
        self.gyvunai=[]

    def prideti_gyvuna(self, gyvunas):
        self.gyvunai.append(gyvunas)

    def gauti_pagal_rusi(self, rusis):
        return [gyvunas for gyvunas in self.gyvunai if gyvunas.rusis==rusis]
    
    def gauti_pagal_amziu(self, amzius):
        return [gyvunas.__dict__ for gyvunas in self.gyvunai if gyvunas.amzius < amzius]
    
class Kate(Gyvunas): # klase kate paveldi klase gyvunas

    def __init__(self,  gimimo_metai, vardas, svoris, kraikas):
        rusis='kate'
        super().__init__(gimimo_metai, rusis, vardas, svoris) # pateikti visus argumentus, kuriu reikalauja klase gyvunas
        self.kraikas = kraikas

    def kalbeti(self):
        return "miau"

objektas = Gyvunas(2009, 'kate', 'pilka',5)
print(objektas.vardas)
suo=Gyvunas(2015,'suo','Reksas',20)

#print(objektas.apskaiciuoti_amziu())
print(suo.apskaiciuoti_amziu())
print(suo.amzius)

prieglauda1=GyvunuPrieglauda("Lese")
prieglauda1.prideti_gyvuna(objektas)
prieglauda1.prideti_gyvuna(suo)

print(prieglauda1.gyvunai)
print(prieglauda1.gauti_pagal_rusi('kate'))
print(object.__dict__)

print(prieglauda1.gauti_pagal_amziu(12))

print(prieglauda1.gyvunai[0].vardas)

kate1=Kate(2020, 'Garfildas',10,'naturalus')
print(kate1.vardas)
print(kate1.kraikas)
print(kate1.apskaiciuoti_amziu())
print(kate1.kalbeti())