from fastapi import HTTPException
from models.film import Film
from lista_filmova import filmovi

def pronadi_film(field: str, value: any):
  film = next((f.dict() for f in filmovi if f.dict()[field] == value), None)
  if film is None:
    raise HTTPException(status_code=404, detail='Film nije ponaden')
  return Film(**film)
