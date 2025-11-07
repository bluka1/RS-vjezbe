def isPrime(broj):
  if broj <= 1:
    return False
  for i in range(broj - 1, 1, -1):
    if broj % i == 0:
      return False
  return True

# alternativno se mogu provjeriti samo dijeljenje s brojevima manjima od korijena unesenog broja
# for i in range(2, int(broj ** 0.5) + 1):
#   if broj % i == 0:
#     return False
# return True
print(isPrime(10))


def primes_in_range(start, end):
  primes = []
  for i in range(start, end + 1):
    if isPrime(i):
      primes.append(i)
  return primes

print(primes_in_range(1, 10))
