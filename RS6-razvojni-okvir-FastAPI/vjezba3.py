# 3.2 Zadaci za vježbu: Obrada grešaka
# Definirajte rutu i odgovarajući Pydantic model za dohvaćanje podataka o automobilima. Svaki automobil ima sljedeće atribute: id, marka, model, godina_proizvodnje, cijena i boja. Ako korisnik pokuša dohvatiti automobil s ID-em koji ne postoji, podignite iznimku HTTPException s statusom 404 i porukom Automobil nije pronađen.

# Nadogradite prethodnu rutu s query parametrima min_cijena, max_cijena, min_godina i max_godina. Implementirajte validaciju query parametra za cijenu i godinu proizvodnje. Minimalna cijena mora biti veća od 0, a minimalna godina proizvodnje mora biti veća od 1960. Unutar funkcije obradite iznimku kada korisnik unese minimalnu cijenu veću od maksimalne cijene ili minimalnu godinu proizvodnje veću od maksimalne godine proizvodnje te vratite odgovarajući HTTPException.

# Definirajte rutu za dodavanje novog automobila u bazu podataka. id se mora dodati na poslužitelju, kao i atribut cijena_pdv (definirajte dodatni Pydantic model za to). Ako korisnik pokuša dodati automobil koji već postoji u bazi podataka, podignite odgovarajuću iznimku. Implementirajte ukupno 3 Pydantic modela, uključujući BaseCar model koji će nasljeđivati preostala 2 modela.

from fastapi import FastAPI, HTTPException, status, Query
from models import CarResponse, CarCreate
from typing import Optional

app = FastAPI()

automobili = []
@app.get('/automobili', response_model=list[CarResponse])
def get_automobili(max_cijena: Optional[float] = Query(title='maksimalna cijena', default=None), max_godina: Optional[int] = Query(title='maksimalna godina proizvodnje', default=None), min_godina: Optional[int] = Query(title='minimalna godina proizvodnje', ge=1960, default=None), min_cijena: Optional[float] = Query(title='minimalna cijena', ge=0, default=None)):
  if min_cijena is not None and max_cijena is not None and min_cijena > max_cijena:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Minimalna cijena mora biti manja od maksimalne cijene.')
  if min_godina is not None and max_godina is not None and min_godina > max_godina:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Minimalna godina mora biti manja od maksimalne godine.')
  return [a for a in automobili if (min_cijena is None or a['cijena'] >= min_cijena) and (max_cijena is None or a['cijena'] <= max_cijena) and (min_godina is None or a['godina_proizvodnje'] >= min_godina) and (max_godina is None or a['godina_proizvodnje'] <= max_godina)]

@app.get('/automobili/{id}', response_model=CarResponse)
def get_automobili(id: int):
  a = next((a for a in automobili if a['id'] == id), None)
  if a is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Automobil nije pronaden')
  return a

@app.post('/automobili', response_model=CarResponse)
def add_automobil(auto: CarCreate):
  auto = auto.model_dump()
  PDV_MULTIPLIER = 1.25
  a = next((a for a in automobili if len(automobili) != 0 and (a['model'] == auto['model'] and a['marka'] == auto['marka'])), None)

  if a is not None:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Automobil već postoji u bazi')
  
  cijena_s_pdv: float = auto['cijena'] * PDV_MULTIPLIER
  novi_id: int = max((car['id'] for car in automobili), default=0) + 1
  auto_za_bazu: CarResponse = {'id': novi_id, 'cijena_pdv': cijena_s_pdv, **auto}
  automobili.append(auto_za_bazu)
  return auto_za_bazu

# curl 'http://localhost:8000/automobili?min_cijena=5000&max_cijena=20000&min_godina=2010&max_godina=2020'
# curl 'http://localhost:8000/automobili?min_cijena=20000&max_cijena=10000'
# curl 'http://localhost:8000/automobili?min_godina=2005'
# curl http://localhost:8000/automobili/2
# curl http://localhost:8000/automobili/25
# curl -X POST -H "Content-Type: application/json" -d '{"marka": "Toyota", "model": "Corolla", "godina_proizvodnje": 2015, "cijena": 25000, "boja": "bijela"}' http://localhost:8000/automobili
# curl -X POST -H "Content-Type: application/json" -d '{"marka": "Toyota", "model": "Rav4", "godina_proizvodnje": 2025, "cijena": 45000, "boja": "zelena"}' http://localhost:8000/automobili
