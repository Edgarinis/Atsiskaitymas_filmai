print('')
import pickle
import datetime

class Filmas:
    def __init__(self,pavadinimas,trukme,zanras,rezisierius,isleidimo_m,amziaus_reitingas = 8):
          self.pavadinimas = pavadinimas
          self.trukme = trukme
          self.zanras = zanras
          self.rezisierius = rezisierius
          self.isleidimo_m = isleidimo_m
          self.amziaus_reitingas = amziaus_reitingas
    def __str__(self):
        return (f"Filmas: {self.pavadinimas} |Trukme: {self.trukme} |Zanras: {self.zanras} |Rezisierius: {self.rezisierius} |Metai: {self.isleidimo_m} |PEGI-{self.amziaus_reitingas}")

class Organizatorius:
    filmu_biblioteka = []
    seansai = []

    def __init__(self,organizatoriaus_vardas):
         self.organizatoriaus_vardas = organizatoriaus_vardas
    def videotekos_inicializacija():
        with open("filmu_biblioteka_pickle.pickle","rb") as failas:
            Organizatorius.filmu_biblioteka = pickle.load(failas)
    def seansu_inicializacija():
        with open("seansu_biblioteka_pickle.pickle","rb") as seansu_failas:
            Organizatorius.seansai = pickle.load(seansu_failas)
    def perziureti_filmus():
        with open("filmu_biblioteka_pickle.pickle","rb") as failas:
            filmu_sarasas_is_failo = pickle.load(failas) #pickle.dump(turinys,failas) //PRIDETA dump
            return filmu_sarasas_is_failo
    def prideti_filma(filmas): # saugosim filmus kaip objektus
        try:
            Organizatorius.filmu_biblioteka.append(filmas)
            with open("filmu_biblioteka_pickle.pickle","wb") as failas:
                pickle.dump(Organizatorius.filmu_biblioteka,failas)
            return True
        except ValueError:
            raise Exception ('Isleidimo metai privalo buti sveikas skaicius!')
    def ieskoti_filmo(ieskomas_raktazodis):
        atitinkantys_paieska = []
        for filmas in Organizatorius.filmu_biblioteka:
                if ieskomas_raktazodis.lower() in filmas.pavadinimas.lower() or ieskomas_raktazodis.lower() in filmas.rezisierius.lower():
                    atitinkantys_paieska.append(filmas)
        if atitinkantys_paieska: # Cia patikrina ar isvis yra kazkas sarase ar ne (TRUE jeigu yra)
            return atitinkantys_paieska
        else:
            return False

    def istrinti_filma(raktazodis):
        rastas = False
        for filmas in Organizatorius.filmu_biblioteka.copy():
            if raktazodis.lower() in filmas.pavadinimas.lower() and raktazodis != '':
                Organizatorius.filmu_biblioteka.remove(filmas)
                rastas = True
        if rastas == True:
            with open("filmu_biblioteka_pickle.pickle","wb") as failas:
                pickle.dump(Organizatorius.filmu_biblioteka,failas)
                return True
        elif rastas == False:
            return False

    def prideti_seansa(filmas,diena,valanda,minutes):
        laikas = f'{diena}, {valanda}:{minutes}'
        Organizatorius.seansai.append({str(filmas):laikas})
        with open("seansu_biblioteka_pickle.pickle","wb") as seansu_failas:
            pickle.dump(Organizatorius.seansai,seansu_failas) #pickle.dump(turinys,failas) //PRIDETA dump
        return True

class Ziurovas:
    def __init__(self,amzius):
          self.vartotojo_vardas = amzius
    def perziureti_filmus(self):
        with open("filmu_biblioteka_pickle.pickle","rb") as failas:
            bible_is_failo = pickle.load(failas) #pickle.dump(turinys,failas) //PRIDETA dump
            return bible_is_failo
    def rezervuoti_bilietus(self):
         pass
    def ieskoti_filmo(ieskomas_raktazodis):
        i = 0
        while i < len(Organizatorius.filmu_biblioteka):
                if ieskomas_raktazodis in Organizatorius.filmu_biblioteka[i]["Pavadinimas"] or ieskomas_raktazodis in Organizatorius.filmu_biblioteka[i]["Rezisierius"]:
                    return Organizatorius.filmu_biblioteka[i]
                i = i + 1

