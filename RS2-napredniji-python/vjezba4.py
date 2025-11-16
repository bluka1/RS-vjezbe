import datetime
import functools
import math

# Definirajte klasu Automobil s atributima marka, model, godina_proizvodnje i kilometraža. Dodajte metodu ispis koja će ispisivati sve atribute automobila.
# Stvorite objekt klase Automobil s proizvoljnim vrijednostima atributa i pozovite metodu ispis.
# Dodajte novu metodu starost koja će ispisivati koliko je automobil star u godinama, trenutnu godine dohvatite pomoću datetime modula.

class Automobil():
  def __init__(self, _marka, _model, _gp, _kilometraza):
    self.marka = _marka
    self.model = _model
    self.godina_proizvodnje = _gp
    self.kilometraza = _kilometraza

  def atributi(self):
    print(list(self.__dict__))
  
  def startost(self):
    print(datetime.datetime.now().year - self.godina_proizvodnje)

auto = Automobil("Toyota", "RAV 4", 2025, 0)
auto.atributi()
auto.startost()

# 2. Definirajte klasu Kalkulator s atributima a i b. Dodajte metode zbroj, oduzimanje, mnozenje, dijeljenje, 
# potenciranje i korijen koje će izvršavati odgovarajuće operacije nad atributima a i b.
class Kalkulator():
  def __init__(self, _a, _b):
    self.a = _a
    self.b = _b

  def zbroj(self):
    return self.a + self.b

  def oduzimanje(self):
    return self.a - self.b

  def mnozenje(self):
    return self.a * self.b

  def dijeljenje(self):
    return self.a / self.b

  def potenciranje(self):
    return self.a ** self.b

  def bkorijen_iz_a(self):
    return self.a ** (1/self.b)
  
  def akorijen_iz_b(self):
    return self.b ** (1/self.a)
  
  def korijen(self):
    return (self.a ** 0.5, self.b ** 0.5)
  

# 3. Definirajte klasu Student s atributima ime, prezime, godine i ocjene.
class Student():
  def __init__(self, _ime, _prezime, _godine, _ocjene):
    self.ime = _ime
    self.prezime = _prezime
    self.godine = _godine
    self.ocjene = _ocjene
  
  def prosjek(self):
    return sum(self.ocjene) / len(self.ocjene)

# Iterirajte kroz sljedeću listu studenata i za svakog studenta stvorite objekt klase Student i dodajte ga u novu listu studenti_objekti:

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
    {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
    {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
    {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]

studenti_objekti = [Student(student['ime'], student['prezime'], student['godine'], student['ocjene']) for student in studenti]

# Dodajte metodu prosjek koja će računati prosječnu ocjenu studenta.
# U varijablu najbolji_student pohranite studenta s najvećim prosjekom ocjena iz liste studenti_objekti. Implementirajte u jednoj liniji koda.
najbolji_student = functools.reduce(lambda s1, s2: s1 if s1.prosjek() > s2.prosjek() else s2, studenti_objekti)

print(najbolji_student.__dict__)

# Definirajte klasu Krug s atributom r. Dodajte metode opseg i povrsina koje će računati opseg i površinu kruga.
class Krug():
  def __init__(self, _r):
    self.r = _r

  def opseg(self):
    return 2 * self.r * math.pi

  def povrsina(self):
    return self.r ** 2 * math.pi


# Stvorite objekt klase Krug s proizvoljnim radijusom i ispišite opseg i površinu kruga.
krug = Krug(5)
print(krug.opseg())
print(krug.povrsina())

# Definirajte klasu Radnik s atributima ime, pozicija, placa. Dodajte metodu work koja će ispisivati "Radim na poziciji {pozicija}".
class Radnik():
  def __init__(self, _ime, _pozicija, _placa):
    self.ime = _ime
    self.pozicija = _pozicija
    self.placa = _placa

  def work(self):
    print(f"Radim na poziciji {self.pozicija}")

# Dodajte klasu Manager koja nasljeđuje klasu Radnik i definirajte joj atribut department. Dodajte metodu work koja će ispisivati "Radim na poziciji {pozicija} u odjelu {department}".
class Manager(Radnik):
  def __init__(self, _ime, _pozicija, _placa, _department):
    super().__init__(_ime, _pozicija, _placa)
    self.department = _department

  def work(self):
    print(f"Radim na poziciji {self.pozicija} u odjelu {self.department}")
    
  def give_raise(self, radnik, povecanje):
    radnik.placa = int(radnik.placa) + int(povecanje)

# U klasu Manager dodajte metodu give_raise koja prima parametre radnik i povecanje i povećava plaću radnika (Radnik) za iznos povecanje.

# Definirajte jednu instancu klase Radnik i jednu instancu klase Manager i pozovite metode work i give_raise.
radnik = Radnik("Marko", "developer", "10000")
radnik.work()

manager = Manager("Luka", "CTO", 100000, "Software development")
manager.give_raise(radnik, 2000)
