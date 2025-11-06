godina = int(input("Unesite godinu: "))

def prijestupna_godina(godina):
  if godina % 400 == 0:
    return True
  elif godina % 4 == 0 and godina % 100 != 0:
    return True
  else:
    return False
    

if prijestupna_godina(godina):
  print(f"Godina {godina}. je prijestupna.")
else:
  print(f"Godina {godina}. nije prijestupna.")