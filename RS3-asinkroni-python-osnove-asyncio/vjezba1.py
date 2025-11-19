# Definirajte korutinu koja će simulirati dohvaćanje podataka s weba. Podaci neka budu lista
# brojeva od 1 do 10 koju ćete vratiti nakon 3 sekunde. Listu brojeva definirajte comprehensionom.
# Nakon isteka vremena, u korutinu ispišite poruku "Podaci dohvaćeni." i vratite podatke. Riješite bez
# korištenja asyncio.gather() i asyncio.create_task() funkcija.

import asyncio
async def korutina():
  lista = [x for x in range(1,11)]
  await asyncio.sleep(3)
  print('Podaci dohvaćeni.')
  return lista

asyncio.run(korutina())
