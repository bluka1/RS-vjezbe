import proizvodi
import functools

class Narudzba():
  def __init__(self, _naruceni_proizvodi, _ukupna_cijena):
    self.naruceni_proizvodi = _naruceni_proizvodi
    self.ukupna_cijena = _ukupna_cijena

  def ispis_narudzbe(self):
    proizvodi_str = ", ".join([f"{p['naziv']} x {p['narucena_kolicina']}" for p in self.naruceni_proizvodi])
    print(f"Naručeni proizvodi: {proizvodi_str}, Ukupna cijena: {self.ukupna_cijena} eur")


def napravi_narudzbu(products):
  dostupan = True
  # provjera jesu li proizvodi lista
  if not isinstance(products, list):
    return
  
  # provjera prazne liste
  if len(products) == 0:
    return
  
  for p in products:
    # provjera rjecnika
    if not isinstance(p, dict):
      return
    # provjera polja
    if "naziv" not in p or "cijena" not in p or "narucena_kolicina" not in p:
      return

  ukupna_cijena = functools.reduce(lambda x,y: x["narucena_kolicina"] * x["cijena"] + y["narucena_kolicina"] * y["cijena"],products)

  for p in products:
    pro = list(filter(lambda x: x["naziv"] == p["naziv"], proizvodi.skladiste))

    if (pro["narucena_kolicina"] < p["dostupna_kolicina"]):
      print(f"Proizvod {p["naziv"]} nije dostupan!")
      dostupan == False
      return

  if (dostupan == False): return

  return Narudzba(products, ukupna_cijena)


narudzbe = []
