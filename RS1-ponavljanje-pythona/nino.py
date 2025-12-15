import nino_br

def validiraj_broj_telefona(broj: str):
  # prvo čistimo broj
  ocisceni_broj = ocisti_broj(broj)
  if ocisceni_broj is None:
    return {
      "pozivni_broj": None,
      "broj_ostatak": broj,
      "vrsta": None,
      "mjesto": None,
      "operater": None,
      "validan": False
    }
  # zatim validiramo
  return validiraj_broj(ocisceni_broj)

def ocisti_broj(broj: str):
  znakovi_za_ciscenje = ['(', ')', '+', ' ', '-', '!', '?', ',', ':', ';', '~']
  # mičemo praznine na početku i kraju ako ih ima u stringu
  broj = broj.strip()
  # pretvaramo broj u niz znakova
  niz_brojeva = list(broj)
  # filtriramo znakove kroz list comprehension
  samo_brojevi = [x for x in niz_brojeva if x not in znakovi_za_ciscenje]
  # pretvaramo niz u string
  ocisceni_broj = ''.join(samo_brojevi)

  # umjesto dodavanja svih slova i svih mogućih znakova koji nisu brojke, ovdje jednostavno provjeravamo je li očišćeni broj zapravo broj
  if not ocisceni_broj.isdigit():
    return None
  
  ocisceni_broj = makni_medunarodne(ocisceni_broj)

  # ako smo unijeli lokalni broj, ne želimo dodati "leading zero"
  for obj in nino_br.brojevi:
    if ocisceni_broj.startswith(obj['pozivni_broj']):
      return ocisceni_broj
  brojevi = '0' + ocisceni_broj
  return brojevi

def validiraj_broj(broj: str):
  # deklariramo pomoćne varijable
  trazeni_dict = None
  pozivni_broj = None
  broj_ostatak = None
  vrsta = None
  mjesto_operater = None
  validan = True
  mjesto = None
  operater = None

  # da bismo došli do potrebnih informacija o broju, prolazimo kroz listu pozivnih brojeva i pripadajućih informacija
  for obj in nino_br.brojevi:
    if broj.startswith(obj['pozivni_broj']):
      trazeni_dict = obj
      pozivni_broj = obj['pozivni_broj']
      vrsta = obj['vrsta']
      mjesto_operater = obj['mjesto_operater']
      broj_ostatak = broj[len(pozivni_broj):]

  # ako pozivni broj nije naden u listi pozivnih, samo vraćamo uneseni broj i validnost postavljamo na None
  if trazeni_dict is None:
    return {
      "pozivni_broj": None,
      "broj_ostatak": broj,
      "vrsta": None,
      "mjesto": None,
      "operater": None,
      "validan": False
    }
  else:
    # provjeravamo validnost
    if vrsta == 'Posebne usluge' and len(broj_ostatak) != 6:
      validan = False
    if (vrsta == 'Fiksna mreža' or vrsta == 'Mobilna mreža') and (len(broj_ostatak) < 6 or len(broj_ostatak) > 7):
      validan = False

    # postavljamo vrijednosti pomoćnih varijabli
    if vrsta == 'Mobilna mreža':
      mjesto = None
      operater = mjesto_operater
    if vrsta == 'Posebne usluge':
      mjesto = None
      operater = None
    if vrsta == 'Fiksna mreža':
      operater = None
      mjesto = mjesto_operater
    # vraćamo završni objekt
    return {
      "pozivni_broj": pozivni_broj,
      "broj_ostatak": broj_ostatak,
      "vrsta": vrsta,
      "mjesto": mjesto,
      "operater": operater,
      "validan": validan
    }
  
def makni_medunarodne(broj: str):
  # mičemo medunarodni pozivni broj kako bismo došli do lokalnog broja
  if broj.startswith('00385'):
    return broj[5:]
  elif broj.startswith('385'):
    return broj[3:]
  elif broj.startswith('00'):
    return broj[2:]
  else:
    return broj

# print(validiraj_broj_telefona('012345678'))
# print(validiraj_broj_telefona('+(385)91123456777777777'))
# print(validiraj_broj_telefona('0038591123456777777777'))
# print(validiraj_broj_telefona('00385911234567'))
# print(validiraj_broj_telefona('385911234567'))
# print(validiraj_broj_telefona('0049857353287354'))
# print(validiraj_broj_telefona('(385)19876543'))
