# Napišite program koji ispisuje sumu svih parnih brojeva od 1 do 100 (uključivo).
zbroj = 0
for i in range(1, 101, 2):
  zbroj += i
print(zbroj)
print("================================================")
# Napišite program koji ispisuje prvih 10 neparnih brojeva u obrnutom redoslijedu.
for i in range(19, 0, -2):
  print(i)
print("================================================")

# Napišite program koji ispisuje Fibonaccijev niz do 1000. Fibonaccijev niz počinje s brojevima 0 i 1, a svaki sljedeći broj je zbroj prethodna dva broja.
a = 0
b = 1
for i in range(1, 1000):
  print(f"{i}. {a}")
  a, b = b, a + b
