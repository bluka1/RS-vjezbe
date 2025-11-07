def brojanje_rijeci(tekst):
  frekvencija_rijeci = {}
  rijeci = tekst.split()
  for rijec in rijeci:
    if not rijec in frekvencija_rijeci.keys():
      frekvencija_rijeci[rijec] = 1
    else:
      frekvencija_rijeci[rijec] += 1
  return frekvencija_rijeci

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
print(brojanje_rijeci(tekst))
