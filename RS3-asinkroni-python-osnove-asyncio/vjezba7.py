# Objasnite korak po korak kako se ponaša event loop (kako se raspoređuju, izvršavaju i dovršavaju
# korutine te koja su njihova stanja u različitim fazama izvođenja) na sljedećem primjeru:

import asyncio

# async je ključna riječ kojom dajemo do znanja pythonu da želimo hendlati asinkronost tj. u našem slučaju da želimo
# omogućiti konkurentnost izvršavanja koda
# ova funkcija pokreće se gotovo istovremeno za sve taskove koje smo proslijedili event loopu
async def timer(name, delay):
  for i in range(delay, 0, -1): # simuliranje timera - unutar for petlje koristimo sleep metodu koja traje 1 sekundu i pokrećemo ju onoliko puta koliko sekundi je dodijeljeno parametru delay
    print(f'{name}: {i} sekundi preostalo...') # ispis koliko je vremena još ostalo
    await asyncio.sleep(1) # ovdje simuliramo asinkronost koja bi se desila u stvarnom slučaju kada bismo dohvaćali podatke i sl.
  print(f'{name}: Vrijeme je isteklo!') # označavanje kraja korutine

async def main():
  # ova lista ključna je za event loop jer mu dajemo do znanja kojim sve zadacima on treba upravljati
  # dakle, ovdje definiramo taskove koji će biti predani event loopu
  timers = [
    asyncio.create_task(timer('Timer 1', 3)),
    asyncio.create_task(timer('Timer 2', 5)),
    asyncio.create_task(timer('Timer 3', 7))
  ]
  await asyncio.gather(*timers) # pokretanje svih taskova tj. korutina zbog await-a -> tada se taskovi predaju event loopu da ih hendla i izvršava tj. pokreće
  # važno za naglasiti je da je ovo prvi await u našoj skripti i to je trenutak u kojem će svi do tada definirani taskovi biti predani event loopu

asyncio.run(main()) # stvaramo tj. pokrećemo event loop i omogućujemo konkurentno izvršavanje taskova


# kako se raspoređuju, izvršavaju i dovršavaju korutine te koja su njihova stanja u različitim fazama izvođenja?

# Event loop rasporeduje i izvršava korutine tj. taskove onim redoslijedom kojim su dodani u listu.
# Svi taskovi su proslijedeni event loopu kroz gather metodu i unpacking(*) operator.
# Oni će biti pokrenuti gotovo istovremeno radi principa konkurentnosti.
# Taskovi će se čak i izvršavati gotovo istovremeno.
# Medutim, razlikuje se dovršavanje taskova jer svaki od njih ima različitu delay vrijednost i samim time korutina ima različito trajanje
# Dakle, u ovom našem primjeru, ukupno trajanje će biti nešto mrvicu više od 7 sekundi jer sve korutine kreću "istovremeno" tako da je
# ukupno vrijeme dobiveno trajanjem najdulje korutine odnosno trajanjem 3. timera.
