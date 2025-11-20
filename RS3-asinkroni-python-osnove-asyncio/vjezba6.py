# Kako možete unutar main korutine natjerati event loop da obuhvati ispis unutar korutine
# fetch_data(2) bez da ju awaitate unutar main funkcije? Preciznije, dokažite kako se može ispisati
# tekst Dovršio sam s 2. unutar korutine fetch_data(2) bez da eksplicitno pozivate await task2
# unutar main() funkcije.

# ODGOVOR:

# 1. NAČIN:
# Možemo koristiti asyncio.gather i proslijediti mu sve taskove koje treba riješiti.
# Na taj način prepuštamo event loopu da izvršava taskove i vrati ih kad zadnji od njih bude gotov.
# Medutim, opet moramo koristiti await i malo izmjeniti kod.

# 2. NAČIN:
# Možemo jednostavno dodati asyncio.sleep(<proizvoljan broj veći od 1>) kao na 34.liniji koda i ispisat će se tekst unutar task2
# Zašto je to tako?
# Zato jer su oba taska definirana i spremljena u varijable task1 i task2. Time event loop postaje svjestan da oni postoje.
# U result1 varijabli prvi smo puta naveli await što je signal event loopu da preuzme sve dodijeljene taskove i krene ih izvršavati redom kojim su dodani.
# Event loop kreće izvršavanje prvog pa drugog taska (konkurentno ih izvršava)
# S obzirom da mi awaitamo samo task1, task2 se prekida i ne dovršava jer ga nismo awaitali, odnosno, nismo zatražili njegov rezultat

import asyncio, time

async def fetch_data(param):
  print(f"Nešto radim s {param}...")
  await asyncio.sleep(param)
  print(f'Dovršio sam s {param}.')
  return f"Rezultat za {param}"

async def main():
  task1 = asyncio.create_task(fetch_data(1)) # schedule
  task2 = asyncio.create_task(fetch_data(2)) #schedule
  result1 = await task1
  print("Fetch 1 uspješno završen.")
  # await asyncio.sleep(3)
  return [result1]

t1 = time.perf_counter()
results = asyncio.run(main()) # pokretanje event loop-a
t2 = time.perf_counter()
print(results)
print(f"Vrijeme izvođenja {t2 - t1:.2f} sekunde")
