# Pojasnite zašto sljedeća petlja nema (previše) smisla:
for i in range(1, 2):
  print(i)
# Nema smisla jer se petlja izvršava samo jednom.
# Početna vrijednost je 1, krajnja vrijednost je 2, a nema koraka pa je defaultni korak 1.
# Petlja se, izmedu ostalog, izvršava samo jednom jer kreće od početne vrijednosti koja je uključna u raspon dok krajnja vrijednost nije uključena.

# ================================
# Što će ispisati sljedeća petlja?
for i in range(10, 1, 2):
  print(i)
# Neće ispisati ništa jer je u rangeu početna vrijednost veća od krajnje, a uz to ima i pozitivan korak.
# U toj situaciji range testira je li početna vrijednost manja od krajnje - ako nije, petlja se ne izvršava radi pozitivnog koraka.

# ================================
# Što će ispisati sljedeća petlja?
for i in range(10, 1, -1):
  print(i)
# Ispisat će brojeve od 10 do 2 (uključujući i 2).
# Razlog tome je što je u rangeu dodan negativan korak.
# Dakle, ovdje se provjerava je li početna vrijednost veća od krajnje radi negativnog koraka.