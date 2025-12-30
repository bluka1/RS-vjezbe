import json
from models.film import Film

YEAR = 'Year'
IMDB_RATING = 'imdbRating'
IMDB_VOTES = 'imdbVotes'
RUNTIME = 'Runtime'

with open('./filmovi.json', 'r') as data:
  filmovi = json.load(data)

for film in filmovi:
  try:
    if '–' in film[YEAR]:
      start_year, _ = film[YEAR].split('–')
      film[YEAR] = int(start_year)
    else:
      film[YEAR] = int(film[YEAR])
  except ValueError:
    film[YEAR] = 1901

for film in filmovi:
  film[IMDB_RATING] = float(film[IMDB_RATING]) if film[IMDB_RATING] != 'N/A' else 0.1
  film[IMDB_VOTES] = int(film[IMDB_VOTES].replace(',', '')) if film[IMDB_VOTES] != 'N/A' else 1
  film[RUNTIME] = int(film[RUNTIME].replace(' min', '')) if film[RUNTIME] != 'N/A' else 1

filmovi = [Film(**film) for film in filmovi]
