a = float(input("Unesite prvi broj: "))
b = float(input("Unesite drugi broj: "))
operator = input("Unesite operator: ")

def kalkulator(a,b,operator):
  if operator == "+":
    rezultat = a + b
  elif operator == "-":
    rezultat = a - b
  elif operator == "*":
    rezultat = a * b
  elif operator == "/":
    if b == 0:
      rezultat = "Nemoguće dijeljenje s 0!"
    else:
      rezultat = a / b
  else:
    rezultat = "Nepodržani operator!"
  return rezultat

rezultat = kalkulator(a,b,operator)
if type(rezultat) == float:
  print("Rezultat operacije", a, operator, b, "je", rezultat)
else:
  print(rezultat)