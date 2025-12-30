from typing import Literal
from models.film import Film

def filtriraj_filmove(
  f: Film,
  min_year: int = None,
  max_year: int = None,
  min_rating: float = None,
  max_rating: float = None,
  type: Literal['movie', 'series'] = None
) -> bool:
  YEAR = 'Year'
  RATING = 'imdbRating'
  TYPE = 'Type'
  return (
    (min_year is None or f.Year >= min_year) and 
    (max_year is None or f.Year <= max_year) and 
    (min_rating is None or (float(f.imdbRating) >= min_rating)) and 
    (max_rating is None or (float(f.imdbRating) <= max_rating)) and 
    (type is None or f.Type == type)
  )
