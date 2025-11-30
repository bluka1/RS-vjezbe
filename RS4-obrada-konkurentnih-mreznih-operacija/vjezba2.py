# Zadatak 2: filter_cat_facts
# Definirajte dvije korutine, od kojih će jedna služiti za dohvaćanje činjenica o mačkama koristeći get_cat_fact korutinu koja šalje GET zahtjev na 
# URL: https://catfact.ninja/fact. Izradite 20 Task objekata za dohvaćanje činjenica o mačkama te ih pozovite unutar main korutine i rezultate 
# pohranite odjednom koristeći asyncio.gather funkciju. Druga korutina filter_cat_facts ne šalje HTTP zahtjeve, već zaprima gotovu listu činjenica 
# (stringova) o mačkama i vraća novu listu koja sadrži samo one činjenice koje sadrže riječ "cat" ili "cats" (neovisno o velikim/malim slovima).

import asyncio
import aiohttp

API_URL = 'https://catfact.ninja/fact'

async def get_cat_fact(session):
  res = await session.get(API_URL)
  data = await res.json()
  return data['fact']

async def filter_cat_facts(facts):
  return list(filter(lambda f : 'cat' in f.lower() or 'cats' in f.lower(), facts))

async def main():
  async with aiohttp.ClientSession() as session:
    tasks = [asyncio.create_task(get_cat_fact(session)) for _ in range(20)]
    facts = await asyncio.gather(*tasks)
    filtered_facts = await filter_cat_facts(facts)
    print(filtered_facts)


asyncio.run(main())