#   Uzkraunami pickle failai paleidus programa
Organizatorius.videotekos_inicializacija()
Organizatorius.seansu_inicializacija()
# while True:
#     prisijungimo_input = str(input("Prisijunkite kaip 'organizatorius' arba 'ziurovas': "))
#     if prisijungimo_input in ['organizatorius', 'ziurovas']:
#         break
#     print("Klaida! Prisijunkite kaip 'organizatorius' arba 'ziurovas'. ")
prisijungimo_input = 'organizatorius'
programa_ijungta = True
while programa_ijungta:
    if prisijungimo_input == 'organizatorius':
        print("""Prisijungta organizatoriaus teisemis. Pasirinkite veiksma:
                1 - Prideti nauja filma
                2 - Perziureti filmu sarasa
                3 - Ieskoti filmo
                4 - Iseiti is programos 
                5 - Parodyti esamus seansus""")
        veiksmas = (input('Jusu veiksmas: '))
        while veiksmas not in ['1','2','3','4','5']:
            print('Klaida! Iveskite sveikaji skaiciu (1-5) atitinkamam veiksmui atlikti.')
            veiksmas = input('Jusu veiksmas: ')

        if veiksmas == '1':       # Prideti filma
            print('Prideti filma.\n')
            while True:
                pavadinimas = input('Iveskite pavadinima: ')
                if pavadinimas == '':
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
            rezisierius = input('Iveskite rezisieriu: ')
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
            
#=================================================================================================================================
        elif veiksmas == '2':     # Filmu saraso atvaizdavimas
            zodynas_is_failo = Organizatorius.perziureti_filmus()
            for filmas in zodynas_is_failo:
                print(filmas)
            saraso_submenu = (input('Tolimesnis veiksmas:\n1. Pasalinti filma pagal pavadinima \n2. Atnaujinti filmu duomenis\n3. Filtruoti\n4. Sukurti seansa\n5. Grizti\nJusu pasirinkimas: '))
            while saraso_submenu not in ['1','2','3','4']:
                print('Klaida! Iveskite sveikaji skaiciu (1-4) atitinkamam veiksmui atlikti.')
                saraso_submenu = input('Jusu veiksmas: ')
                #================================================================================
            if saraso_submenu == '1':
                while True:
                    trinamo_filmo_pavadinimas = input('Iveskite norimo istrinti filmo pavadinima arba spauskite ENTED, kad griztumete i meniu: ')
                    if Organizatorius.istrinti_filma(trinamo_filmo_pavadinimas) == True:
                        print(f"Filmas '{trinamo_filmo_pavadinimas}' sekmingai istrintas.")
                        break
                    elif Organizatorius.istrinti_filma(trinamo_filmo_pavadinimas) == False:
                        print("Toks filmo pavadinimas neegzistuoja. Bandykite dar karta arba spauskite ENTER, kad griztumete i meniu.")
                        if trinamo_filmo_pavadinimas == '':
                            break
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
                #================================================================================
            elif saraso_submenu == '3':     #Filtravimas
                zanrofiltras = input('Filtravimas pagal zanra. Iveskite pageidaujama zanra: ')
                for filmas in Organizatorius.filmu_biblioteka:
                    if zanrofiltras.lower() in filmas.zanras.lower():
                        print(filmas)
                #================================================================================
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
                    Organizatorius.prideti_seansa(filmas1,savaites_diena,valanda,minute)

                #================================================================================
            elif saraso_submenu == '4': # Grizti
                break
#=================================================================================================================================
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
#=================================================================================================================================
        elif veiksmas == '5': # Parodyti seansus
            print('Seansu sarasas:')
            for filmas in Organizatorius.seansai:
                print (filmas)
#=================================================================================================================================
        elif veiksmas == '4': # Exit
            print('Viso gero.')
            programa_ijungta = False
            break
        else:
            print('Neteisinga ivestis. Rinkites veiksma 1-4.')