# 2.2 Zadaci za vježbu - Osnove definicije ruta i Pydantic modela
# Definirajte novu FastAPI rutu GET /filmovi koja će klijentu vraćati listu filmova definiranu u sljedećoj listi:

# Nadogradite prethodnu rutu na način da će output biti validiran Pydantic modelom Film kojeg definirate u zasebnoj datoteci models.py.
# Definirajte novu FastAPI rutu GET /filmovi/{id} koja će omogućiti pretraživanje novog filma prema id-u definiranom u parametru rute id. Dodajte i ovdje validaciju Pydantic modelom Film.
# Definirajte novu rutu POST /filmovi koja će omogućiti dodavanje novog filma u listu filmova. Napravite novi Pydantic model CreateFilm koji će sadržavati atribute naziv, genre i godina, a kao output vraćajte validirani Pydantic model Film koji predstavlja novododani film s automatski dodijeljenim id-em.
# Dodajte query parametre u rutu GET /filmovi koji će omogućiti filtriranje filmova prema genre i min_godina. Zadane vrijednosti za query parametre neka budu None i 2000.

filmovi = [
  {"id": 1, "naziv": "Titanic", "genre": "drama", "godina": 1997},
  {"id": 2, "naziv": "Inception", "genre": "akcija", "godina": 2010},
  {"id": 3, "naziv": "The Shawshank Redemption", "genre": "drama", "godina": 1994},
  {"id": 4, "naziv": "The Dark Knight", "genre": "akcija", "godina": 2008}
]

from fastapi import FastAPI, HTTPException
from models import Film, CreateFilm

app = FastAPI()

@app.get('/filmovi', response_model=list[Film])
def get_filmovi(genre: str = None, min_godina: int = 2000):
  return [f for f in filmovi if (genre is None or f['genre'] == genre) and (f['godina'] >= min_godina)]

@app.get('/filmovi/{id}', response_model=Film)
def get_film_by_id(id: int):
  p = next((f for f in filmovi if f['id'] == id), None)
  if p is None:
    raise HTTPException(status_code=404, detail=f'Film s id-em {id} nije pronaden.')
  return p

@app.post('/filmovi', response_model=Film)
def create_film(film: CreateFilm):
  id = max([f['id'] for f in filmovi], default=0) + 1
  novi_film: Film = {'id': id, **film.model_dump()}
  filmovi.append(novi_film)
  return novi_film


# curl 'http://localhost:8000/filmovi?genre=akcija&min_godina=2010'
# curl 'http://localhost:8000/filmovi?min_godina=2005'
# curl 'http://localhost:8000/filmovi?genre=drama'
# curl http://localhost:8000/filmovi/2
# curl http://localhost:8000/filmovi/25
# curl -X POST -H "Content-Type: application/json" -d '{"naziv": "Dvojica pape", "genre": "biografija", "godina": 2015}' http://localhost:8000/filmovi
# curl -X POST -H "Content-Type: application/json" -d '{"naziv": "Dvojica pape", "genre": "biografija", "godina": "asdfgh"}' http://localhost:8000/filmovi
