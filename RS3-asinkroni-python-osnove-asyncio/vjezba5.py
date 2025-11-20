# Definirajte korutinu secure_data koja će simulirati enkripciju osjetljivih podataka. Kako se u
# praksi enkripcija radi na poslužiteljskoj strani, korutina će simulirati enkripciju podataka u trajanju od
# 3 sekunde. Korutina prima kao argument rječnik osjetljivih podataka koji se sastoji od ključeva
# prezime , broj_kartice i CVV . Definirajte listu s 3 rječnika osjetljivih podataka. Pohranite u listu
# zadaci kao u prethodnom zadatku te pozovite zadatke koristeći asyncio.gather() . Korutina
# secure_data mora za svaki rječnik vratiti novi rječnik u obliku: {'prezime': 'prezime',
# 'broj_kartice': 'enkriptirano', 'CVV': 'enkriptirano'} . Za fake enkripciju koristite funkciju
# hash(str) koja samo vraća hash vrijednost ulaznog stringa ili nešto slično.
import asyncio

lista_podataka = [
  {'prezime': 'Antić', 'broj_kartice': '1234 2345 3456 4567', 'CVV': '123'},
  {'prezime': 'Buntić', 'broj_kartice': '2345 3456 4567 5678', 'CVV': '234'},
  {'prezime': 'Cindrić', 'broj_kartice': '3456 4567 5678 6789', 'CVV': '345'}
]

def enkriptiraj_podatke(zapis):
  return {k: hash(v) if k != 'prezime' else v for k, v in zapis.items()}

async def secure_data(zapis):
  await asyncio.sleep(3)
  return enkriptiraj_podatke(zapis)

async def main():
  zadaci = [asyncio.create_task(secure_data(podatak)) for podatak in lista_podataka]
  rezultat = await asyncio.gather(*zadaci)
  print(rezultat)

asyncio.run(main())
