# Definirajte dvije korutine koje će simulirati dohvaćanje podataka s weba. Prva korutina neka
# vrati listu proizvoljnih rječnika (npr. koji reprezentiraju podatke o korisnicima) nakon 3 sekunde, a
# druga korutina neka vrati listu proizvoljnih rječnika (npr. koji reprezentiraju podatke o proizvodima)
# nakon 5 sekundi. Korutine pozovite konkurentno korištenjem asyncio.gather() i ispišite rezultate.
# Program se mora izvršavati ~5 sekundi.

import asyncio
import time
async def get_korisnici():
  korisnici = [
    {
      "ime": "Luka",
      "prezime": "Lukić"
    },
    {
      "ime": "Ante",
      "prezime": "Antić"
    },
    {
      "ime": "Ivan",
      "prezime": "Ivić"
    }
  ]
  await asyncio.sleep(3)
  return korisnici

async def get_proizvodi():
  proizvodi = [
    {
      "naziv": "Mobitel",
      "cijena": "1000",
      "boja": "bijela"
    },
    {
      "naziv": "Tablet",
      "cijena": "777",
      "boja": "zlatna"
    },
    {
      "naziv": "Pametni sat",
      "cijena": "300",
      "boja": "siva"
    }
  ]
  await asyncio.sleep(5)
  return proizvodi

async def main():
  t1 = time.perf_counter()
  korisnici, proizvodi = await asyncio.gather(get_korisnici(), get_proizvodi())
  t2 = time.perf_counter()
  print(f"VRIJEME: {t2 - t1:.2f}")
  print('KORISNICI:', korisnici)
  print('PROIZVODI:', proizvodi)

asyncio.run(main())
