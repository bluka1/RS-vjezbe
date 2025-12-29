import asyncio
import aiohttp
from aiohttp import web
import time

async def fetch_from_s1():
  async with aiohttp.ClientSession() as session:
    res = await session.get('http://localhost:8081')
    return await res.json()

async def fetch_from_s2():
  async with aiohttp.ClientSession() as session:
    res = await session.get('http://localhost:8082')
    return await res.json()
  
async def fetch_s():
  async with aiohttp.ClientSession() as session:
    r1 = session.get('http://localhost:8081')
    r2 = session.get('http://localhost:8082')
    tasks = [asyncio.create_task(r1), asyncio.create_task(r2)]
    res = await asyncio.gather(*tasks)
    return [await r.json() for r in res]
  
async def main():
  t1 = time.time()
  print('Main korutina pokrenuta')
  # tasks = [asyncio.create_task(fetch_from_s1()), asyncio.create_task(fetch_from_s2())]
  # res1, res2 = await asyncio.gather(*tasks)
  res1, res2 = await fetch_s()
  print(res1)
  print(res2)
  t2 = time.time()
  print(f"VRIJEME: {t2-t1:.2f}")

asyncio.run(main())
