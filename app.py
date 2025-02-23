print('')
import pickle
import datetime

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
    def istrinti_filma(filmas):
            try:
                Organizatorius.filmu_biblioteka.pop(filmas)
                with open("filmu_biblioteka_pickle.pickle","wb") as failas: #pickle.dump(turinys,failas) //PRIDETA dump
                    pickle.dump(Organizatorius.filmu_biblioteka, failas)
                return True
            except:
                raise Exception ('Ivedete netinkama filma.')
                    

class Ziurovas:
    def __init__(self,vartotojo_vardas):
          self.vartotojo_vardas = vartotojo_vardas
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

Organizatorius.videotekos_inicializacija()
prisijungimo_input = str(input("Prisijunkite kaip 'organizatorius' arba 'ziurovas': "))
while True:
    if prisijungimo_input == 'organizatorius':
        print("""
                Prisijungta organizatoriaus teisemis. Pasirinkite veiksma:
                1 - Prideti nauja filma
                2 - Perziureti filmu sarasa
                3 - Ieskoti filmo
                4 - Istrinti filma
                5 - Iseiti is programos """)
        veiksmas = int(input('Jusu veiksmas: '))
        if veiksmas == 1:       # Prideti filma
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
                    raise Exception('Didziausias amziaus reitingas yra 18 (pilnametyste)')
            except ValueError:
                print("Klaida ivestuose metuose! Iveskite sveika skaiciu.")
            pridedamas_filmas = Filmas(pavadinimas,trukme,zanras,rezisierius,isleidimo_m,amziaus_reitingas)
            Organizatorius.prideti_filma(pridedamas_filmas)
            
#=================================================================================================================================
        elif veiksmas == 2:     # Filmu saraso atvaizdavimas

            # iteracija = 0
            zodynas_is_failo = Organizatorius.perziureti_filmus()
            for filmas in zodynas_is_failo:
                print(filmas)
            # while iteracija < len(zodynas_is_failo):
            #     print(f'{zodynas_is_failo[iteracija]}')
            #     iteracija = iteracija + 1

        elif veiksmas == 3:     # Knygu ieskojimas
            Organizatorius.ieskoti_filmo(input('Iveskite paieskos termina(autoriu arba pavadinima): '))

        elif veiksmas == 4:     # Knygu istrynimas
            i = 0
            print('Kuri filma noretumete istrinti? \n')
            while i < len(Organizatorius.filmu_biblioteka): # ciklas skirtas atvaizdavimui esamo saraso
                print(i,Organizatorius.filmu_biblioteka[i], '\n') #printinam saraso elementa ir keliam eilute
                i = i + 1
                if i == len(Organizatorius.filmu_biblioteka): # cia sustoja ciklas pasiekes bibliotekos pabaiga ir tada klausia kelinta numeri triname
                    Organizatorius.istrinti_filma(int(input()))
        else:
            print('Viso gero')
            break

