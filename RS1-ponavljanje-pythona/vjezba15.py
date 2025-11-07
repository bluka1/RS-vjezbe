vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

def count_vowels_consonants(str):
  rjecnik = {
    "samoglasnici": 0,
    "suglasnici": 0
  }
  for char in str:
    if char in vowels:
      rjecnik["samoglasnici"] += 1
    elif char in consonants:
      rjecnik["suglasnici"] += 1
    else:
      continue
  return rjecnik


tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

print(count_vowels_consonants(tekst))
