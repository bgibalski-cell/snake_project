def hex_decorator(func):
    def wrapper(a, b):

        wynik = func(a, b)
        return hex(int(wynik))
    return wrapper

@hex_decorator
def dodawanie(a, b):
    return a + b

@hex_decorator
def odejmowanie(a, b):
    return a - b

@hex_decorator
def mnozenie(a, b):
    return a*b

@hex_decorator
def dzielenie(a,b):
    return a/b


def hex_math(a, b, func):
    return func(a, b)


print(hex_math(10, 5, dodawanie))
print(hex_math(10, 5, odejmowanie))
print(hex_math(10, 5, mnozenie))
print(hex_math(10, 5, dzielenie))