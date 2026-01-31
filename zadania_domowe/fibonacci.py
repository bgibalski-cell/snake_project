n = input("Podaj długość ciagu Fibonacciego: ")
n = int(n)
a = 0
b = 1
ciag_f =[a,b]
for i in range(1,n):
    b = b + a
    a = b - a
    ciag_f.append(b)
print(f"Twoj ciag Fibonacciego to: {ciag_f}")