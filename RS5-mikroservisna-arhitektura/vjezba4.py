# Definirajte aiohttp poslužitelj koji radi na portu 8081 . Poslužitelj mora imati dvije rute: /proizvodi i
# /proizvodi/{id} . Prva ruta vraća listu proizvoda u JSON formatu, a druga rutu vraća točno jedan proizvod
# prema ID-u. Ako proizvod s traženim ID-em ne postoji, vratite odgovor s statusom 404 i porukom
# {'error': 'Proizvod s traženim ID-em ne postoji'} .
# Proizvode pohranite u listu rječnika:

from aiohttp import web
from aiohttp.web import AppRunner
import asyncio, aiohttp

proizvodi = [
  {"id": 1, "naziv": "Laptop", "cijena": 5000},
  {"id": 2, "naziv": "Miš", "cijena": 100},
  {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
  {"id": 4, "naziv": "Monitor", "cijena": 1000},
  {"id": 5, "naziv": "Slušalice", "cijena": 50}
]

async def get_proizvodi(request):
  return web.json_response(proizvodi)

async def get_proizvod_by_id(request):
  proizvod_id = request.match_info.get('id')
  if proizvod_id is None:
    return web.json_response({'error': 'ID nije naveden.'}, status=400)
  
  for p in proizvodi:
    if p['id'] == int(proizvod_id):
      return web.json_response(p, status=200)
    else:
      return web.json_response({'error': 'Proizvod s traženim ID-em ne postoji'}, status=404)


app = web.Application()
app.router.add_get('/proizvodi', get_proizvodi)
app.router.add_get('/proizvodi/{id}', get_proizvod_by_id)

async def start_server():
  runner = AppRunner(app)
  await runner.setup()
  site = web.TCPSite(runner, 'localhost', 8080)
  await site.start()
  print("Poslužitelj sluša na http://localhost:8080")

async def main():
  await start_server()
  async with aiohttp.ClientSession() as session:
    res = await session.get('http://localhost:8080/proizvodi')
    proizvodi = await res.text()
    print(proizvodi)
    res2 = await session.get('http://localhost:8080/proizvodi/6')
    proizvod = await res2.text()
    print(proizvod)
    res3 = await session.get('http://localhost:8080/proizvodi/')
    proizvod2 = await res3.text()
    print(proizvod2)
    res4 = await session.get('http://localhost:8080/proizvodi/1')
    proizvod3 = await res4.text()
    print(proizvod3)

asyncio.run(main())
