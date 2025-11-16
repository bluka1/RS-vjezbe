class Proizvod():
  def __init__(self, _naziv , _cijena, _dostupna_kolicina):
    self.naziv = _naziv
    self.cijena = _cijena
    self.dostupna_kolicina = _dostupna_kolicina
  
  def ispis(self):
    print(vars(self))

skladiste = [Proizvod("mobitel", 1000, 100), Proizvod("tablet", 500, 50)]

def dodaj_proizvod(proizvod):
  skladiste.append(proizvod)
