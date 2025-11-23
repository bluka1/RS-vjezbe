# Definirajte aiohttp poslužitelj koji radi na portu 8081 koji na putanji /proizvodi vraća listu proizvoda u
# JSON formatu. Svaki proizvod je rječnik koji sadrži ključeve naziv , cijena i količina . Pošaljite zahtjev na
# adresu http://localhost:8081/proizvodi koristeći neki od HTTP klijenata ili curl i provjerite odgovor

from aiohttp import web

proizvodi = [
  {"naziv": "mobitel", "cijena": 1000, "kolicina": 1000}, 
  {"naziv": "tablet", "cijena": 777, "kolicina": 77}
]

async def get_proizvodi(request):
  return web.json_response(proizvodi)

app = web.Application()
app.router.add_get('/proizvodi', get_proizvodi)

web.run_app(app, host='localhost', port=8081)

# curl http://localhost:8081/proizvodi
