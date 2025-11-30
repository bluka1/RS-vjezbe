# Zadatak 1: fetch_users i izdvajanje podataka
# Definirajte korutinu fetch_users koja će slati GET zahtjev na JSONPlaceholder API na URL-u: https://jsonplaceholder.typicode.com/users. 
# Morate simulirate slanje 5 zahtjeva konkurentno unutar main korutine. Unutar main korutine izmjerite vrijeme izvođenja programa, 
# a rezultate pohranite u listu odjedanput koristeći asyncio.gather funkciju. Nakon toga koristeći map funkcije ili list comprehension 
# izdvojite u zasebne 3 liste: samo imena korisnika, samo email adrese korisnika i samo username korisnika. 
# Na kraju main korutine ispišite sve 3 liste i vrijeme izvođenja programa.

import aiohttp
import asyncio
import time

API_URL = 'https://jsonplaceholder.typicode.com/users'

async def fetch_users(session):
  res = await session.get(API_URL)
  data = await res.json()
  return data

async def main():
  t1 = time.perf_counter()
  async with aiohttp.ClientSession() as session:
    tasks = [asyncio.create_task(fetch_users(session)) for _ in range(5)]
    results = await asyncio.gather(*tasks)
    korisnici, emailovi, usernameovi = [[x[key] for lista in results for x in lista] for key in ('name', 'email', 'username')]
  t2 = time.perf_counter()
  print(f'VRIJEME: {t2 - t1:.2f}')
  print(f'KORISNICI: {korisnici}')
  print(f'EMAILOVI: {emailovi}')
  print(f'USERNAMEOVI: {usernameovi}')

asyncio.run(main())
