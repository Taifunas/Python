import random
import sqlite3
class Saskaita:
    def __init__(self,savininko_vardas,saskaitos_nr, saskaitos_likutis = 0):
        self.savininko_vardas = savininko_vardas
        self.saskaitos_nr = saskaitos_nr
        self.likutis = saskaitos_likutis

    def inesti_pinigu(self,inesama_suma):
        self.likutis = self.likutis + inesama_suma
        with sqlite3.connect('bankas.db') as conn:
            c = conn.cursor()
            c.execute(f"UPDATE saskaita SET likutis = {self.likutis} WHERE savininko_vardas = '{self.savininko_vardas}' and saskaitos_nr = '{self.saskaitos_nr}'")

    def nusiimti_pinigu(self,suma):
        try:    
            if suma > self.likutis:
                raise Exception('Nepakankamas likutis!')
            else:
                 self.likutis = self.likutis - suma
                 self.atnaujinti_likuti()
        except Exception as e:
            print(e)
        
    def atnaujinti_likuti(self):
        with sqlite3.connect('bankas.db') as conn:
            c = conn.cursor()
            c.execute(f"UPDATE saskaita SET likutis = {self.likutis} WHERE savininko_vardas = '{self.savininko_vardas}' and saskaitos_nr = '{self.saskaitos_nr}'")



    def parodyti_likute(self):
         print(self.likutis)

class Bankas:
     
    def __init__(self):
          self.saskaitos = []
          self.nuskaityti_saskaitas()

    def prideti_saskaita(self,saskaita):
         self.saskaitos.append(saskaita)
         with sqlite3.connect('bankas.db') as conn:
             c = conn.cursor()
             c.execute('INSERT INTO saskaita (savininko_vardas, saskaitos_nr, likutis) VALUES (?,?,?)', (saskaita.savininko_vardas, saskaita.saskaitos_nr, saskaita.likutis))


    def gauti_saskaita(self,s_vardas,s_numeris):
        try:
            for saskaita in self.saskaitos:
                if s_vardas == saskaita.savininko_vardas and s_numeris == saskaita.saskaitos_nr:
                   return saskaita
            raise Exception('Tokia saskaita neegzistuoja!')
        except Exception as e:
            print(e)
    
    def nuskaityti_saskaitas(self):
        with sqlite3.connect('bankas.db') as conn:
            c = conn.cursor()
            saskaitos = c.execute('SELECT * FROM saskaita')
        for saskaita in saskaitos:
            n_saskaita = Saskaita(saskaita[1], saskaita[2], saskaita[3])
            self.saskaitos.append(n_saskaita)
            

with sqlite3.connect('bankas.db') as conn:
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS saskaita(id INTEGER PRIMARY KEY AUTOINCREMENT, savininko_vardas VARCHAR(50), saskaitos_nr VARCHAR(11), likutis FLOAT)')

bankas = Bankas()

while True:
     print("------------")
     print("0 - baigti darba.")
     print("1 - atidaryti saskaita ")
     print("2 - valdyti saskaita ")
     print("------------")
     pasirinkimas = input('Pasirinkite ka norite atlikti: ')
     if pasirinkimas == '0':
          break
     elif pasirinkimas == '1':
        savininko_vardas = input("Įveskite savininko vardą: ")
        saskaitos_nr = 'LT0000' + str(random.randint(10000,100000))
        saskaita = Saskaita(savininko_vardas,saskaitos_nr)
        bankas.prideti_saskaita(saskaita)
        print(f'saskaita buvo sekmingai prideta! {saskaitos_nr}')
     elif pasirinkimas == '2':
        savininko_vardas = input("Įveskite savininko vardą: ")
        saskaitos_nr = input('Iveskite saskaitos numeri: ')
        saskaita = bankas.gauti_saskaita(savininko_vardas,saskaitos_nr)
        while saskaita:
            print("------------")
            print("0 - baigti darba.")
            print("1 - perziureti likuti ")
            print("2 - prideti pinigu ")
            print("3 - nusiimti pinig ")
            print("------------")
            s_pasirinkimas = input('Pasirinkite ka norite atlikti: ')       
            if s_pasirinkimas == '0':
                 break
            elif s_pasirinkimas == '1':
                 print(saskaita.likutis)
            elif s_pasirinkimas == '2':
                 suma = int(input('iveskite suma, kuria norite prideti: '))
                 saskaita.inesti_pinigu(suma)
            elif s_pasirinkimas == '3':
                 suma = int(input('iveskite suma, kuria norite nusiimti: '))
                 saskaita.nusiimti_pinigu(suma)    
