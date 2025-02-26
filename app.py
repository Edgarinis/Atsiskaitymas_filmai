print('')
import pickle
import datetime
from klases.filmai import Filmas
from klases.seansai import Seansas
from klases.organizatorius import Organizatorius
from klases.ziurovas import Ziurovas

def tuscias_input(ivestis):
    if ivestis == '':
        return True
    else:
        return False

#   Uzkraunami pickle failai paleidus programa
Organizatorius.videotekos_inicializacija()
Organizatorius.seansu_inicializacija()
while True:
    prisijungimo_input = str(input("Prisijunkite kaip 'organizatorius' arba 'ziurovas': "))
    if prisijungimo_input in ['organizatorius', 'ziurovas']:
        break
    print("Klaida! Prisijunkite kaip 'organizatorius' arba 'ziurovas'. ")
programa_ijungta = True
#========================= ORGANIZATORIAUS MAIN MENU ===============================================================================
while programa_ijungta:
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
#========================= PRIDETI FILMA ===============================================================================
        if veiksmas == '1':       # Prideti filma
            print('Prideti filma.\n')
            while True:
                pavadinimas = input('Iveskite pavadinima: ')
                if tuscias_input(pavadinimas):
                    print('Pavadinimo langelis negli buti tuscias. Iveskite bent 1 simboli.')
                else:
                    break
            while True:
                try:
                    trukme = int(input('Iveskite trukme minutemis: '))
                    if trukme <= 0:
                        print('Trukme turi buti daugiau nei 0!')
                    elif trukme > 300:
                        print('Trukme negali buti daugiau nei 300(5 valandos!')
                    else:
                        break
                except ValueError:
                    print('Neteisinga ivestis. Trukme turi buti nurodyta minutemis(sveikasis skaicius).')
            while True:
                zanras = input('Iveskite zanra: ')
                if not zanras.isalpha():
                    print('Ivesties klaida.Zanre negali buti simboliu ne is abeceles.')
                else:
                    break
            while True:
                rezisierius = input('Iveskite rezisieriu: ')
                if tuscias_input(rezisierius):
                    print('Ivestis negali buti tuscia.')
                else:
                    break
                
            while True:
                try:
                    isleidimo_m = int(input('Iveskite isleidimo metus: '))
                    if isleidimo_m < 1878:
                        print("Metai neteisingi! Pirmasis filmas buvo isleistas 1878 pavadinimu 'The Horse in Motion'")
                    elif isleidimo_m > datetime.datetime.now().year:
                        print(f'Metai neteisingi! Dabar juk {datetime.datetime.now().year}')
                    else:
                        break
                except ValueError:
                    print("Isleidimo metai ivesti neteisingai! Tai turi buti sveikas skaicius.")
            while True:
                try:
                    amziaus_reitingas = int(input('Iveskite amziaus reitinga: N - '))
                    if amziaus_reitingas < 0:
                        print('Amzius negali buti neigiamas!')
                    elif amziaus_reitingas > 18:
                        print('Didziausias amziaus reitingas yra 18 (pilnametyste).')
                    else:
                        break
                except ValueError:
                    print("Klaida ivestuose metuose! Iveskite sveika skaiciu.")
            pridedamas_filmas = Filmas(pavadinimas,trukme,zanras,rezisierius,isleidimo_m,amziaus_reitingas)
            Organizatorius.prideti_filma(pridedamas_filmas) 
