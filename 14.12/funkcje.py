#Napisz funkcję oblicz_srednia, która przyjmuje trzy liczby jako argumenty pozycyjne i zwraca ich średnią
#arytmetyczną. Przetestuj funkcję na różnych danych wejściowych.

def oblicz_srednia(a,b,c):
    return((a+b+c)/3)

#a=float(input("Podaj pierwszą liczbę: "))
#b=float(input("Podaj drugą liczbę: "))
#c=float(input("Podaj trzecią liczbę: "))

#print(oblicz_srednia(a,b,c))

#Napisz funkcję zaokraglij_srednia, która przyjmuje cztery argumenty:
#• trzy liczby (obowiązkowe),
#• liczbę miejsc po przecinku (opcjonalną, domyślnie 2).
#Funkcja powinna obliczać średnią z trzech liczb i zwracać jej zaokrąglenie do wskazanej liczby miejsc po
#przecinku. Przetestuj różne warianty wywołań tej funkcji.

def zaokraglij_srednia(d,e,f,g):
    return(round((d+e+f)/3, g))

#d=float(input("Podaj pierwszą liczbę: "))
#e=float(input("Podaj drugą liczbę: "))
#f=float(input("Podaj trzecią liczbę: "))
#g=int(input("Podaj liczbę miejsc po przecinku: "))

#print(zaokraglij_srednia(d,e,f,g))

#Napisz funkcję opis_danych, która przyjmuje dowolną liczbę argumentów nazwanych (kwargs). Funkcja powinna:
#• Dla każdego argumentu wypisać jego nazwę oraz wartość.
#• Zwrócić liczbę przekazanych argumentów.
#Przetestuj funkcję z różnymi zestawami argumentów nazwanych.

def opis_danych(**kwargs):
    for nazwa, wartosc in kwargs.items():
        print(f"Nazwa: {nazwa}, Wartość: {wartosc}")
    return len(kwargs)


print("Test 1:")
liczba_argumentow = opis_danych(imie="Jan", wiek=25, miasto="Warszawa")
print(f"Liczba przekazanych argumentów: {liczba_argumentow}\n")

print("Test 2:")
liczba_argumentow = opis_danych(nazwa="Komputer", cena=3000, gwarancja="2 lata", producent="Lenovo")
print(f"Liczba przekazanych argumentów: {liczba_argumentow}\n")

print("Test 3:")
liczba_argumentow = opis_danych()
print(f"Liczba przekazanych argumentów: {liczba_argumentow}")

#Napisz funkcję analiza_zakresu, która:
#• Przyjmuje listę liczb jako argument.
#• Wewnątrz siebie definiuje dwie funkcje pomocnicze:
#– minimum – zwracającą najmniejszą liczbę z listy.
#– maximum – zwracającą największą liczbę z listy.
#• Zwraca krotkę zawierającą minimum, maksimum oraz różnicę między nimi.
#• Nie korzystaj z funkcji wbudowanych min i max.
#Przetestuj funkcję na różnych listach liczb.

def analiza_zakresu(lista):
    def minimum():
        najmniejsza = lista[0]
        for liczba in lista:
            if liczba < najmniejsza:
                najmniejsza = liczba
        return najmniejsza

    def maximum():
        najwieksza = lista[0]
        for liczba in lista:
            if liczba > najwieksza:
                najwieksza = liczba
        return najwieksza

    min_wartosc = minimum()
    max_wartosc = maximum()
    roznica = max_wartosc - min_wartosc

    return (min_wartosc, max_wartosc, roznica)

print("Test 1:")
wynik = analiza_zakresu([3, 7, 1, 9, 4])
print(f"Minimum: {wynik[0]}, Maximum: {wynik[1]}, Różnica: {wynik[2]}")

print("\nTest 2:")
wynik = analiza_zakresu([-5, -2, -8, 0, -1])
print(f"Minimum: {wynik[0]}, Maximum: {wynik[1]}, Różnica: {wynik[2]}")

print("\nTest 3:")
wynik = analiza_zakresu([10, 10, 10])
print(f"Minimum: {wynik[0]}, Maximum: {wynik[1]}, Różnica: {wynik[2]}")


#Napisz rekurencyjną funkcję oblicz_silnie, która:
#• Przyjmuje liczbę całkowitą n.
#• Zwraca silnię liczby n (n!).
#Silnia n! jest definiowana jako:
#n! = (1 dla n = 0,
#     n · (n − 1)! dla n > 0.
#Przykład jak obliczane są działania 3! i 4!:
#3! = 1 · 2 · 3 = 6
#4! = 1 · 2 · 3 · 4 = 24
#Przetestuj funkcję dla różnych wartości n, w tym n=0 oraz liczb ujemnych (w takich przypadkach funkcja
#powinna zwracać błąd lub komunikat).

def oblicz_silnie(n):
    if n==0:
        return(1)
    else:
        return(n*(oblicz_silnie(n-1)))
    
print(oblicz_silnie(5))

