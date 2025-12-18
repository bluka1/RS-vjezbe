# Zadatak 8: Mikroservisna obrada - CatFacts API
# Definirajte 2 mikroservisa unutar direktorija cats.

# Prvi mikroservis cat_microservice.py mora slušati na portu 8086 i na endpointu /cats 
# vraćati JSON odgovor s listom činjenica o mačkama. 
# Endpoint /cat mora primati URL parametar amount koji predstavlja broj činjenica koji će se dohvatiti. 
# Na primjer, slanjem zahtjeva na /cat/30 dohvatit će se 30 činjenica o mačkama. 
# Činjenice se moraju dohvaćati konkurentnim slanjem zahtjeva na CatFacts API. 
# Link: https://catfact.ninja/

# Drugi mikroservis cat_fact_check mora slušati na portu 8087 i 
# na endopintu /facts očekivati JSON objekt s listom činjenica o mačkama u tijelu HTTP zahtjeva. 
# Glavna dužnost ovog mikroservisa je da provjeri svaku činjenicu sadrži li riječ cat ili cats, 
# neovisno o velikim i malim slovima. 
# Odgovor neka bude JSON objekt s novom listom činjenica koje zadovoljavaju prethodni uvjet.

# U client.py pozovite ove dvije korutine sekvencijalno, obzirom da drugi mikroservis ovisi o rezultatima prvog. 
# Testirajte kôd za proizvoljan broj činjenica.
import aiohttp
import asyncio

async def get_facts(ruta, broj=None):
  async with aiohttp.ClientSession() as session:
    if broj is None:
      res = await session.get(f'http://localhost:8086/{ruta}')
    else:
      res = await session.get(f'http://localhost:8086/{ruta}/{broj}')
    data = await res.json()
    return data

async def check_facts(lista):
  async with aiohttp.ClientSession() as session:
    res = await session.post(f'http://localhost:8087/facts', json=lista)
    data = await res.json()
    return data

async def main():
  facts_10 = await get_facts('cat', 10)
  checked_10_facts = await check_facts(facts_10)
  print(checked_10_facts)

asyncio.run(main())
