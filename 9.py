""""
Funkcje
"""
from copy import deepcopy
import os



def print_args(*args):
    print('Krotka z argumentami: ', args)


print_args(1, 2, 3)


def print_args(*args):
    x = args[0]
    print('Krotka z argumentami: ', *args)
    print('Pierwsza pozycja krotki: ', x)


print_args(1, 2, 3)


def print_kwargs(**kwargs):
    print('Słownik z argumentami: ', kwargs)


print_kwargs()
print_kwargs(wine='merlot', entree='baranina', dessert='lody')


def print_kwargs(**kwargs):
    x = kwargs['wine']
    print('Słownik z argumentami: ', *kwargs)
    print('Pierwsza pozycja słownika: ', x)


print_kwargs(wine='merlot', entree='baranina', dessert='lody')


def print_data(dane, *, start=0, end=100):
    # argumenty w wywołaniu po '*' muszą być nazwane, chyba, że mają wartości domyślne
    for value in (dane[start:end]):
        print(value)


data = ['a', 'b', 'c', 'd', 'e', 'f']
print_data(data)
print()
print_data(data, start=4)
print()
print_data(data, end=2)

outside = ['jaki', 'piękny', 'dzień']


def mangle1(arg):
    """uwaga! jeśli arg będzie typem mutowalnym to funkcja może zmienić wartość zmiennej podanej jako argument"""
    arg[1] = 'okropny'


print(help(mangle1))  # wyświetlenie komentarza dokumentacyjnego w sposób sformatowany
print('oryginalny: ', outside)
mangle1(outside)
print('po funkcji: ', outside)

outside = ['jaki', 'piękny', 'dzień']


def mangle2(arg):
    """ a to jest jedno z rozwiązań tego problemu """
    x = deepcopy(arg)
    x[1] = 'okropny'


print()
print(mangle2.__doc__)  # wyświetlenie komentarza dokumentacyjnego w sposób niesformatowany
print('oryginalny: ', outside)
mangle2(outside)
print('po funkcji: ', outside)


def answer():
    print(42)


def run_something(func):
    """ funkcja wywołująca inna funkcję """
    func()


print(run_something(answer))


def add_args(arg1, arg2):
    print(arg1 + arg2)


def run_something_with_args(func, arg1, arg2):
    """ funkcja wywołująca inna funkcję z parametrami """
    func(arg1, arg2)


run_something_with_args(add_args, 5, 9)


def sum_args(*args):
    return sum(args)


def multiply_args(*args):
    x = 1
    for i in args:
        x *= i
    return x


def run_with_positional_args(func, *args):
    return func(*args)


arguments1 = (1, 2, 3, 4)
arguments2 = [1, 2, 3, 4]
print(run_with_positional_args(sum_args, 1, 2, 3, 4))
print(run_with_positional_args(multiply_args, 1, 2, 3, 4))
print(run_with_positional_args(multiply_args, *arguments1))
print(run_with_positional_args(multiply_args, *arguments2))


def knights2(saying):
    """ funkcja zwraca funkcję"""
    def inner2():
        return "Jesteśmy rycerzami, którzy mówią: '%s'" % saying
    return inner2


a = knights2('kaczka')
b = knights2('gulasz z królika')

print(type(a))
print(type(b))

print(a())
print(b())


""" Dekoratory"""


def document_it(func):
    def new_function(*args, **kwargs):
        print('Nazwa funkcji:', func.__name__)
        print('Argumenty pozycyjne:', args)
        print('Argumenty nazwane:', kwargs)
        result = func(*args, **kwargs)
        print('Wynik:', result)
        return result
    return new_function


def add_ints1(a, b):
    return a + b


print()
cooler_add_ints = document_it(add_ints1)  # Ręcznie zastosowany dekorator
print('Ręczny dekorator: ', cooler_add_ints(3, 5))


@document_it  # Aleternatywny sposób dekorowania
def add_ints2(a, b):
    return a + b


print()
print('Dekorator alternatywny: ', add_ints2(3, 5))


def square_it(func):  # drugi dekorator
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function


@document_it
@square_it
def add_ints3(a, b):
    return a + b


print()
print('Dwa dekoratory: ', add_ints3(3, 5))


@square_it
@document_it
def add_ints4(a, b):
    return a + b


print()
print('Dwa dekoratory ale odwrotnie: ', add_ints4(3, 5))


animal = 'kot'
def change_and_print_global():
    # print('Wartość wewnątrz funkcji change_and_print_global:', animal)
    global animal
    animal = 'pies'
    print('Wartość po zmianie:', animal)
    print(change_and_print_global.__name__)

print()
change_and_print_global()
print(animal)

print()
print(globals())
print(__name__)
print(__file__)


""" Rekurencja """
def flatten1(lol):  # zastosowanie rekurencji i funkcji generatorej do spłaszczenia zagnieżdżonych list
    for item in lol:
        if isinstance(item, list):
            for subitem in flatten1(item):
                yield subitem
        else:
            yield item

lol = [1, 2, [3,4,5], [6,[7,8,9], []]]
print(list(flatten1(lol)))

def flatten2(lol):  # zastosowanie rekurencji i wyrażenia generatorowego do spłaszczenia zagnieżdżonych list
    for item in lol:
        if isinstance(item, list):
            yield from flatten2(item)
        else:
            yield item

print(list(flatten2(lol)))
