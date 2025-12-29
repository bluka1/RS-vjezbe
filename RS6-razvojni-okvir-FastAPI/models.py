from pydantic import BaseModel, Field
import datetime
from typing import Literal, TypedDict

class Film(BaseModel):
  id: int
  naziv: str
  genre: str
  godina: int

class CreateFilm(BaseModel):
  naziv: str
  genre: str
  godina: int

class Izdavac(BaseModel):
  naziv: str
  adresa: str

class Knjiga(BaseModel):
  naslov: str
  ime_autora: str
  prezime_autora: str
  # godina_izdavanja: int = datetime.today().year -> ovaj kod se izvršava samo kod učitavanja modula tj. kod pokretanja koda
  godina_izdavanja: int = Field(default_factory=lambda : datetime.today().year) # sada imamo kod koji se izvršava prilikom stvaranja instance objekta i dodijeljuje ispravno trenutnu godinu
  broj_stranica: int
  izdavac: Izdavac

class Admin(BaseModel):
  ime: str
  prezime: str
  korisnicko_ime: str
  email: str
  ovlasti: list[Literal['dodavanje', 'brisanje', 'ažuriranje', 'čitanje']] = []

class Jelo(BaseModel):
  id: int
  naziv: str
  cijena: float

class StolInfo(TypedDict):
  broj: int
  lokacija: Literal['terasa', 'balkon', 'pušački dio', 'nepušački dio']

class RestaurantOrder(BaseModel):
  id: int
  ime_kupca: str
  stol_info: StolInfo
  lista_jela: list[Jelo]
  ukupna_cijena: float

class CCTV_frame(BaseModel):
  id: int
  vrijeme_snimanja: datetime
  koordinate: tuple[float, float] = (0.0, 0.0)
