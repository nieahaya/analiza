#Napisz program, który wygeneruje listę składającą się z 50 losowych liczb całkowitych z zakresu od 0 do 10,
#a następnie wyświetli 5 najczęściej spotykanych liczb. Do wykonania zadania należy użyć funkcji Counter(),
#z modułu collections.
#Użyteczne wyrażenia: collections.Counter(), most_common(), random.randrange().

#import random
#import collections

#def zad1():
#    lista = [random.randrange(0, 11) for _ in range(50)]
#    print(lista)
#    return collections.Counter(lista).most_common(5)

#print(f"5 najczęściej spotykanych liczb: {zad1()}")


#Zastosuj funkcje z modułu itertools, żeby wypisać na ekran permutacje i kombinacje dwusymbolowe, które
#można złożyć z liter napisu podanego przez użytkownika.
#Napis pobrany od użytkownika: "ABCD"
#Permutacje: AB AC AD BA BC BD CA CB CD DA DB DC
#Kombinacje: AB AC AD BC BD CD
#Użyteczne wyrażenia: itertools.permutations(), itertools.combinations(), input().

#import itertools

#napis2=input("Podaj napis: ")
#permutacje=itertools.permutations(napis2, 2)
#kombinacje=itertools.combinations(napis2, 2)
#print("Permutacje:", " ".join([''.join(p) for p in permutacje]))
#print("Kombinacje:", " ".join([''.join(c) for c in kombinacje]))


#Utwórz strukturę składającą się z list zagnieżdżonych, która będzie reprezentować macierz (w rozumieniu
#matematycznym). Następnie, zaimplementuj funkcję, która będzie wykonywała mnożenie macierzy przez wektor
#pionowy (reprezentowany przez zwykłą listę). W przypadku gdy do funkcji jako drugi argument jest podana
#macierz (lista zagnieżdżona) zamiast listy, należy wyrzucić wyjątek ValueError w którym będą umieszczone
#stosowne informacje. Zademonstruj działanie zaimplementowanej funkcji.

#Listing 2: Przykład definiowania macierzy i przykładowy wynik działania programu.
#Przykładowa macierz:
#a = [
#[1, 2, 3],
#[4, 5, 6],
#[7, 8, 9]
#]
## Przykładowy wektor:
#b = [6, 4, 2]
#Wynik mnożenia macierzy a przez pionowy wektor b:
#[20, 56, 92]

#Użyteczne wyrażenia: def, return, for, range(), ValueError()

def zad3(matrix, vector):
    # Sprawdź, czy `vector` jest jednowymiarową listą
    if any(isinstance(item, list) for item in vector):
        raise ValueError("Drugi argument musi być wektorem (jednowymiarową listą).")

    # Sprawdź, czy liczba kolumn w macierzy pasuje do długości wektora
    if len(matrix[0]) != len(vector):
        raise ValueError("Nieprawidłowe wymiary: liczba kolumn w macierzy musi być równa długości wektora.")

    result = []
    for row in matrix:
        row_result = sum(row[i] * vector[i] for i in range(len(vector)))
        result.append(row_result)

    return result

d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

e = [6, 4, 2]

try:
    result = zad3(d,e)
    print("Zadanie 3: ", result)
except ValueError as e:
    print("Błąd: ", e)


#Wczytaj plik points.txt, który zawiera współrzędne 100 punktów położonych w przestrzeni dwuwymiarowej
#(jeden wiersz - jeden punkt, współrzędne x i y są oddzielone od siebie spacjami). Następnie, wypisz na ekran
#dwa punkty które są położone najbliżej siebie.
#Użyteczne wyrażenia: with, open(), read(), splitlines(), math.dist(), itertools.combinations().

import math

# Funkcja do znajdowania dwóch najbliższych punktów
def zad4(file_path):
    # Wczytaj punkty z pliku
    with open(file_path, "r") as plik:
        punkty = []
        for linia in plik:
            x, y = map(float, linia.split())  # Zamień tekst na liczby
            punkty.append((x, y))  # Dodaj punkt do listy

    # Przygotowanie zmiennych do szukania najbliższych punktów
    najblizsza_odleglosc = float("inf")  # Bardzo duża liczba na start
    najblizsze_punkty = None

    # Sprawdzaj każdą parę punktów
    for i in range(len(punkty)):
        for j in range(i + 1, len(punkty)):
            p1 = punkty[i]
            p2 = punkty[j]
            # Oblicz odległość
            odleglosc = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
            # Jeśli odległość jest mniejsza, zapisz te punkty
            if odleglosc < najblizsza_odleglosc:
                najblizsza_odleglosc = odleglosc
                najblizsze_punkty = (p1, p2)

    return najblizsze_punkty, najblizsza_odleglosc

# Wykonaj program
try:
    punkty, odleglosc = zad4("points.txt")
    print(f"Najbliższe punkty: {punkty[0]} i {punkty[1]}")
    print(f"Odległość między nimi: {odleglosc}")
except FileNotFoundError:
    print("Nie znaleziono pliku 'points.txt'.")
except ValueError:
    print("Błąd: Plik ma niepoprawny format.")


