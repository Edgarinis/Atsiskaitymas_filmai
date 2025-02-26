from app import prisijungimo_input
from app import programa_ijungta

def pagrindinis_meniu():
    while programa_ijungta and prisijungimo_input in ['ziurovas','organizatorius']:
        if prisijungimo_input == 'organizatorius':
            print("""Prisijungta organizatoriaus teisemis. Pasirinkite veiksma:
                    1 - Prideti nauja filma
                    2 - Perziureti filmu sarasa
                    3 - Ieskoti filmo
                    4 - Parodyti esamus seansus
                    5 - Iseiti is programos """)
            veiksmas = (input('Jusu veiksmas: '))
            while veiksmas not in ['1','2','3','4','5']:
                print('Klaida! Iveskite sveikaji skaiciu (1-5) atitinkamam veiksmui atlikti.')
                veiksmas = input('Jusu veiksmas: ')