class Seansas:
    def __init__(self,filmas,diena,valanda,minute,vietu_skaicius):
        self.filmas = filmas
        self.diena = diena
        self.valanda = valanda
        self.minute = minute
        self.vietu_skaicius = vietu_skaicius
    def __str__(self):
        return f"{self.filmas} | {self.diena}, {self.valanda}:{self.minute} | Vietu skaicius: {self.vietu_skaicius}"
    def laikas(self):
        return f"{self.diena}, {self.valanda}:{self.minute}"
    def laisvos_vietos(self):
        return int(self.vietu_skaicius)
    