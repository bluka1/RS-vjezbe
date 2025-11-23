# Definirajte poslužitelj koji sluša na portu 8082 i na putanji /punoljetni vraća listu korisnika starijih od 18
# godina. Svaki korisnik je rječnik koji sadrži ključeve ime i godine . Pošaljite zahtjev na adresu
# http://localhost:8082/punoljetni i provjerite odgovor. Novu listu korisnika definirajte koristeći funkciju
# filter ili list comprehension .

from aiohttp import web

korisnici = [
  {'ime': 'Ivo', 'godine': 25},
  {'ime': 'Ana', 'godine': 17},
  {'ime': 'Marko', 'godine': 19},
  {'ime': 'Maja', 'godine': 16},
  {'ime': 'Iva', 'godine': 22}
]

async def get_punoljetni(request):
  return web.json_response(list(filter(lambda k: k['godine'] > 17, korisnici)))

app = web.Application()

app.router.add_get('/punoljetni', get_punoljetni)

web.run_app(app, host='localhost', port=8082)

# curl http://localhost:8082/punoljetni
