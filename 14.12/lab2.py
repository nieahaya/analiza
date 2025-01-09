#Napisz funkcję która przyjmuje liczbę x jako jedyny argument i zwraca wartość funkcji f(x) = x^2 + 4x − 3
#dla podanego argumentu x. Użyteczne wyrażenia: def, return.

#x=float(input("Podaj liczbę: "))

def zad1(x):
    return x**2 + 4*x - 3

#print(zad1(x))

#Napisz funkcję, która dodaje dwie liczby a i b podane w argumentach. Funkcja ma być zdefiniowana z jednym
#pozycyjnym (positional) i argumentem nazwanym(keyword/ze zdefiniowaną wartością domyślną). Wartość
#domyślną dla drugiej liczby proszę ustawić na 2. Następnie, wywołaj tą funkcję na 5 różnych możliwych
#sposobów tak, żeby została obliczona suma liczb 1 i 2.

def zad2(a, b=2):
    return a+b

#print(zad2(1))
#print(zad2(a=1))
#print(zad2(1,2))
#print(zad2(1, b=2))
#print(zad2(a=1,b=2))


#Napisz funkcję, która przyjmuje jako argument listę liczb całkowitych, tworzy kopie tej listy i modyfikuje jej
#kopie w następujący sposób:
#• Usuwa wszystkie podzielne przez 3 liczby,
#• Wkleja wartość -1 przed każdą liczbą parzystą.
#Po dokonaniu modyfikacji zmodyfikowana wersja listy ma być zwrócona z funkcji. Przy tym funkcję należy
#napisać tak, żeby lista, podana jako argument została niezmieniona. Zademonstruj działanie funkcji na liście
#liczb losowych z zakresu od 0 do 10.
#Listing 2: Przykładowe działanie programu.
#Lista: [2, 3, 1, 5, 6, 3, 2, 4]
#Wynik: [-1, 2, 1, 5, -1, 2, -1, 4]
#Użyteczne wyrażenia: def, return, copy(), del, pop(), insert().

lista = [2, 3, 1, 5, 6, 3, 2, 4]

def zad3(lista):
    kopia_listy = lista.copy()
    kopia_listy = [x for x in kopia_listy if x % 3 != 0]
 
    i = 0
    while i < len(kopia_listy):
        if kopia_listy[i] % 2 == 0:
            kopia_listy.insert(i, -1)
            i += 1
        i += 1
    return kopia_listy

print(zad3(lista))


#Utwórz funkcję, która przyjmuje trzy argumenty n, a, b i zwraca listę o długości n, wypełnioną losowymi
#liczbami całkowitymi z zakresu od a do b. Argument n ma mieć wartość domyślną 10, argument a wartość
#domyślną 0 i argument b wartość domyślną 10.
#Użyteczne wyrażenia: def, return, random.randrange().

import random

def zad4(n=10,a=0,b=10):
     lista4 = [random.randrange(a,b) for i in range(n)]
     return(lista4)

print(zad4())


#Napisz funkcję, która przyjmuję jeden argument n, i wykonuje następujące rzeczy:
#• Utworzy listę liczb losowych z zakresu od 0 do 10 o długości n (można użyć funkcje z poprzedniego zadania).
#• Wypisze na ekran wylosowaną listę.
#• Wypisze na ekran największą liczbę z listy.
#• Wypisze indeks pod którym znajduje się najmniejsza liczba w liście.
#• Wypisze sumę liczb w liście.
#• Wypisze ile razy w liście występuje wartość 5.
#• Wypisze zbiór liczb unikalnych występujących w tej liście.
#Użyteczne wyrażenia: print(), max(), min(), index(), sum(), count(), set().