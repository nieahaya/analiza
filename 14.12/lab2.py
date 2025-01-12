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

print(f"Zadanie 3: {zad3(lista)}")


#Utwórz funkcję, która przyjmuje trzy argumenty n, a, b i zwraca listę o długości n, wypełnioną losowymi
#liczbami całkowitymi z zakresu od a do b. Argument n ma mieć wartość domyślną 10, argument a wartość
#domyślną 0 i argument b wartość domyślną 10.
#Użyteczne wyrażenia: def, return, random.randrange().

import random

def zad4(n=10,a=0,b=10):
     lista4 = [random.randrange(a,b) for i in range(n)]
     return(lista4)

print(f"Zadanie 4: {zad4()}")


#Napisz funkcję, która przyjmuję jeden argument n, i wykonuje następujące rzeczy:
#• Utworzy listę liczb losowych z zakresu od 0 do 10 o długości n (można użyć funkcje z poprzedniego zadania).
#• Wypisze na ekran wylosowaną listę.
#• Wypisze na ekran największą liczbę z listy.
#• Wypisze indeks pod którym znajduje się najmniejsza liczba w liście.
#• Wypisze sumę liczb w liście.
#• Wypisze ile razy w liście występuje wartość 5.
#• Wypisze zbiór liczb unikalnych występujących w tej liście.
#Użyteczne wyrażenia: print(), max(), min(), index(), sum(), count(), set().4

import random

def zad5(n=10):
     lista5 = [random.randrange(0,10) for i in range(n)]

     print(f"Wylosowana lista: {lista5}")
     print(f"Największa liczba: {max(lista5)}")
     print(f"Indeks najmniejszej liczby: {lista5.index(min(lista5))}")
     print(f"Suma liczb: {sum(lista5)}")
     print(f"Liczba 5 pojawia się w liście {lista5.count(5)} razy")
     print(f"Zbiór liczb unikalnych: {set(lista5)}")

zad5()



#Napisz funkcję, która przyjmuje dwie listy a i b o dowolnych długościach jako argumenty i zwraca iloczyn
#kartezjański elementów tych dwóch list w postaci listy krotek (list of tuples).
#Listing 4: Przykład działania programu.
#Lista 1: [1, 2, 3]
#Lista 2: ["’"a"’", "’"b"’"]
#Iloczyn kartezja´nski: [(1, "’"a"’"), (1, "’"b"’"), (2, "’"a"’"), (2, "’"b"’"), (3, "’"a"’"), (3, "’"b"’")]
#Użyteczne wyrażenia: for in, def, return, [].
#Zabronione w tym zadaniu wyrażenia: itertools.product()


lista61=[1,2,3]
lista62=["a", "b"]

def iloczyn_kartezjanski(a,b):
    wynik6=[]
    for i in a:
        for j in b:
            wynik6.append((i, j))
    return(wynik6)
    

print(f"Zadanie 6: {iloczyn_kartezjanski(lista61,lista62)}")


#Zaznajom się ze składnią list składanych (list comprehension), następnie napisz program, który utworzy
#używając tej składni trzy listy:
#• Lista składająca się z kwadratów liczb naturalnych od 0 do 10.
#• Lista składająca się z kwadratów liczb naturalnych od 0 do 20 pod warunkiem że kwadrat tej liczby jest nieparzysty.
#• Lista składająca się z na przemian kwadratów i sześcianów liczb naturalnych od 0 do 10. Jeżeli liczba jest parzysta,
#to zapisujemy jej kwadrat, inaczej sześcian. Początek listy: [0, 1, 4, 27, 16, 125....
#Użyteczne wyrażenia: List comprehension.
#Zabronione w tym zadaniu wyrażenia: append(), insert().

def zad7():
    lista71=[x**2 for x in range(0,11)]
    lista72=[x**2 for x in range(0,21) if x**2%2!=0]
    lista73=[x**2 if x%2==0 else x**3 for x in range(11)]

    return(lista71, lista72, lista73)

print(f"Zadanie 7: {zad7()}")



#Napisz program, który wygeneruje listę składającą się z 20 całkowitych liczb losowych od -100 do 100,
#a następnie obliczy sumę liczb dodatnich z tej listy, korzystając się ze składni list składanych (list comprehension).
#Użyteczne wyrażenia: List comprehension, random.randrange().

import random

def zad8():
    lista8=[random.randrange(-100,101) for x in range(20)]
    print(lista8)

    suma8=sum([x for x in lista8 if x>0])
    print(suma8)

zad8()


#Napisz funkcję, która przyjmuje jeden argument który może być liczbą albo listą liczb. Jeżeli jako argument
#została podana liczba, należy zwrócić tą liczbę pomnożoną razy 2. Jeżeli jako argument została podana lista
#należy utworzyć nową listę, która będzie zawierała elementy pierwotnej listy, pomnożone razy 2. Zademonstruj
#działanie tej funkcji dla liczby i listy losowej.
#Użyteczne wyrażenia: List comprehension, random.randrange(), isinstance().

