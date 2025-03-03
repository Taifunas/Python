# Ligonine 

# pacientai
# gydytojai
# vizitai


class Pacientas:

    def __init__(self, vardas, pavarde, ak, email):
        self.vardas = vardas
        self.pavarde = pavarde
        self.ak = ak
        self.email = email

class Gydytojas:

    def __init__(self, vardas, pavarde, specialybe):
        self.vardas = vardas
        self.pavarde = pavarde
        self.specialybe = specialybe
        self.vizitai = []

    def prideti_vizita(self, vizitas):
        self.vizitai.append(vizitas)

    def ar_laisvas(self, data):
        # datos = []
        # for vizitas in self.vizitai:
        #     datos.append(vizitas.data)
        datos = [vizitas.data for vizitas in self.vizitai]
        return data in datos # blogai jeigu grazina True, gerai jeigu grazina False

class Vizitas:

    def __init__(self, pacientas, gydytojas, data, paskirtis, informacija):
        self.pacientas = pacientas
        self.gydytojas = gydytojas
        self.data = data # 2025-02-26
        self.paskirtis = paskirtis
        self.informacija = informacija

class Ligonine:

    def __init__(self, pavadinimas):
        self.pavadinimas = pavadinimas
        self.gydytojai = []
        self.pacientai = []
        self.vizitai = []

    def prideti_gydytoja(self):
        vardas = input('Įveskite gydytojo vardą: ')
        pavarde = input('Įveskite gydytojo pavardę: ')
        specialybe = input('Įveskite gydytojo specialybę: ')
        gydytojas = Gydytojas(vardas, pavarde, specialybe)
        self.gydytojai.append(gydytojas)
        print(f'Gydytojas {gydytojas.vardas} buvo pridėtas')

    def prideti_pacienta(self):
        vardas = input('Įveskite paciento vardą: ')
        pavarde = input('Įveskite paciento pavardę: ')
        ak = input('Įveskite paciento asmens kodą: ')
        email = input('Įveskite paciento el. paštą: ')
        pacientas = Pacientas(vardas, pavarde, ak, email)
        self.pacientai.append(pacientas)
        print(f'Pacientas {pacientas.vardas} buvo pridėtas')
        # print(f'Pacientas {self.pacientai[-1].vardas} buvo pridėtas')

    def rasti_pacienta(self, vardas, pavarde):
        for pacientas in self.pacientai:
            if pacientas.vardas == vardas and pacientas.pavarde == pavarde:
                return pacientas

    def rasti_gydytoja(self, vardas, pavarde):
        for gydytojas in self.gydytojai:
            if gydytojas.vardas == vardas and gydytojas.pavarde == pavarde:
                return gydytojas

    def gauti_specialybes(self):
        specialybes=set()
        for gydytojas in self.gydytojai:
            set.add(gydytojas.specialybe)

    def prideti_vizita(self):
        # pacientas, gydytojas, data, paskirtis, informacija
        p_vardas, p_pavarde = input('Įveskite paciento vardą ir pavardę, atskirdami tarpu').split()
        pacientas = self.rasti_pacienta(p_vardas, p_pavarde)
        while not pacientas:
            print('Pacientas nebuvo rastas!')
            p_vardas, p_pavarde = input('Įveskite paciento vardą ir pavardę, atskirdami tarpu').split()
            pacientas = self.rasti_pacienta(p_vardas, p_pavarde)

        g_vardas, g_pavarde = input('Įveskite gydytojo vardą ir pavardę, atskirdami tarpu').split()
        gydytojas = self.rasti_gydytoja(g_vardas, g_pavarde)
        while not gydytojas:
            print('Gydytojas nebuvo rastas!')
            g_vardas, g_pavarde = input('Įveskite gydytojo vardą ir pavardę, atskirdami tarpu').split()
            gydytojas = self.rasti_gydytoja(g_vardas, g_pavarde)
        while True:
            data = input('Įveskite pageidaujamą vizito datą (YYYY-MM-DD): ')
            if not gydytojas.ar_laisvas(data):
                break
            print('Gydytojas tą dieną užimtas, pasirinkite kitą dieną!')
        paskirtis = input('Įveskite paskirtį: ')
        informacija = input('Papildomi komentarai: ')
        vizitas = Vizitas(pacientas, gydytojas, data, paskirtis, informacija)
        gydytojas.prideti_vizita(vizitas)
        self.vizitai.append(vizitas)
        print('Vizitas sėkmingai pridėtas')
