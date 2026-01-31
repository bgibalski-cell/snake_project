def silnia (n):
  if n == 0:
      return 0
  elif n == 1:
      return 1
  else:
      return n*silnia(n-1)

n = input("Podaj liczbe z której mam zrobić silnie: ")
n = int(n)
print(f"Silnia z zadanej liczby to: {silnia(n)}")