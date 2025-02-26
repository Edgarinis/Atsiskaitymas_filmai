class Filmas:
    def __init__(self,pavadinimas,trukme,zanras,rezisierius,isleidimo_m,amziaus_reitingas = 8):
          self.pavadinimas = pavadinimas
          self.trukme = trukme
          self.zanras = zanras
          self.rezisierius = rezisierius
          self.isleidimo_m = isleidimo_m
          self.amziaus_reitingas = amziaus_reitingas
          self.ivertinimai = []

    def prideti_ivertinima(self,ivertinimas):
        if 1 < ivertinimas <= 10:
            self.ivertinimai.append(ivertinimas)
            return True
        else:
            return False
    
    def ivertinimu_vidurkis(self):
        if not self.ivertinimai:
            return 'Nera'
        return round(sum(self.ivertinimai) / len(self.ivertinimai), 2) #saraso vidurkio formule, apvalinam iki ,00

    def __str__(self):
        vidurkis = self.ivertinimu_vidurkis()
        return (f"Filmas: {self.pavadinimas} | Trukme: {self.trukme} | Zanras: {self.zanras} "
                f"| Rezisierius: {self.rezisierius} | Metai: {self.isleidimo_m} | PEGI-{self.amziaus_reitingas} "
                f"| Vidutinis ivertinimas: {vidurkis}")