#========================= 2 FILMU ATVAIZDAVIMAS ===============================================================================
        elif veiksmas == '2':     # Filmu saraso atvaizdavimas
            zodynas_is_failo = Organizatorius.perziureti_filmus()
            print('Filmu sarasas:')
            for filmas in zodynas_is_failo:
                print(filmas)
            saraso_submenu = (input('Tolimesnis veiksmas:\n1. Pasalinti filma pagal pavadinima \n2. Atnaujinti filmu duomenis\n3. Filtruoti\n4. Sukurti seansa\n5. Grizti\nJusu pasirinkimas: '))
            while saraso_submenu not in ['1','2','3','4','5']:
                print('Klaida! Iveskite sveikaji skaiciu (1-5) atitinkamam veiksmui atlikti.')
                saraso_submenu = input('Jusu veiksmas: ')
                #======================= 1 FILMU ATVAIZDAVIMO SUB-MENU / Filmo istrynimas =========================================================
            if saraso_submenu == '1': #Filmo istrynimas
                while True:
                    trinamo_filmo_pavadinimas = input('Iveskite norimo istrinti filmo pavadinima arba spauskite ENTER, kad griztumete i meniu: ')
                    if Organizatorius.istrinti_filma(trinamo_filmo_pavadinimas) == True:
                        print(f"Filmas '{trinamo_filmo_pavadinimas}' sekmingai istrintas.")
                        break
                    else:
                        print("Toks filmo pavadinimas neegzistuoja. Bandykite dar karta arba spauskite ENTER, kad griztumete i meniu.")
                        if trinamo_filmo_pavadinimas == '':
                            break
                #======================= 2 FILMU ATVAIZDAVIMO SUB-MENU / Atributo keitimas =========================================================
            elif saraso_submenu == '2':     #Atributo keitimas
                atnaujinamas_filmas = input('Iveskite norimo atnaujinti filmo pavadinima: ')
                rastas_filmas = Organizatorius.ieskoti_filmo(atnaujinamas_filmas)
                if not rastas_filmas:
                    print('Tokio filmo pavadinimo nera.')
                else:
                    filmas = rastas_filmas[0] #naudojam su indeksu nes paieskos metodas grazina sarasa.
                    print(filmas)
                    print("1. Pavadinimas\n2. Trukme\n3. Zanras\n4. Rezisierius\n5. Isleidimo metai\n6. Amziaus reitingas")
                    keiciamas_parametras = input('Keiciamas parametras (1-6): ')
                    if keiciamas_parametras == '1':
                        filmas.pavadinimas = input('Iveskite nauja pavadinima: ')
                    elif keiciamas_parametras == '2':
                        filmas.trukme = input('Iveskite nauja trukme: ')
                    elif keiciamas_parametras == '3':
                        filmas.zanras = input('Iveskite nauja zanra: ')
                    elif keiciamas_parametras == '4':
                        filmas.rezisierius = input('Iveskite nauja rezisieriu: ')
                    elif keiciamas_parametras == '5':
                        filmas.isleidimo_m = input('Iveskite naujus isleidimo metus: ')
                    elif keiciamas_parametras == '6':
                        filmas.amziaus_reitingas = input('Iveskite nauja amziaus reitinga: ')
                    with open("filmu_biblioteka_pickle.pickle", "wb") as failas:
                        pickle.dump(Organizatorius.filmu_biblioteka, failas)
                    print("Filmo duomenys atnaujinti.")
                #======================= 3 FILMU ATVAIZDAVIMO SUB-MENU / Filtravimas =========================================================
            elif saraso_submenu == '3':     #Filtravimas
                zanrofiltras = input('Filtravimas pagal zanra. Iveskite pageidaujama zanra: ')
                for filmas in Organizatorius.filmu_biblioteka:
                    if zanrofiltras.lower() in filmas.zanras.lower():
                        print(filmas)
                #======================= 4 FILMU ATVAIZDAVIMO SUB-MENU / Seanso pridejimas =========================================================
            elif saraso_submenu == '4': #Seanso pridejimas
                filmas_seansui_input = input('Parasykite pavadinima filmo, kuriam norite sukurti seansa: ')
                rastas_seansui = Organizatorius.ieskoti_filmo(filmas_seansui_input)
                if not rastas_seansui:
                    print('Tokio filmo pavadinimo nera.')
                else:
                    filmas1 = rastas_seansui[0] # Naudojam 0 nes mums returnina sarasa
                    print(f'Pasirinktas filmas: {filmas1.pavadinimas}, {filmas1.zanras}, Metai:{filmas1.isleidimo_m}, N-{filmas1.amziaus_reitingas}')
                    savaites_diena = input('Kelintadieni rodysite?: ')
                    valanda = input('Valanda: ')
                    minute = input('Minutes: ')
                    vietu_sk = input('Kedziu skaicius:')
                    sutampa = False
                    for seansas in Organizatorius.seansai:
                        if seansas.diena == savaites_diena and seansas.valanda == valanda and seansas.minute == minute:
                            sutampa = True
                            break
                    if sutampa:
                        print('Seansas nepridetas. Tuo laiku rodomas kitas filmas!')
                    else:
                        print(f"Seansas pridetas.Filma '{filmas1.pavadinimas}' rodysime: {savaites_diena} {valanda}:{minute}")
                        Organizatorius.prideti_seansa(filmas1,savaites_diena,valanda,minute,vietu_sk)
                #================================================================================
            elif saraso_submenu == '5': # Grizti i  pagrindini meniu
                continue
#========================= 3 FILMU PAIESKA ===============================================================================
        elif veiksmas == '3':     # Filmu ieskojimas
            while True:
                paieskos_ivestis = input('Iveskite paieskos termina(rezisieriu arba pavadinima): ')
                if len(paieskos_ivestis) < 2:
                    print('Paieskos raktazodziui turite ivesti bent 2 simbolius!')
                elif len(paieskos_ivestis) > 1:
                    break
            surasti_filmai = Organizatorius.ieskoti_filmo(paieskos_ivestis)
            if surasti_filmai == False:
                print('Tokio filmo repertuare nera')
            else:
                print(f'Paieskos rezultatai ({len(surasti_filmai)}):')
                for filmas in surasti_filmai:
                    print(filmas)
                print('')
#========================= 4 SEANSU ATVAIZDAVIMAS ===============================================================================
        elif veiksmas == '4': # Parodyti seansus
            print('Seansu sarasas:')
            for seansas in Organizatorius.seansai:
                print (seansas)
