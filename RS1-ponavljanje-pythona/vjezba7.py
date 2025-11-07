def provjera_lozinke(lozinka):
  has_upper = False
  has_digit = False

  for char in lozinka:
    if char.isupper():
      has_upper = True
    elif char.isdigit():
      has_digit = True

  lozinka_lower = lozinka.lower()

  if len(lozinka) < 8 or len(lozinka) > 15:
    print("Lozinka mora sadržavati između 8 i 15 znakova")
  elif lozinka_lower.find("password") != -1 or lozinka_lower.find("lozinka") != -1:
    print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'")
  elif not has_upper or not has_digit:
    print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj")
  # alternativno rješenje za provjeru upper case i brojeva
  # elif not any(char.isdigit() for char in lozinka) or not any(char.isupper() for char in lozinka):
  #   print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj")
  else:
    print("Lozinka je jaka!")


lozinka = input("Unesite lozinku: ")
provjera_lozinke(lozinka)