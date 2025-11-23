# Nadogradite poslužitelj iz prethodnog zadatka na način da na istoj putanji /proizvodi prima POST zahtjeve
# s podacima o proizvodu. Podaci se šalju u JSON formatu i sadrže ključeve naziv , cijena i količina .
# Handler funkcija treba ispisati primljene podatke u terminalu, dodati novi proizvod u listu proizvoda i vratiti
# odgovor s novom listom proizvoda u JSON formatu.

from aiohttp import web

proizvodi = [
  {"naziv": "mobitel", "cijena": 1000, "kolicina": 1000}, 
  {"naziv": "tablet", "cijena": 777, "kolicina": 77}
]

async def get_proizvodi(request):
  return web.json_response(proizvodi)

async def add_proizvodi(request):
  data = await request.json()
  proizvodi.append(data)
  print(data)
  return web.json_response(proizvodi)

app = web.Application()
app.router.add_get('/proizvodi', get_proizvodi)
app.router.add_post('/proizvodi', add_proizvodi)

web.run_app(app, host='localhost', port=8081)

# curl http://localhost:8081/proizvodi

# curl -X POST -H "Content-Type: application/json" -d '{"naziv": "pametni sat", "cijena": 500, "kolicina": 50}' http://localhost:8081/proizvodi
# curl -X POST -H "Content-Type: application/json" -d '{"naziv": "kamera", "cijena": 90, "kolicina": 40}' http://localhost:8081/proizvodi
# curl -X POST -H "Content-Type: application/json" -d '{"naziv": "robot usisavač", "cijena": 130, "kolicina": 20}' http://localhost:8081/proizvodi
