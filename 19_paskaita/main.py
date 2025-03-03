from ligonine import Ligonine, Pacientas, Vizitas, Gydytojas

def pasirinkimai():
    print('----------------')
    print('0 - baigti darbą')
    print('1 - pridėti gydytoją')
    print('2 - pridėti pacientą')
    print('3 - pridėti vizitą')
    print('4 - pridėti vizitą')
    print('----------------')

ligonine = Ligonine("Santariškės")
pacientas = Pacientas('Angele', 'Rasuole', 43030303030, 'a.rasuole@gmail.com')
gydytojas = Gydytojas('Antanas', 'Smetona', 'Chirurgas')
vizitas = Vizitas(pacientas, gydytojas, '2025-02-27', 'konsultacija', 'peršalimas')
gydytojas.prideti_vizita(vizitas)
ligonine.gydytojai.append(gydytojas)
ligonine.pacientai.append(pacientas)
ligonine.vizitai.append(vizitas)

while True:
    pasirinkimai()
    pasirinkimas = input('Pasirinkite veiksmą: ')
    if pasirinkimas == '0':
        break
    elif pasirinkimas == '1':
        ligonine.prideti_gydytoja()
    elif pasirinkimas == '2':
        ligonine.prideti_pacienta()
    elif pasirinkimas == '3':
        ligonine.prideti_vizita()