def zad9(a):
    if isinstance(a, int):  
        return a * 2
    elif isinstance(a, list):  
        return [x * 2 for x in a]
    else:
        return "Podany argument musi być liczbą lub listą liczb."
    
liczba = 5
print("Zadanie 9: Liczba:", liczba, "-> Wynik:", zad9(liczba))
lista = [random.randrange(1, 10) for _ in range(5)]
print("Zadanie 9: Lista:", lista, "-> Wynik:", zad9(lista))



#Napisz funkcję, która zamieni znaki podanego jako argument napisu s na liste odpowiadających tym znakom
#kody ascii. Ta lista ma być zwrócona jako wynik działania tej funkcji. Do napisania funkcji użyj składni
#list comprehension.
#Listing 5: Przykładowe wywołanie funkcji.
#>>> s = "’"Ala ma kota"’"
#>>> zamien(s)
#[65, 108, 97, 32, 109, 97, 32, 107, 111, 116, 97]
#Użyteczne wyrażenia: List comprehension, ord().

def zad10(s):
    return[ord(x) for x in s]

s = "Ala ma kota"
print(f"Napis: {s}")
print(f"Kody ASCII: {zad10(s)}")



#Napisz funkcję, która przyjmuje dwa napisy (słowa czy zdania), a następnie w kolejnych wierszach wypisuje:
#• zbiór wszystkich znaków unikatowych występujących w obu napisach,
#• zbiór znaków występujących w obu napisach jednocześnie,
#• zbiór znaków występujących w pierwszym napisie, ale nie występujących w drugim.
#Listing 6: Przykładowe działanie programu.
#Napis 1: "ala ma kota"
#Napis 2: "apple"
#Wynik:
#{"’"p"’", "’"o"’", "’"k"’", "’"l"’", "’"t"’", "’" "’", "’"m"’", "’"a"’", "’"e"’"}
#{"’"a"’", "’"l"’"}
#{"’"o"’", "’"k"’", "’"t"’", "’" "’", "’"m"’"}
#Użyteczne wyrażenia: set(), intersection(), union(), difference().

napis1="ala ma kota"
napis2="apple"

def zad11(c,d):
    zbior1 = set(c)
    zbior2 = set(d)
    print(f"Znaki unikatowe występujące w obu napisach: {zbior1.union(zbior2)}")
    print(f"Znaki występujące w obu znakach jednocześnie: {zbior1.intersection(zbior2)}")
    print(f"Znaki występujące w pierwszym napisie, ale nie występujące w drugim: {zbior1.difference(zbior2)}")

zad11(napis1,napis2)


#Napisz funkcję, która będzie posługiwać się predefiniowanym słownikiem do tłumaczenia słów zawierających
#się w tym słowniku na język polski. Funkcja ma przyjmować napis, będący zbiorem słów w języku angielskim
#(wystarczy około 5 słów) i zwracać napis składający się z przetłumaczonych słów jeżeli słowo zawiera się w
#słowniku i oryginałów słów zawartych w nawiasy kwadratowe jeżeli słowo jest nieznane.
#Listing 7: Słownik i przykładowe działanie programu.
#Słownik: {
#"banana": "banan",
#"cherry": "wiśnia",
#"apple": "jabłko",
#"pear": "grusza",
#"watermelon": "arbuz" }
#Napis: "’"apple banana lemon orange pear"’"
#Wynik: "’"jabłko banan [lemon] [orange] grusza"’"
#Użyteczne wyrażenia: split(), join(), get(), if ... is None.

def zad12(tekst):
    słownik = {
        "banana": "banan",
        "cherry": "wiśnia",
        "apple": "jabłko",
        "pear": "gruszka",
        "watermelon": "arbuz"
    }

    # Tłumaczenie słów w tekście
    przetlumaczone_słowka = []
    for słowo in tekst.split():
        # Sprawdzanie, czy słowo jest w słowniku
        przetlumaczone_słowo = słownik.get(słowo)
        if przetlumaczone_słowo is None:
            przetlumaczone_słowka.append(f"[{słowo}]")
        else:
            przetlumaczone_słowka.append(przetlumaczone_słowo)

    # Łączenie przetłumaczonych słów w jeden napis
    return " ".join(przetlumaczone_słowka)

# Przykładowe wywołanie funkcji
tekst_wejsciowy = "apple banana lemon orange pear"
tekst_przetlumaczony = zad12(tekst_wejsciowy)

print(f"Zadanie 12: Napis wejściowy: '{tekst_wejsciowy}'")
print(f"Napis przetłumaczony: '{tekst_przetlumaczony}'")
