def prvi_i_zadnji(lista): return lista[0], lista[-1]
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(prvi_i_zadnji(lista))

def max_i_min(lista): return sorted(lista)[0], sorted(lista)[-1]
lista2 = [5, 10, 20, 50, 100, 11, 250, 50, 80]
print(max_i_min(lista2))

def presjek(lista1, lista2): return lista1.intersection(lista2)
skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}
print(presjek(skup_1, skup_2))
