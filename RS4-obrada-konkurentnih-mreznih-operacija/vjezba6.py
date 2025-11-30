# Zadatak 6: Simulacija raspodijeljenog sustava za dohvaćanje i obradu vremenskih podataka

# Radite na raspodijeljenom sustavu za dohvaćanje vremenskih podataka s različitih javnih API-ja**. 
# Vaš servis treba konkurentno agregirati podatke o vremenu iz više izvora te nakon toga izračunati i ispisati prosječnu temperaturu. 
# Definirajte korutinu fetch_weather_data (predstavlja mikroservis koji vraća podatke s meteorološke stanice na određenoj lokaciji), koja
# simulira određeno čekanje (možete staviti nasumično čekanje između 1 i 5 sekundi koristeći random.uniform(1, 5)) i vraća nasumičnu 
# temperaturu između 20 i 25 stupnjeva Celzijusa. U glavnoj korutini main kreirajte i rasporedite 10 objekata tipa Task za konkurentno 
# dohvaćanje vremenskih podataka s 10 različitih vremenskih stanica. Nakon što dobijete sve rezultate, izračunajte i ispišite prosječnu temperaturu.

# - Simulirajte situaciju u kojoj nekoliko vremenskih stanica ne odgovara na vrijeme te pravilno obradite iznimku TimeoutError.

# - Ograničite vrijeme čekanja na svaki zahtjev na najviše 2 sekunde; u suprotnom slučaju vratite None te 
# izračunajte prosječnu temperaturu bez podataka za tu mjernu stanicu.

# Ako hoćete, možete određene dijelove koda rasporediti u zasebne datoteke (module) ili možete sve napisati u jednoj datoteci.

import asyncio
import random

async def fetch_weather_data():
  sleep_time = random.uniform(1, 5)
  try:
    await asyncio.wait_for(asyncio.sleep(sleep_time), timeout=2)
    rand = random.uniform(20, 25)
    print('RANDOM TEMPERATURA: ', rand)
    return rand
  except asyncio.TimeoutError as e:
    print('TIMEOUT ERROR')
    return None
  

async def main():
  tasks = [asyncio.create_task(fetch_weather_data()) for _ in range(10)]
  results = await asyncio.gather(*tasks)
  
  # avg = sum(results) / len(results)
  valid_res = [x for x in results if x is not None]
  suma = sum(valid_res)
  brEl = len(valid_res)
  if (brEl > 0):
    avg = suma / brEl
  else:
    avg = 0
  print(f'PROSJEČNA TEMPERATURA IZNOSILA JE: {avg:.2f} CELZIJUSA.')

asyncio.run(main())
