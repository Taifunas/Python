def prideti_islaida():
    data = input('Įveskite datą, tokiu formatu: xxxx-xx-xx: ')
    kategorija = input('Įveskite kategoriją: ')
    suma = input('Įveskite sumą: ')
    with open('islaidos.txt', 'a+') as f:
        f.write(f'{data}, {kategorija}, {suma} \n')
    print()
    print('Išlaida įrašyta!')

def perziureti_islaidas(data=None):
    print()
    if not data:
        data = skaityti_faila()
    for row in data:
        print(' | '.join([el.replace('\n', '') for el in row.split(',')]))

def skaityti_faila():
    with open('islaidos.txt', 'r') as f:
        data = f.readlines()
    return data

def filtruoti_pagal_data(index,data):
    filtruoti = []
    f_data = skaityti_faila()
    for islaida in f_data:
        if islaida.split(',')[index].lstrip() == data:
            filtruoti.append(islaida)
    if filtruoti == []:
        print(f'Išlaidų pagal filtrą {data} nerasta!')
    else:
        print('----------------')
        print('Pagal filtrą rasti įrašai: ')
        perziureti_islaidas(filtruoti)
        print('----------------')

def skaiciuoti_bendra_suma():
    data = skaityti_faila()
    print('Bendra suma: ', end='')
    print(sum( [int(row.split(',')[2].replace('\n','') ) for row in data]))

def islaidu_sekimas():
    while True:
        print('---------------------')
        print('1 - Pridėti naują išlaidą')
        print('2 - Peržiūrėti visas išlaidas')
        print('3 - Filtruoti pagal kategoriją')
        print('4 - Filtruoti pagal datą')
        print('5 - Apskaičiuoti bendrą sumą')
        print('6 - Išeiti')
        print('---------------------')
        pasirinkimas = input('Pasirinkite veiksmą: ')
        if pasirinkimas not in ['1', '2', '3', '4', '5', '6']:
            print('pasirinkimas turi būti 1-6!')
            continue
        if pasirinkimas == '6':
            break
        elif pasirinkimas == '1':
            prideti_islaida()
        elif pasirinkimas == '2':
            perziureti_islaidas()
        elif pasirinkimas == '3':
            data = input('Įveskite kategoriją: ')
            filtruoti_pagal_data(1, data)
        elif pasirinkimas == '4':
            data = input('Įveskite datą formatu YYYY-MM-DD: ')
            filtruoti_pagal_data(0, data)
        elif pasirinkimas == '5':
            skaiciuoti_bendra_suma()

islaidu_sekimas()