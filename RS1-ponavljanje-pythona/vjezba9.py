def ukloni_duplikate(lista):
  skup = set(lista)
  return list(skup)

lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(ukloni_duplikate(lista))