#========================= 5 UZDARYTI PROGRAMA =================================================================================
        elif veiksmas == '5': # Exit
            print('Viso gero.')
            programa_ijungta = False
            break
        else:
            print('Neteisinga ivestis. Rinkites veiksma 1-4.')
#=================================================================================================================================
#==================     ZIUROVO MENU        ======================================================================================
#=================================================================================================================================
    elif prisijungimo_input == 'ziurovas':
        print(
            """Prisijungta ziurovo teisemis. Pasirinkite veiksma:
    1 - Perziureti filmu sarasa
    2 - Ieskoti filmo
    3 - Parodyti esamus seansus
    4 - Iseiti is programos""")
        veiksmas = (input('Jusu veiksmas: '))
        while veiksmas not in ['1','2','3','4']:
            print('Klaida! Iveskite sveikaji skaiciu (1-4) atitinkamam veiksmui atlikti.')
            veiksmas = input('Jusu veiksmas: ')
#========================= 1 FILMU SARASAS =================================================================================
        if veiksmas == '1': #Filmu sarasas
            zodynas_is_failo = Organizatorius.perziureti_filmus()
            for filmas in zodynas_is_failo:
                print(filmas)

            saraso_submenu = (input("""Tolimesnis veiksmas:
    1. Filtruoti
    2.Ivertinti špilma
    3.Grizti
    Jusu pasirinkimas: """))
            while saraso_submenu not in ['1','2','3']:
                print('Klaida! Iveskite sveikaji skaiciu (1-4) atitinkamam veiksmui atlikti.')
                saraso_submenu = input('Jusu veiksmas: ')
            if saraso_submenu == '1':   #Filtravimas
                zanrofiltras = input('Filtravimas pagal zanra. Iveskite pageidaujama zanra: ')
                print(f"Atfiltruota pagal '{zanrofiltras}' zanra:")
                for filmas in Organizatorius.filmu_biblioteka:
                    if zanrofiltras.lower() in filmas.zanras.lower():
                        print(filmas)
#=========================  IVERTINTI FILMA =================================================================================
            elif saraso_submenu == '2':
                ziurovas = Ziurovas(amzius = 18)
                vertinamas_filmas = input('Iveskite norimo ivertinti filmo pavadinima: ')
                surastas_ivertinimui = Organizatorius.ieskoti_filmo(vertinamas_filmas)
                if not surastas_ivertinimui:
                    print('Tokio filmo pavadinimo nera.')
                else:
                    try:
                        ivertinimas = int(input(f"Ivertinkite filma '{vertinamas_filmas}' skaleje 1 - 10:  "))
                        ziurovas.ivertinti(vertinamas_filmas,ivertinimas)
                    except ValueError:
                        print('Neteisinga ivestis. Iveskite sveika skaiciu nuo 1 iki 10.')
            elif saraso_submenu == '3':
                continue

#=========================  IESKOTI FILMO =================================================================================
        elif veiksmas == '2': #Ieskoti filmo
            while True:
                paieskos_ivestis = input('Iveskite paieskos termina(rezisieriu arba pavadinima): ')
                if len(paieskos_ivestis) < 2:
                    print('Paieskos raktazodziui turite ivesti bent 2 simbolius!')
                elif len(paieskos_ivestis) > 1:
                    break
            surasti_filmai = Organizatorius.ieskoti_filmo(paieskos_ivestis)
            if surasti_filmai == False:
                print('Tokio filmo repertuare nera')
            else:
                print(f'Paieskos rezultatai ({len(surasti_filmai)}):')
                for filmas in surasti_filmai:
                    print(filmas)
                print('')
#========================= 3 SEANSU SARASAS =================================================================================
        elif veiksmas == '3': # Ismeta seansu sukurtu sarasa
            print('Seansu sarasas:')
            eil_nr = 1
            for filmas in Organizatorius.seansai:
                print (f'{eil_nr}. {filmas}')
                eil_nr = eil_nr +1
            print ('\n1. Atlikti rezervacija\n2. Ivertinti filma\nENTER - grizti.')
            
            seansu_submenu = input('Jusu veiksmas: ')
            if seansu_submenu == '1':
                try:
                    pasirinktas_seansas = int(input(f'Pasirinkite seansa rezervacijai, nuo 1 iki {len(Organizatorius.seansai)}: ')) - 1
                    if pasirinktas_seansas >= 0 and pasirinktas_seansas < len(Organizatorius.seansai):
                        rezervuotas_seansas = Organizatorius.seansai[pasirinktas_seansas]
                        print(f'Rezervuota vieta seansui: {rezervuotas_seansas}')
                        Ziurovas.rezervuoti_bilietus(pasirinktas_seansas)
                    else:
                        print('Klaida! Nera tokio numerio.')
                except ValueError:
                    print('Klaidinga ivestis. Ivestis turi buti sveikas skaicius.')
#========================= 4 ISJUNGIAM PROGRAMA =================================================================================
        elif veiksmas == '4':
            print('Viso gero')
            programa_ijungta = False

