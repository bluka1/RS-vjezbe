# Definirajte korutinu fetch_users koja će slati GET zahtjev na JSONPlaceholder API na URL-u:
# https://jsonplaceholder.typicode.com/users . Morate simulirate slanje 5 zahtjeva konkurentno
# unutar main korutine. Unutar main korutine izmjerite vrijeme izvođenja programa, a rezultate
# pohranite u listu odjedanput koristeći asyncio.gather funkciju. Nakon toga koristeći map funkcije ili
# list comprehension izdvojite u zasebne 3 liste: samo imena korisnika, samo email adrese korisnika i
# samo username korisnika. Na kraju main korutine ispišite sve 3 liste i vrijeme izvođenja programa.

import asyncio
import time
import aiohttp

USERS_API_URL = 'https://jsonplaceholder.typicode.com/users'

async def fetch_users(session):
  res = await session.get(USERS_API_URL)
  users = await res.json()
  return users


async def main():
  t1 = time.perf_counter()
  async with aiohttp.ClientSession() as session:
    zadaci = [asyncio.create_task(fetch_users(session)) for i in range(1,6)]
    rezultati = await asyncio.gather(*zadaci)
    imena, emailovi, usernameovi = ([x[key] for lista in rezultati for x in lista] for key in ('name', 'email', 'username'))
    # ILI
    # imena = [x['name'] for lista in rezultati for x in lista]
    # emailovi = [x['email'] for lista in rezultati for x in lista]
    # usernameovi = [x['username'] for lista in rezultati for x in lista]
  t2 = time.perf_counter()
  print('\n', 'IMENA:', imena, '\n')
  print('\n', 'EMAILOVI:', emailovi, '\n')
  print('\n', 'USERNAMEOVI:', usernameovi, '\n')
  print(f"VRIJEME: {t2 - t1:.2f}")

asyncio.run(main())
