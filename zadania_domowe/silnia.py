n = input("Podj liczbę, z której chcesz utworzyć silnie: ")
n = int(n)
if n < 0:
    print("nie ma silni dla liczb ujemnych")
elif n == 0:
    print("Silnia z 0 to 1")
else:
    silnia = 1
    for i in range (1, n+1):
        silnia = silnia*i
        print(silnia)
wynik = silnia
print(f"Silnia ! z zadanej wartości to: {wynik}")