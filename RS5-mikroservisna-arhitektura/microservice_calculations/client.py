# Zadatak 7: Računske operacije
# Definirajte 3 mikroservisa unutar direktorija microservice_calculations. 
# Prvi mikroservis neka sluša na portu 8083 i na endpointu /zbroj vraća JSON bez čekanja. 
# Ulazni podatak u tijelu zahtjeva neka bude lista brojeva, a odgovor neka bude zbroj svih brojeva. 
# Dodajte provjeru ako brojevi nisu proslijeđeni, vratite odgovarajući HTTP odgovor i statusni kôd.

# Drugi mikroservis neka sluša na portu 8084 te kao ulazni podataka prima iste podatke. 
# Na endpointu /umnozak neka vraća JSON odgovor s umnoškom svih brojeva. 
# Dodajte provjeru ako brojevi nisu proslijeđeni, vratite odgovarajući HTTP odgovor i statusni kôd.

# Treći mikroservis pozovite nakon konkurentnog izvršavanja prvog i drugog mikroservisa. 
# Dakle treći ide sekvencijalno jer mora čekati rezultati prethodna 2. 
# Ovaj mikroservis neka sluša na portu 8085 te na endpointu /kolicnik očekuje JSON s podacima prva dva servisa. 
# Kao odgovor mora vratiti količnik umnoška i zbroja. Dodajte provjeru i vratite odgovarajući statusni kôd ako se pokuša umnožak dijeliti s 0.

# U client.py pozovite konkurentno s proizvoljnim podacima prva dva mikroservisa, a zatim sekvencijalno pozovite treći mikroservis.

import asyncio
import aiohttp

async def get_ms_response(port, ruta, lista = None, umnozak = None, zbroj = None):
  async with aiohttp.ClientSession() as session:
    if lista != None:
      res = await session.post(f'http://localhost:{port}/{ruta}', json=lista)
    else:
      res = await session.post(f'http://localhost:{port}/{ruta}', json={'zbroj': zbroj, 'umnozak': umnozak})
    return await res.json()
  
async def main():
  lista_brojki = [1,2,3,4,5,6,7,8,9,10]
  tasks = [asyncio.create_task(get_ms_response(8083, 'zbroj', lista_brojki)), asyncio.create_task(get_ms_response(8084, 'umnozak', lista_brojki))]
  zbroj, umnozak = await asyncio.gather(*tasks)
  kolicnik = await get_ms_response(8085, 'kolicnik', None, umnozak['umnozak'], zbroj['zbroj'])
  print('kolicnik: ', kolicnik)

asyncio.run(main())
