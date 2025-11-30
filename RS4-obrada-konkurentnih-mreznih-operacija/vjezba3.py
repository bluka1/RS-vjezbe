# Zadatak 3: mix_dog_cat_facts
# Definirajte korutinu get_dog_fact koja dohvaća činjenice o psima sa DOG API servisa.

# Korutina get_dog_fact neka dohvaća činjenicu o psima na URL-u: https://dogapi.dog/api/v2/facts. Nakon toga, 
# definirajte korutinu get_cat_fact koja dohvaća činjenicu o mačkama slanjem zahtjeva na URL: https://catfact.ninja/fact.

# Istovremeno pohranite rezultate izvršavanja ovih Taskova koristeći asyncio.gather(*dog_facts_tasks, *cat_facts_tasks) 
# funkciju u listu dog_cat_facts, a zatim ih koristeći list slicing odvojite u dvije liste obzirom da znate da je prvih 
# 5 činjenica o psima, a drugih 5 o mačkama (bez obzira što mrežni rezultati različito "dolaze", gather ih pohranjuje redoslijedom poziva).

# Na kraju definirajte treću korutinu mix_facts koja prima dvije liste, dog_facts i cat_facts, 
# te vraća novu listu u kojoj se za svaki indeks i nalazi odabrana činjenica prema sljedećem pravilu: uzmite činjenicu o psima ako je njezina 
# duljina veća od duljine odgovarajuće mačje činjenice; u suprotnom odaberite mačju činjenicu. Za paralelnu iteraciju dviju lista upotrijebite 
# funkciju zip, npr. for dog_fact, cat_fact in zip(dog_facts, cat_facts). Nakon dobivanja nove liste, ispišite filtrirani skup činjenica.

import asyncio
import aiohttp

CAT_API_URL = 'https://catfact.ninja/fact'
DOG_API_URL = 'https://dogapi.dog/api/v2/facts'

async def get_cat_fact(session):
  res = await session.get(CAT_API_URL)
  data = await res.json()
  return data['fact']

async def get_dog_fact(session):
  res = await session.get(DOG_API_URL)
  data = await res.json()
  fact = data['data'][0]['attributes']['body']
  return fact

async def mix_facts(dog_facts, cat_facts):
  return [dogf if len(dogf) >= len(catf) else catf for dogf, catf in zip(dog_facts, cat_facts)]

async def main():
  async with aiohttp.ClientSession() as session:
    dog_tasks = [asyncio.create_task(get_dog_fact(session)) for _ in range(5)]
    cat_tasks = [asyncio.create_task(get_cat_fact(session)) for _ in range(5)]
    dog_cat_facts = await asyncio.gather(*dog_tasks, *cat_tasks)
    mixed_facts = await mix_facts(dog_cat_facts[:5], dog_cat_facts[5:])
    print(mixed_facts)

asyncio.run(main())
