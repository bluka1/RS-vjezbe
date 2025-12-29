import aiohttp
import asyncio

# async def main():
#   print('Main korutina pokrenuta')
#   async with aiohttp.ClientSession() as session:
#     data = [i for i in range(1,11)]
#     p = {"podaci": data}
#     res = await session.post('http://localhost:8081/zbroj', json=p)
#     rez = await res.json()
#     print(rez)
#     d = {"podaci": data, "zbroj": rez.get('zbroj')}
#     res2 = await session.post('http://localhost:8082/ratio', json=d)
#     rez2 = await res2.json()
#     print(rez2)

async def get_korijeni(session, data):
  pod = await session.post('http://localhost:8084/korijeni', json=data)
  data = await pod.json()
  return data

async def get_kvadrati(session, data):
  pod = await session.post('http://localhost:8083/kvadrati', json=data)
  data = await pod.json()
  return data

async def main():
  async with aiohttp.ClientSession() as session:
    tasks = [asyncio.create_task(get_korijeni(session,{'podaci': [4, 9, 16, 25]})), asyncio.create_task(get_kvadrati(session,{'podaci': [5,10,15,25]}))]
    korijeni, kvadrati = await asyncio.gather(*tasks)
    print('korijeni:', korijeni)
    print('kvadrati:', kvadrati)
asyncio.run(main())
