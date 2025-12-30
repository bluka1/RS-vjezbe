from typing import Literal, Optional
from pydantic import BaseModel, Field

class Actor(BaseModel):
  name: str
  surname: str

class Writer(BaseModel):
  name: str
  surname: str

class Film(BaseModel):
  Title: str = Field(description="Naslov filma")
  Year: int = Field(description="Godina izlaska filma/serije", gt=1900)
  Rated: str
  Released: Optional[str] = None
  Genre: str
  Director: Optional[str] = None
  Writer: str
  Actors: str
  Plot: str
  Language: str
  Country: str
  Awards: Optional[str] = None
  Poster: Optional[str] = None
  Metascore: Optional[str] = None
  imdbRating: Optional[float] = Field(description="Ocjena filma", ge=0, le=10)
  imdbVotes: Optional[int] = Field(description="Broj glasova", gt=0)
  imdbID: Optional[str] = None
  Type: Literal['movie', 'series']
  Response: Optional[str] = None
  Images: list[str]
  Runtime: int = Field(description="Trajanje filma u minutama", gt=0)
