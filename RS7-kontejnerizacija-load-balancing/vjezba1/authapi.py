## 1.8 Zadaci za vježbu: Kontejnerizacija mikroservisa

# 1. **Definirajte jednostavni `aiohttp` mikroservis** `authAPI` koji će slušati na portu `9000`. Mikroservis pohranjuje _in-memory_ podatke o korisnicima, s hashiranim lozinkama. U komentarima pored svakog zapisa možete pronaći stvarnu lozinku koja je korištena za generiranje hash vrijednosti funkcijom `hash_data`.
# - implementirajte rutu `POST /register` koja dodaje novog korisnika u listu korisnika. Pohranite samo hashiranu lozinku korisnika.
# - implementirajte rutu `POST /login` koja pronalazi korisnika po korisničkom imenu u listi korisnika i provjerava je li unesena lozinka u tijelu HTTP zahtjeva ispravna, odnosno podudaraju li se hash vrijednosti. Ako se pokuša prijaviti korisnik koji ne postoji, vratite odgovarajući statusni kod i poruku. Ako se lozinke ne podudaraju, vratite odgovarajući statusni kod i poruku.
# - definirajte `Dockerfile` za `authAPI` mikroservis i pokrenite ga u Docker kontejneru. Servis treba slušati na portu `9000` domaćina.

import hashlib
from aiohttp import web
import functools
import asyncio

korisnici = [
  {"korisnicko_ime": "admin", "lozinka_hash" : "8d43d8eb44484414d61a18659b443fbfe52399510da4689d5352bd9631c6c51b"}, # lozinka = "lozinka123"
  {"korisnicko_ime": "markoMaric", "lozinka_hash" : "5493c883d2b943587ea09ab8244de7a0a88d331a1da9db8498d301ca315d74fa"}, # lozinka = "markoKralj123"
  {"korisnicko_ime": "ivanHorvat", "lozinka_hash" : "a31d1897eb84d8a6952f2c758cdc72e240e6d6d752b33f23d15fd9a53ae7c302"}, # lozinka = "lllllllllllozinka_123"
  {"korisnicko_ime": "Nada000", "lozinka_hash":"492f3f38d6b5d3ca859514e250e25ba65935bcdd9f4f40c124b773fe536fee7d"} # lozinka = "blablabla"
]

def hash_data(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

async def handle_register(request):
  data = await request.json()
  ki = data['korisnicko_ime']
  lo = data['lozinka']
  hl = hash_data(lo)
  korisnici.append({
     "korisnicko_ime": ki,
     "lozinka_hash": hl
  })
  return web.json_response('success', status = 200)

async def handle_login(request):
  # print('login trigger')
  data = await request.json()
  ki = data['korisnicko_ime']
  lo = data['lozinka']
  hl = hash_data(lo)
  korisnik = next((k for k in korisnici if k['korisnicko_ime'] == ki), None)
  # print('korisnik:', korisnik)
  if not korisnik:
    return web.json_response('korisnik nije naden', status = 404)
  
  if hl != korisnik['lozinka_hash']:
    return web.json_response('niste autorizirani', status = 401)
  
  return web.json_response('uspjesno ste prijavljeni', status = 200)

app = web.Application()

app.router.add_post('/register', handle_register)
app.router.add_post('/login', handle_login)

web.run_app(app, host='0.0.0.0', port=9000)

# docker build -t authapi:1.0 .
# docker run -p 9000:9000 authapi:1.0
