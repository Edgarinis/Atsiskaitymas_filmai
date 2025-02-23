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
    def __init__(self,organizatoriaus_vardas):
         self.organizatoriaus_vardas = organizatoriaus_vardas
    def videotekos_inicializacija():
        with open("filmu_biblioteka_pickle.pickle","rb") as failas:
            Organizatorius.filmu_biblioteka = pickle.load(failas)
    def perziureti_filmus():
        # with open("filmu_biblioteka_pickle.pickle","wb") as failas: #pickle.dump(turinys,failas) //PRIDETA dump
        #     pickle.dump(filmu_biblioteka, failas)
        with open("filmu_biblioteka_pickle.pickle","rb") as failas:
            filmu_sarasas_is_failo = pickle.load(failas) #pickle.dump(turinys,failas) //PRIDETA dump
            return filmu_sarasas_is_failo
    def prideti_filma(filmas): # saugosim filmus kaip objektus
        try:
            Organizatorius.filmu_biblioteka.append(filmas)
            # with open("filmu_biblioteka_pickle.pickle","rb") as failas: #pickle.dump(turinys,failas) //PRIDETA dump
            #     pickle.load(failas) #pickle.dump(turinys,failas) //PRIDETA dump
            #     Organizatorius.filmu_biblioteka.append(filmas)
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


Organizatorius.videotekos_inicializacija()
# while True:
#     prisijungimo_input = str(input("Prisijunkite kaip 'organizatorius' arba 'ziurovas': "))
#     if prisijungimo_input in ['organizatorius', 'ziurovas']:
#         break
#     print("Klaida! Prisijunkite kaip 'organizatorius' arba 'ziurovas'. ")
prisijungimo_input = 'organizatorius'
while True:
    if prisijungimo_input == 'organizatorius':
        print("""Prisijungta organizatoriaus teisemis. Pasirinkite veiksma:
                1 - Prideti nauja filma
                2 - Perziureti filmu sarasa
                3 - Ieskoti filmo
                4 - Istrinti filma
                5 - Iseiti is programos """)
        veiksmas = (input('Jusu veiksmas: '))
        if veiksmas == '1':       # Prideti filma
            print('Prideti filma.\n')
            pavadinimas = input('Iveskite pavadinima: ')
            trukme = input('Iveskite trukme minutemis: ')
            zanras = input('Iveskite zanra: ')
            rezisierius = input('Iveskite rezisieriu: ')
            try:
                isleidimo_m = int(input('Iveskite isleidimo metus: '))
                if isleidimo_m < 1878:
                    raise ValueError("Metai neteisingi! Pirmasis filmas buvo isleistas 1878 pavadinimu 'The Horse in Motion'")
                if isleidimo_m > datetime.datetime.now().year:
                    raise ValueError(f'Metai neteisingi! Dabar juk {datetime.datetime.now().year}')
            except ValueError:
                print("Isleidimo metai ivesti neteisingai!")
            try:
                amziaus_reitingas = int(input('Iveskite amziaus reitinga: N - '))
                if amziaus_reitingas < 0:
                    raise Exception('Amzius negali buti neigiamas!')
                if amziaus_reitingas > 18:
                    raise Exception('Didziausias amziaus reitingas yra 18 (pilnametyste).')
            except ValueError:
                print("Klaida ivestuose metuose! Iveskite sveika skaiciu.")
            pridedamas_filmas = Filmas(pavadinimas,trukme,zanras,rezisierius,isleidimo_m,amziaus_reitingas)
            Organizatorius.prideti_filma(pridedamas_filmas)
            
#=================================================================================================================================
        elif veiksmas == '2':     # Filmu saraso atvaizdavimas
            zodynas_is_failo = Organizatorius.perziureti_filmus()
            for filmas in zodynas_is_failo:
                print(filmas)
            trinti_naujinti_grizti = input('Tolimesnis veiksmas:\n1. Pasalinti filma pagal pavadinima \n2. Atnaujinti filmu duomenis\n3. Grizti\nJusu pasirinkimas: ')
            if trinti_naujinti_grizti == '1':
                while True:
                    trinamo_filmo_pavadinimas = input('Iveskite norimo istrinti filmo pavadinima: ')
                    if Organizatorius.istrinti_filma(trinamo_filmo_pavadinimas) == True:
                        print(f"Filmas '{trinamo_filmo_pavadinimas}' sekmingai istrintas.")
                        break
                    elif Organizatorius.istrinti_filma(trinamo_filmo_pavadinimas) == False:
                        print("Toks filmo pavadinimas neegzistuoja. Bandykite dar karta arba spauskite ENTER, kad griztumete i meniu.")
                        if trinamo_filmo_pavadinimas == '':
                            break
            elif trinti_naujinti_grizti == '2':
                atnaujinamas_filmas = input('Iveskite norimo atnaujinti filmo pavadinima: ')
                rastas_filmas = Organizatorius.ieskoti_filmo(atnaujinamas_filmas)
                if not rastas_filmas:
                    print('Tokio filmo nera.')
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
        elif veiksmas == '4':     # Filmu istrynimas
            i = 0
            print('Kuri filma noretumete istrinti? \n')
            while i < len(Organizatorius.filmu_biblioteka): # ciklas skirtas atvaizdavimui esamo saraso
                print(i,Organizatorius.filmu_biblioteka[i], '\n') #printinam saraso elementa ir keliam eilute
                i = i + 1
                if i == len(Organizatorius.filmu_biblioteka): # cia sustoja ciklas pasiekes bibliotekos pabaiga ir tada klausia kelinta numeri triname
                    Organizatorius.istrinti_filma(int(input()))
#=================================================================================================================================
        elif veiksmas == '5':     # Exit
            print('Viso gero.')
            break
        else:
            print('Neteisinga ivestis. Rinkites veiksma 1-5.')


