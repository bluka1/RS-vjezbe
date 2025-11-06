zbroj = 0

while True:
  broj = int(input("Unesite broj: "))
  zbroj += broj
  if broj == 0:
    break

print(f"Zbroj svih unesenih brojeva je {zbroj}")