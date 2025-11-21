# Definirajte korutinu get_dog_fact koja dohvaća činjenice o psima sa DOG API.
# Korutina get_dog_fact neka dohvaća činjenicu o psima na URL-u: https://dogapi.dog/api/v2/facts .
# Nakon toga, definirajte korutinu get_cat_fact koja dohvaća činjenicu o mačkama slanjem zahtjeva na
# URL: https://catfact.ninja/fact .

# Istovremeno pohranite rezultate izvršavanja ovih Taskova koristeći asyncio.gather(*dog_facts_tasks,
# *cat_facts_tasks) funkciju u listu dog_cat_facts , a zatim ih koristeći list slicing odvojite u dvije liste
# obzirom da znate da je prvih 5 činjenica o psima, a drugih 5 o mačkama.

# Na kraju, definirajte i treću korutinu mix_facts koja prima liste dog_facts i cat_facts i vraća novu
# listu koja za vrijednost indeksa i sadrži činjenicu o psima ako je duljina činjenice o psima veća od duljine
# činjenice o mačkama na istom indeksu, inače vraća činjenicu o mački. Na kraju ispišite rezultate filtriranog
# niza činjenica. Liste možete paralelno iterirati koristeći zip funkciju, npr. for dog_fact, cat_fact in
# zip(dog_facts, cat_facts) .

import asyncio
import aiohttp

DOG_API_URL = 'https://dogapi.dog/api/v2/facts'
CAT_API_URL = 'https://catfact.ninja/fact'

async def get_dog_fact(session):
  res = await session.get(DOG_API_URL)
  data = await res.json()
  fact = data['data'][0]['attributes']['body']
  return fact

async def get_cat_fact(session):
  res = await session.get(CAT_API_URL)
  data = await res.json()
  fact = data['fact']
  return fact

def mix_facts(dog_facts, cat_facts):
  return [dogf if len(dogf) >= len(catf) else catf for dogf, catf in zip(dog_facts, cat_facts)]

async def main():
  async with aiohttp.ClientSession() as session:
    dog_facts_tasks = [asyncio.create_task(get_dog_fact(session)) for i in range(1,6)]
    cat_facts_tasks = [asyncio.create_task(get_cat_fact(session)) for i in range(1,6)]
    dog_cat_facts = await asyncio.gather(*dog_facts_tasks, *cat_facts_tasks)
    # print('\n','DOG CAT FACTS:', dog_cat_facts, '\n')
    dog_facts, cat_facts = (dog_cat_facts[:5], dog_cat_facts[5:])
    print(mix_facts(dog_facts, cat_facts))

asyncio.run(main())