#Napisz funkcję, która służy do rozwiązywania równań kwadratowych przyjmującą trzy argumenty, będące współczynnikami
#równania. Do obliczenia pierwiastka z delty należy użyć funkcji math.sqrt(). Proszę nie używać warunków dla
#sprawdzenia czy delta jest ujemna, a wyjątek wyrzucany przez funkcje math.sqrt() przechwycić poza funkcją.

#Następnie, napisz program który będzie w pętli odpytywać użytkownika o kolejne równania które trzeba rozwiązać
#(użytkownik ma podawać trzy współczynniki w jednym wierszu, lub podawać kolejne współczynniki w kolejnych wierszach,
#dane pobierać do momentu wprowadzenia przez użytkownika pustego wierszu). Znalezione pierwiastki należy wypisać na
#ekran, jeżeli równanie nie ma pierwiastków rzeczywistych, odpowiednio poinformować użytkownika o tym. Proszę również
#pamiętać, że jeżeli funkcja została zaimplementowana zgodnie z wymaganiami będzie ona wyrzucać wyjątek, który należy
#odpowiednio obsłużyć.
#Użyteczne wyrażenia: input(), math.sqrt(), try, expect.

import math

def funkcja_kwadratowa(a, b, c):
    delta = b**2 - 4*a*c
    x1 = (-b - math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)
    return x1, x2

#def zad5():
    while True:
        try:
            input_data = input("Podaj współczynniki a, b, c (lub naciśnij Enter, aby zakończyć): ")
            if not input_data:
                break

            input_data = input_data.replace(',', ' ')
            # Rozdzielanie danych na trzy współczynniki
            a, b, c = map(float, input_data.split())

            try: 
                print(f"Pierwiastki równania to: {funkcja_kwadratowa(a, b, c)}")
            except ValueError:
                print("Brak pierwiastków rzeczywistych")
        except ValueError:
            print("Błąd: Proszę podać trzy liczby oddzielone spacjami lub przecinkami.")

#zad5()



#Zaimplementuj funkcje, która utworzy listę liczb pierwszych do n (n jest argumentem funkcji) korzystając z algorytmu sita
#Eratostenesa. Następnie, napisz program, który wygeneruje za pomocą tej funkcji listę liczb pierwszych do 100 i zapisze ją
#do pliku prime_numbers.txt, zapisując po 5 kolejnych liczb pierwszych w każdym wierszu pliku wynikowego.
#Więcej o sicie Eratostenesa: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes.
#Użyteczne wyrażenia: with, open(), write().


#def zad6(n):
    """Generuje listę liczb pierwszych do n (włącznie) za pomocą algorytmu sita Eratostenesa."""
    primes = [True] * (n + 1)  # Domyślnie zakładamy, że wszystkie liczby są pierwsze
    primes[0] = primes[1] = False  # 0 i 1 nie są liczbami pierwszymi

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    # Zwracamy listę liczb pierwszych
    return [i for i in range(n + 1) if primes[i]]


#n = 100  # Zakres liczb pierwszych do wygenerowania

#with open("prime_numbers.txt", "w") as file:
    for i in range(0, len(zad6(n)), 5):
        file.write(" ".join(map(str, zad6(n)[i:i + 5])) + "\n")

#print(f"Liczby pierwsze do {n} zostały zapisane w pliku prime_numbers.txt.")


#Zaimplementuj funkcje-generator, której zadaniem będzie generowanie kolejnych n liczb ciągu Fibonacciego
#(wzór jest podany niżej). Liczba n jest podawana jako argument funkcji. Funkcja ma używać słowa kluczowego
#yield. Przy implementacji nie używamy rekurencji!

def zad7(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


n = 10
for fib in zad7(n):
    print(fib)



#Wczytaj plik students.csv, który zawiera w kolejnych wierszach dane o studentach w postaci imię, nazwisko,
#numer albumu, ocena, oddzielone przycinkami. Należy wczytać te dane do struktury listy krotek (list of
#tuples), przykładowe wczytane dane są pokazane w poniższym przykładzie. Następnie, należy użyć funkcji
#wbudowanych sorted(), max() z argumentem key i wyświetlić:
#• Dane o studentach posortowane po numerach albumów rosnąco,
#• Dane o studentach posortowane po ocenach malejąco,
#• Dane studenta z najwyższą oceną.

with open('students.csv', 'r') as file:
    lines = file.read().splitlines()
    students = []
    for line in lines:
        name, surname, album_number, grade = line.split(',')
        students.append((name, surname, int(album_number), float(grade)))

sorted_by_album = sorted(students, key=lambda x: x[2])
print("Dane posortowane po numerach albumów rosnąco:")
for student in sorted_by_album:
    print(student)

sorted_by_grade_desc = sorted(students, key=lambda x: x[3], reverse=True)
print("\nDane posortowane po ocenach malejąco:")
for student in sorted_by_grade_desc:
    print(student)
    
highest_grade_student = max(students, key=lambda x: x[3])
print("\nStudent z najwyższą oceną:")
print(highest_grade_student)





    

