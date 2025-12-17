# Zadatak 4: Dohvaćanje proizvoda
# Definirajte aiohttp poslužitelj koji radi na portu 8081. Poslužitelj mora imati dvije rute: /proizvodi i /proizvodi/{id}. 
# Prva ruta vraća listu proizvoda u JSON formatu, a druga rutu vraća točno jedan proizvod prema ID-u. 
# Ako proizvod s traženim ID-em ne postoji, vratite odgovor s statusom 404 i porukom {'error': 'Proizvod s traženim ID-em ne postoji'}.

# Proizvode pohranite u listu rječnika:

proizvodi = [
  {"id": 1, "naziv": "Laptop", "cijena": 5000},
  {"id": 2, "naziv": "Miš", "cijena": 100},
  {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
  {"id": 4, "naziv": "Monitor", "cijena": 1000},
  {"id": 5, "naziv": "Slušalice", "cijena": 50}
]
# Testirajte poslužitelj na sve slučajeve kroz klijentsku sesiju unutar main korutine iste skripte.

from aiohttp import web
from aiohttp.web import AppRunner
import asyncio, aiohttp

async def get_proizvodi(request):
  return web.json_response(proizvodi, status=200)

async def get_proizvod_by_id(request):
  id = request.match_info.get('id')
  for p in proizvodi:
    if p['id'] == int(id):
      return web.json_response(p)
  return web.json_response({'error': 'Proizvod s traženim ID-em ne postoji'}, status=404)

app = web.Application()
app.router.add_get('/proizvodi', get_proizvodi)
app.router.add_get('/proizvodi/{id}', get_proizvod_by_id)

async def start_server():
  runner = AppRunner(app)
  await runner.setup()
  site = web.TCPSite(runner, 'localhost', 8081)
  await site.start()
  print('Server je startao na - http://localhost:8081')


async def main():
  asyncio.create_task(start_server())
  async with aiohttp.ClientSession() as session:
    proizvodi_res = await session.get('http://localhost:8081/proizvodi')
    print('proizvodi_res: ', await proizvodi_res.text())
    proizvod_1_res = await session.get('http://localhost:8081/proizvodi/1')
    print('proizvod_1_res: ', await proizvod_1_res.text())
    proizvod_7_res = await session.get('http://localhost:8081/proizvodi/7')
    print('proizvod_1_res: ', await proizvod_7_res.text())

asyncio.run(main())
