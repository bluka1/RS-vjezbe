# Zadatak 5: Proizvodi i ruta za narudžbe
# Nadogradite poslužitelj iz prethodnog zadatka na način da podržava i POST metodu na putanji /narudzbe. 
# Ova ruta prima JSON podatke o novoj narudžbu u sljedećem obliku.
# Za početak predstavite da je svaka narudžba jednostavna i sadrži samo jedan proizvod i naručenu količinu:

# {
#   "proizvod_id": 1,
#   "kolicina": 2
# }

# Handler korutina ove metode mora provjeriti postoji li proizvod s traženim ID-em unutar liste proizvodi. 
# Ako ne postoji, vratite odgovor s statusom 404 i porukom {'error': 'Proizvod s traženim ID-em ne postoji'}. 
# Ako proizvod postoji, dodajte novu narudžbu u listu narudžbi i vratite odgovor s nadopunjenom listom narudžbi u JSON formatu i prikladnim statusnim kôdom.

# Listu narudžbi definirajte globalno, kao praznu listu.

# Vaš konačni poslužitelj mora sadržavati 3 rute: /proizvodi, /proizvodi/{id} i /narudzbe.

# Testirajte poslužitelj na sve slučajeve kroz klijentsku sesiju unutar main korutine iste skripte.

proizvodi = [
  {"id": 1, "naziv": "Laptop", "cijena": 5000},
  {"id": 2, "naziv": "Miš", "cijena": 100},
  {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
  {"id": 4, "naziv": "Monitor", "cijena": 1000},
  {"id": 5, "naziv": "Slušalice", "cijena": 50}
]

narudzbe = []

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

async def add_narudzba(request):
  res = await request.json()
  # postoji_u_narudzbama = False
  # trazena_narudzba = None
  for p in proizvodi:
    if p['id'] == res['proizvod_id']:
      narudzbe.append(res)
      return web.json_response(narudzbe, status=201)
      # potencijalno rješenje ako na primjer prikupljamo narudžbe za jednog kupca ili sumiramo narudžbe

      # for n in narudzbe:
        # if n['proizvod_id'] == res['proizvod_id']:
        #   postoji_u_narudzbama = True
        #   trazena_narudzba = n

      # if postoji_u_narudzbama:
      #   trazena_narudzba['kolicina'] += res['kolicina']
      #   return web.json_response(narudzbe, status=200)
      # else:
      #   narudzbe.append(res)
      #   return web.json_response(narudzbe, status=201)
  return web.json_response({'error': 'Proizvod s traženim ID-em ne postoji'}, status=404)

app = web.Application()
app.router.add_get('/proizvodi', get_proizvodi)
app.router.add_get('/proizvodi/{id}', get_proizvod_by_id)
app.router.add_post('/narudzbe', add_narudzba)

async def start_server():
  runner = AppRunner(app)
  await runner.setup()
  site = web.TCPSite(runner, 'localhost', 8081)
  await site.start()
  print('Server je startao na - http://localhost:8081')


narudzba_za_dodati = {
  "proizvod_id": 1,
  "kolicina": 2
}
narudzba2_za_dodati = {
  "proizvod_id": 1,
  "kolicina": 2
}
narudzba3_za_dodati = {
  "proizvod_id": 10,
  "kolicina": 2
}
async def main():
  asyncio.create_task(start_server())
  async with aiohttp.ClientSession() as session:
    proizvodi_res = await session.get('http://localhost:8081/proizvodi')
    print('proizvodi_res: ', await proizvodi_res.text())
    proizvod_1_res = await session.get('http://localhost:8081/proizvodi/1')
    print('proizvod_1_res: ', await proizvod_1_res.text())
    proizvod_7_res = await session.get('http://localhost:8081/proizvodi/7')
    print('proizvod_1_res: ', await proizvod_7_res.text())
   
    narudzba1 = await session.post('http://localhost:8081/narudzbe', json=narudzba_za_dodati)
    print('*****************')
    print('narudzba1 status code:', narudzba1.status)
    print('narudzba1:', await narudzba1.text())
    print('*****************')
    narudzba2 = await session.post('http://localhost:8081/narudzbe', json=narudzba2_za_dodati)
    print('*****************')
    print('narudzba2 status code:', narudzba2.status)
    print('narudzba2:', await narudzba2.text())
    print('*****************')
    narudzba3 = await session.post('http://localhost:8081/narudzbe', json=narudzba3_za_dodati)
    print('*****************')
    print('narudzba3 status code:', narudzba3.status)
    print('narudzba3:', await narudzba3.text())
    print('*****************')


asyncio.run(main())
