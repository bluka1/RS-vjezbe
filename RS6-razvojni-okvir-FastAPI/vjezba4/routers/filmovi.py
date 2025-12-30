from fastapi import APIRouter, HTTPException
from typing import Literal
from helpers.pronadi_film import pronadi_film
from helpers.filtriraj_filmove import filtriraj_filmove
from lista_filmova import filmovi
from models.film import Film

router = APIRouter()

@router.get('/filmovi', response_model=list[Film])
def get_filmovi(
  min_year: int = None, 
  max_year: int = None, 
  min_rating: float = None, 
  max_rating: float = None, 
  type: Literal['movie', 'series'] = None
):
  if min_year is not None and max_year is not None and min_year > max_year:
    raise HTTPException(status_code=400, detail='min_year mora biti manji od max_year')
  
  if min_rating is not None and max_rating is not None and min_rating > max_rating:
    raise HTTPException(status_code=400, detail='min_rating mora biti manji od max_rating')
  
  if type is not None and type not in ('movie', 'series'):
    raise HTTPException(status_code=400, detail='type mora biti movie ili series')
  
  return list(filter(lambda f: filtriraj_filmove(f, min_year, max_year, min_rating, max_rating, type), filmovi))

@router.get('/filmovi/imdbid/{imdbID}', response_model=Film)
def get_film_by_imdbId(imdbID: str):
  return pronadi_film('imdbID', imdbID)

@router.get('/filmovi/title/{title}', response_model=Film)
def get_film_by_title(title: str):
  return pronadi_film('Title', title)
