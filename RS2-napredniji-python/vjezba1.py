# kvadriranje broja
def kvadriraj(x):
    return x ** 2

lambda x: x * 2

# zbroji pa kvadriraj
def zbroji_pa_kvadriraj(a, b):
    return (a + b) ** 2

lambda a, b: (a + b) ** 2

# kvadriraj duljinu niza
def kvadriraj_duljinu(niz):
    return len(niz) ** 2

lambda niz : len(niz) ** 2

# pomnoži vrijednost s 5 pa potenciraj na x
def pomnozi_i_potenciraj(x, y):
    return (y * 5) ** x

lambda x, y : (y * 5) ** x

# vrati True ako je broj paran, inače vrati None
def paran_broj(x):
    if x % 2 == 0:
        return True
    else:
        return None

lambda x : True if x % 2 else None
