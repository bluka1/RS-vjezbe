# 2. **Definirajte `FastAPI` mikroservis** `socialAPI` koji će služiti za dohvaćanje izmišljenih objava na društvenoj mreži. Objave su pohranjene u listi rječnika, gdje svaki rječnik predstavlja jednu objavu. Svaka objava ima sljedeće atribute:

# - `id` - jedinstveni identifikator objave (integer)
# - `korisnik` - korisničko ime autora objave (do 20 znakova)
# - `tekst` - tekst objave (do 280 znakova)
# - `vrijeme` - vrijeme kada je objava napravljena (`timestamp`)
#   <br>
# - definirajte odgovarajuće Pydantic modele za izradu nove objave i dohvaćanje objave.
# - implementirajte rutu `POST /objava` koja dodaje novu objavu u listu objava. Prije dodavanja u listu, obavezno validirajte ulazne podatke. Prilikom dodavanja objave, sve vrijednosti su obavezne, osim `id` atributa koji se automatski dodjeljuje. Logiku dodjeljivanja jedinstvenog identifikatora možete implementirati sami po želji.
# - implementirajte rutu `GET /objava/{id}` koja dohvaća objavu po jedinstvenom identifikatoru.
# - implementirajte rutu `GET /korisnici/{korisnik}/objave` koja dohvaća sve objave korisnika s određenim korisničkim imenom.

# - definirajte `Dockerfile` za `socialAPI` mikroservis i pokrenite ga u Docker kontejneru. Servis treba slušati na portu `3500` domaćina.

from fastapi import FastAPI
from models import Post, PostResponse
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
PORT = int(os.getenv("PORT", 8001))

app = FastAPI()

objave = []

@app.post("/objava")
def dodaj_objavu(post: Post):
  post.id = len(objave) + 1
  objave.append(post)
  return PostResponse(**post.model_dump())

@app.get("/objava/{id}")
def dohvati_objavu(id: int):
  for objava in objave:
    if objava.id == id:
      return PostResponse(**objava.model_dump())
  return {"error": "Objava nije pronađena"}

@app.get("/korisnici/{korisnik}/objave")
def dohvati_objave_korisnika(korisnik: str):
  korisnikove_objave = [PostResponse(**objava.model_dump()) for objava in objave if objava.korisnik == korisnik]
  return korisnikove_objave

import uvicorn
objave.append(Post(id=1, korisnik="korisnik1", tekst="Ovo je prva objava", vrijeme=datetime.now()))
objave.append(Post(id=2, korisnik="korisnik2", tekst="Ovo je druga objava", vrijeme=datetime.now()))
objave.append(Post(id=3, korisnik="korisnik1", tekst="Ovo je treća objava", vrijeme=datetime.now()))
uvicorn.run(app, host="0.0.0.0", port=3500)

# docker build -t socialapi:1.0 . 
# docker run -p 3500:3500 socialapi:1.0 
