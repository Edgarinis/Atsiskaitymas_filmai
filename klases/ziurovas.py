from klases.organizatorius import Organizatorius
import pickle
class Ziurovas:
    def __init__(self,amzius):
          self.amzius = amzius

    def perziureti_filmus(self):
        with open("filmu_biblioteka_pickle.pickle","rb") as failas:
            filmai_is_failo = pickle.load(failas) #pickle.dump(turinys,failas) //PRIDETA dump
            return filmai_is_failo

    def rezervuoti_bilietus(seanso_id):
        seansas = Organizatorius.seansai[seanso_id]
        if seansas.laisvos_vietos() > 0:
            seansas.vietu_skaicius = int(seansas.vietu_skaicius)
            seansas.vietu_skaicius -= 1
            print(f'Rezervacija atlikta. Liko vietu:{seansas.laisvos_vietos()}.')
            with open("seansu_biblioteka_pickle.pickle","wb") as seansu_failas:
                pickle.dump(Organizatorius.seansai,seansu_failas) #pickle.dump(turinys,failas) //PRIDETA dump
        else:
            print('Deja laisvu vietu nebera.')
    
    def ivertinti(self,pavadinimas,ivertis):
        for filmas in Organizatorius.filmu_biblioteka:
            if pavadinimas.lower() == filmas.pavadinimas.lower():
                filmas.prideti_ivertinima(ivertis)
                with open("filmu_biblioteka_pickle.pickle", "wb") as failas:
                    pickle.dump(Organizatorius.filmu_biblioteka, failas)
                return f'Filmas {pavadinimas} ivertintas'
        return 'Filmas nerastas'