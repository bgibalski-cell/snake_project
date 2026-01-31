def Fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    ciag_f = [0, 1]
    for i in range(1,n):
        ciag_f.append(ciag_f[-1]+ciag_f[-2])
        print(ciag_f[-2])
        print(ciag_f[-1])

    return  ciag_f
n = int(input("Podaj długość ciagu Fibonacciego:  "))
print(Fibonacci(n))