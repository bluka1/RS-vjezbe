def grupiraj_po_paritetu(lista):
  brojevi = {
    "parni": [],
    "neparni": []
  }

  for broj in lista:
    if broj % 2 == 0:
      brojevi["parni"].append(broj)
    else:
      brojevi["neparni"].append(broj)
  return brojevi

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(grupiraj_po_paritetu(lista))
