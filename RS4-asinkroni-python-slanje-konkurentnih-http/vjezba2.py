# Definirajte dvije korutine, od kojih će jedna služiti za dohvaćanje činjenica o mačkama koristeći
# get_cat_fact korutinu koja šalje GET zahtjev na URL: https://catfact.ninja/fact . Izradite 20
# Task objekata za dohvaćanje činjenica o mačkama te ih pozovite unutar main korutine i rezultate
# pohranite odjednom koristeći asyncio.gather funkciju. Druga korutina filter_cat_facts ne šalje
# HTTP zahtjeve, već mora primiti gotovu listu činjenica o mačkama i vratiti novu listu koja sadrži samo
# one činjenice koje sadrže riječ "cat" ili "cats" (neovisno o velikim/malim slovima).

import asyncio
import aiohttp

CAT_API_URL = 'https://catfact.ninja/fact'

async def get_cat_fact(session):
  res = await session.get(CAT_API_URL)
  dict = await res.json()
  return dict['fact']

def filter_cat_facts(facts):
  return filter(lambda c: 'cat' in c or 'cats' in c.lower(), facts)

async def main():
  async with aiohttp.ClientSession() as session:
    zadaci = [get_cat_fact(session) for i in range(1,21)]
    rezultati = await asyncio.gather(*zadaci)
    gotova_lista = list(filter_cat_facts(rezultati))
    i = 0
    for f in gotova_lista:
      i += 1
      print(i, ':', f, '\n')
    # ILI
    # for i in range(0, len(gotova_lista)):
    #   print(i+1, ':', gotova_lista[i], '\n')

asyncio.run(main())
