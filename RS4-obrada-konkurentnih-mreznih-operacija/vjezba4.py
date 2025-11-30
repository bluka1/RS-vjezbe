# Zadatak 4: simulacija autentifikacije korisnika
# Napišite korutinu autentifikacija koja simulira proces autentifikacije korisnika. Korutina treba primiti korisničko ime i lozinku, 
# zatim simulirati sporo I/O čekanje (npr. 2 sekunde) prije nego što vrati True ako su korisničko ime i lozinka ispravni. 
# Korisničko ime i lozinku provjerite prema rječniku korisnici koji sadrži parove korisničko ime-lozinka.

# Simulirajte pogrešku u autentifikaciji ako su uneseni podaci netočni (raise ValueError).

# Napišite glavnu funkciju koja će poslati konkurentne zahtjeve za autentifikaciju za 5 različitih korisnika 
# (neki s ispravnim, neki s neispravnim podacima). Kako se ponaša asyncio.gather() kada se dogodi iznimka u jednoj od korutina?
# Izmijenite kod korutine i simulirajte grešku u autentifikaciji koja se javlja odmah nakon 3 sekunde čekanja 
# (npr. ne radi autentifikacijski servis) koji će podići iznimku TimeoutError.

# Dodajte timeout prilikom poziva korutine autentifikacija kako biste simulirali situaciju kada autentifikacijski servis ne odgovara na vrijeme.



##### PRVO RJEŠENJE (po meni ispravnije)

# import asyncio

# korisnici = {
#   "korisnik1": "lozinka1",
#   "korisnik2": "lozinka2",
#   "korisnik3": "lozinka3",
# }

# async def autentifikacija(kor_ime, lozinka, to):
#   try:
#     await asyncio.wait_for(asyncio.sleep(to), timeout=2)
#     postoji = korisnici.get(kor_ime)
#     if (postoji == None or korisnici.get(kor_ime) != lozinka):
#       raise ValueError('NEISPRAVNI PODACI')
#     print('USPJEŠNA AUTENTIFIKACIJA')      
#     return True
#   except asyncio.TimeoutError:
#     print('TIMEOUT ERROR')
#     return False
#   except ValueError as e:
#     print(e)
#     return False

# async def main():
#   tasks = [
#     asyncio.create_task(autentifikacija('luka', 'lukic', 1)), 
#     asyncio.create_task(autentifikacija('korisnik1', 'lozinka1', 1.5)), 
#     asyncio.create_task(autentifikacija('korisnik2', 'lozinka2', 1)), 
#     asyncio.create_task(autentifikacija('korisnik3', 'lozinka3', 3)), 
#     asyncio.create_task(autentifikacija('ingrid', 'ingri', 2))
#   ]
#   await asyncio.gather(*tasks)

# asyncio.run(main())



#### DRUGO RJEŠENJE

# Kako se ponaša asyncio.gather() kada se dogodi iznimka u jednoj od korutina?

# asyncio.gather() kod errora u izvršavanju taska baca iznimku i prestaje čekati ostale.
# Dakle, taskovi se i dalje izvode, ali njihovi rezultati se ignoriraju.
# Zato możemo koristiti return_exceptions=True argument kod poziva taskova kako bi se iznimke vratile kao rezultati.

import asyncio

korisnici = {
  "korisnik1": "lozinka1",
  "korisnik2": "lozinka2",
  "korisnik3": "lozinka3",
}

async def autentifikacija(kor_ime, lozinka, to):
  await asyncio.wait_for(asyncio.sleep(to), timeout=2)
  postoji = korisnici.get(kor_ime)
  if (postoji == None or korisnici.get(kor_ime) != lozinka):
    raise ValueError('NEISPRAVNI PODACI')
  print('USPJEŠNA AUTENTIFIKACIJA')
  return True

async def main():
  tasks = [
    asyncio.create_task(autentifikacija('luka', 'lukic', 3)), 
    asyncio.create_task(autentifikacija('korisnik1', 'lozinka1', 1.5)), 
    asyncio.create_task(autentifikacija('korisnik2', 'lozink', 1)), 
    asyncio.create_task(autentifikacija('korisnik3', 'lozinka3', 3)), 
    asyncio.create_task(autentifikacija('ingrid', 'ingri', 2))
  ]
  try:
    # da bismo vratili i iznimke kao rezultate, dodajemo return_exceptions=True argument kod poziva taskova
    results = await asyncio.gather(*tasks, return_exceptions=True)
    # printamo rezultate da vidimo spremaju li se i iznimke
    print(results)
  except asyncio.TimeoutError:
    print('TIMEOUT ERROR')
    return False
  except ValueError as e:
    print(e)
    return False

asyncio.run(main())
