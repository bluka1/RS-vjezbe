# Zadatak 6: Jednostavna komunikacija
# Definirajte 2 mikroservisa u 2 različite datoteke. 
# Prvi mikroservis neka sluša na portu 8081 i na endpointu /pozdrav vraća JSON odgovor nakon 3 sekunde čekanja, 
# u formatu: {"message": "Pozdrav nakon 3 sekunde"}. Drugi mikroservis neka sluša na portu 8082 
# te na istom endpointu vraća JSON odgovor nakon 4 sekunde: {"message": "Pozdrav nakon 4 sekunde"}.

# Unutar client.py datoteke definirajte 1 korutinu koja može slati zahtjev na oba mikroservisa, 
# mora primati argumente url i port. Korutina neka vraća JSON odgovor.

# Korutinu pozovite unutar main korutine. Prvo demonstrirajte sekvencijalno slanje zahtjeva, 
# a zatim konkurentno slanje zahtjeva.

import asyncio
import aiohttp
import time

async def get_pozdrav(url, port):
  async with aiohttp.ClientSession() as session:
    res = await session.get(f'http://localhost:{port}/{url}')
    data = await res.json()
    return data

async def main():
  t1 = time.time()

  # SEKVENCIJALNO SLANJE
  # poz1 = await get_pozdrav('pozdrav', 8081)
  # poz2 = await get_pozdrav('pozdrav', 8082)
  # VRIJEME: 7.01

  # KONKURENTNO SLANJE
  tasks = [asyncio.create_task(get_pozdrav('pozdrav', 8081)), asyncio.create_task(get_pozdrav('pozdrav', 8082))]
  poz1, poz2 = await asyncio.gather(*tasks)
  # VRIJEME: 4.01

  print(poz1)
  print(poz2)
  t2 = time.time()
  print(f'VRIJEME: {t2-t1:.2f}')

asyncio.run(main())
