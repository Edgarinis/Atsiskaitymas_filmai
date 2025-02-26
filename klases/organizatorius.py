import pickle
from klases.seansai import Seansas
class Organizatorius:
    filmu_biblioteka = []
    seansai = []

    def __init__(self,organizatoriaus_vardas):
         self.organizatoriaus_vardas = organizatoriaus_vardas

    def videotekos_inicializacija():
        try:
            with open("filmu_biblioteka_pickle.pickle","rb") as failas:
                Organizatorius.filmu_biblioteka = pickle.load(failas)
        except FileNotFoundError:
            with open("filmu_biblioteka_pickle.pickle","wb") as failas:
                pickle.dump(Organizatorius.filmu_biblioteka,failas)

    def seansu_inicializacija():
        try:
            with open("seansu_biblioteka_pickle.pickle","rb") as seansu_failas:
                Organizatorius.seansai = pickle.load(seansu_failas)
        except FileNotFoundError:
            with open("seansu_biblioteka_pickle.pickle","wb") as seansu_failas:
                pickle.dump(Organizatorius.seansai,seansu_failas)

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

    def prideti_seansa(filmas,diena,valanda,minutes,vietu_skaicius):
        seansas = Seansas(filmas,diena,valanda,minutes,vietu_skaicius)
        Organizatorius.seansai.append(seansas)
        with open("seansu_biblioteka_pickle.pickle","wb") as seansu_failas:
            pickle.dump(Organizatorius.seansai,seansu_failas) #pickle.dump(turinys,failas) //PRIDETA dump
        return True