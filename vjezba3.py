import random

broj_pokusaja = 0
broj = random.randint(1, 100)
broj_je_pogoden = False

while not broj_je_pogoden:
  uneseni_broj = int(input("Unesite broj: "))
  broj_pokusaja += 1
  if uneseni_broj > broj:
    print("Traženi broj je manji!")
  elif uneseni_broj < broj:
    print("Traženi broj je veći!")
  else:
    broj_je_pogoden = True
    print(f"Bravo, pogodio si u {broj_pokusaja} pokušaja")