#Napisz funkcję zlicz_slowa, która:
#– Przyjmuje tekst jako argument (typ str).
#– Zwraca liczbę słów w tekście.
#Przetestuj funkcję na kilku różnych tekstach, w tym na pustym ciągu znaków.

def zlicz_slowa(str):
    liczba=str.split()
    return(len(liczba))

#str=str(input("Podaj tekst: "))
#print(zlicz_slowa(str))


#Napisz funkcję grupuj_wedlug_typow, która:
#• Przyjmuje dowolną liczbę argumentów pozycyjnych (*args).
#• Grupuje te argumenty według ich typów.
#• Zwraca wynik w postaci słownika, gdzie kluczami są nazwy typów, a wartościami listy elementów
#danego typu.
#• Obsługuje również typy złożone, takie jak lista, słownik, czy zbiór.
#Przykład działania:
#grupuj_wedlug_typow(1, "tekst", [1, 2], {"klucz": "wartosc"}, {1, 2, 3}, 3.14)
# Zwróci:
# {
# "int": [1],
# "str": ["tekst"],
# "list": [[1, 2]],
# "dict": [{"klucz": "wartosc"}],
# "set": [{1, 2, 3}],
# "float": [3.14]
# }
#Przetestuj funkcję na różnych zestawach danych wejściowych.

def grupuj_wedlug_typow(*args):
    # Tworzymy pusty słownik, który będzie przechowywał elementy według typów
    wynik = {}
    
    for arg in args:
        # Pobieramy nazwę typu argumentu
        typ = type(arg).__name__
        
        # Jeśli typ nie istnieje jeszcze w słowniku, tworzymy nowy klucz z pustą listą
        if typ not in wynik:
            wynik[typ] = []
        
        # Dodajemy argument do odpowiedniej listy w słowniku
        wynik[typ].append(arg)
    
    return wynik

# Przykład działania
print(grupuj_wedlug_typow(1, "tekst", [1, 2], {"klucz": "wartosc"}, {1, 2, 3}, 3.14))



#Napisz dwie funkcje:
#– oblicz_srednia(lista) – która oblicza średnią arytmetyczną elementów listy.
#– oblicz_wariancje(lista) – która wykorzystuje funkcję oblicz_srednia, aby obliczyć wariancję
#elementów listy według wzoru:

#Wariancja = 1/n * sigma n * (xi - średnia)^2

#Następnie napisz funkcję która przyjmie dwie listy, obliczy średnią i wariancję dla obu list wykorzystując
#powyższe funkcje, a następnie wyświetli informację o tym która lista ma większa średnią, a która ma
#mniejszą wariancję. Przetestuj funkcje na różnych danych wejściowych.

lista1=[1,5,9,3]
lista2=[6,7,10,11]

def oblicz_srednia(lista):
    return(sum(lista)/len(lista))

def oblicz_wariancje(lista):
    srednia=oblicz_srednia(lista)
    return sum([(x - srednia) ** 2 for x in lista]) / len(lista)

def porownaj_listy(lista1, lista2):
    srednia1 = oblicz_srednia(lista1)
    srednia2 = oblicz_srednia(lista2)
    wariancja1 = oblicz_wariancje(lista1)
    wariancja2 = oblicz_wariancje(lista2)
    if srednia1 > srednia2:
        print("Lista 1 ma większą średnią.")
    elif srednia1 < srednia2:
        print("Lista 2 ma większą średnią.")
    else:
        print("Obie listy mają taką samą średnią.")
    if wariancja1 < wariancja2:
        print("Lista 1 ma mniejszą wariancję.")
    elif wariancja1 > wariancja2:
        print("Lista 2 ma mniejszą wariancję.")
    else:
        print("Obie listy mają taką samą wariancję.")

lista1 = [1, 2, 3, 4, 5]
lista2 = [2, 4, 6, 8, 10]
porownaj_listy(lista1, lista2)


#Napisz dwie funkcje:
#– generuj_pary(lista) – która generuje wszystkie możliwe pary elementów z listy i zwraca je jako listę krotek.
#– oblicz_roznice(pary) – która dla każdej pary oblicza różnicę między pierwszym a drugim elementem.
#Następnie napisz funkcję, która przyjmie listę, wygeneruje pary liczb, obliczy różnice pomiędzy liczbami
#w parze (wykorzystując powyższe funkcje) i posortuje różnice od najmniejszych do największych
#Wynik powinien być wyświetlony jako liczba1 - liczba2 : różnica (dla każdej pary licz)
#Przetestuj funkcje na różnych danych wejściowych.

def generuj_pary(lista):
    pary = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            pary.append((lista[i], lista[j]))
    return pary

def oblicz_roznice(pary):
    return [(a, b, a - b) for a, b in pary]

def przetworz_liste(lista):
    pary = generuj_pary(lista)
    roznice = oblicz_roznice(pary)
    posortowane = sorted(roznice, key=lambda x: x[2])
    for a, b, roznica in posortowane:
        print(f"{a} - {b}: {roznica}")

lista = [10, 20, 30, 40]
przetworz_liste(lista)
