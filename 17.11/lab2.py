#Napisz program który znajdzie pozycje (indeks) i wartość największej liczby w liście. Wartości do listy mogą być wpisane na
#sztywno lub pobierane od użytkownika. Proszę nie używać funkcji wbudowanych, a wykonać program używając operatorów for i if.
#Przykładowy wynik działania programu.
#Lista: [4, 2, 3, 1, 5, 1, 3]
#Największa wartość: 5
#Indeks: 4
#Użyteczne wyrażenia: for, range(), if, elif, else, [], append(), int().
#Zabronione w tym zadaniu wyrażenia: max(), index().


lista = [4, 2, 3, 1, 5, 1, 3]
maksymalna_wartosc = lista[0]
maksymalny_indeks = 0

for i in range(len(lista)):
    if lista[i] > maksymalna_wartosc:
        maksymalna_wartosc = lista[i]
        maksymalny_indeks = i

# Wyświetlenie wyników
print("Lista:", lista)
print("Największa wartość:", maksymalna_wartosc)
print("Indeks:", maksymalny_indeks)



#Napisz program, który sprawdzi czy z trzech podanych przez użytkownika długości odcinków można utworzyć
#trójkąt. Zakładamy że użytkownik będzie wprowadzać tylko liczby dodatnie. Z trzech odcinków można
#utworzyć trójkąt wtedy i tylko wtedy gdy suma każdych dwóch odcinków jest większa trzeciemu odcinkowi.
#Użyteczne wyrażenia: if, elif, else, int(), float().

#bok1 = float(input("Podaj długość pierwszego boku trójkąta: "))
#bok2 = float(input("Podaj długość drugiego boku trójkąta: "))
#bok3 = float(input("Podaj długość trzeciego boku trójkąta: "))

#if bok1+bok2>bok3 and bok1+bok2>bok3 and bok2+bok3>bok1:
#    print(f"Można utworzyć trójkąt o bokach: {bok1}, {bok2}, {bok3}")
#else:
#    print(f"Nie można utworzyć trójkąta o bokach: {bok1}, {bok2}, {bok3}")


#Napisz program, który pobierze od użytkownika dwie pary liczb ((x1, y1), (x2, y2)), będące współrzędnymi
#dwóch punktów na płaszczyźnie. Następnie należy obliczyć i wypisać pole i obwód prostokąta zdefiniowanego
#tymi dwoma punktami. Na Rysunku 2 jest pokazany przykładowy prostokąt, zdefiniowany dwoma punktami.
#Użyteczne wyrażenia: int(), float(), abs(), input(), print().

#x1=float(input("Podaj współrzędną x1: "))
#x2=float(input("Podaj współrzędną x2: "))
#y1=float(input("Podaj współrzędną y1: "))
#y2=float(input("Podaj współrzędną y2: "))

#dlugosc=abs(x2-x1)
#szerokosc=abs(y2-y1)

#pole=dlugosc*szerokosc
#obwod=2*dlugosc+2*szerokosc

#print(f"Pole prostokąta wynosi {pole} a obwód {obwod}")


#Napisz program który pobierze od użytkownika liczbę całkowitą, a następnie obliczy sumę cyfr z których
#składa się ta liczba. Przykładowo, dla liczby 1234 mamy otrzymać wynik 1 + 2 + 3 + 4 = 10.
#Użyteczne wyrażenia: while, //, %

#liczba_calkowita=int(input("Podaj liczbę całkowitą: "))

#suma_cyfr = 0

#while liczba_calkowita != 0:
#    suma_cyfr += abs(liczba_calkowita % 10)  # Pobranie ostatniej cyfry i dodanie do sumy
#    liczba_calkowita //= 10  # Usunięcie ostatniej cyfry z liczby

#print("Suma cyfr wynosi:", suma_cyfr)


#Napisz program, który pobierze od użytkownika napis i w kolejnych linijkach wypisze:
#• długość napisu,
#• trzeci znak napisu,
#• ostatni znak,
#• pierwsze 5 znaków napisu,
#• ostatnie 5 znaków napisu,
#• wszystkie znaki od 3 do 3 od końca znaku (włącznie),
#• znaki o indeksach parzystych,
#• wszystkie znaki napisu w odwrotnej kolejności.
#Zakładamy że zawsze będzie podany napis wystarczającej długości. Do zadania należy użyć notacje slice’sów.
#Użyteczne wyrażenia: len(), print(), [start:stop:step].

#napis=str(input("Podaj napis: "))
#print("Długość napisu:", len(napis))
#print("Trzeci znak napisu:", napis[2])
#print("Ostatni znak napisu:", napis[-1])
#print("Pierwsz 5 znaków napisu:", napis[0:5])
#print("Ostatnie 5 znaków napisu:", napis[-1:-6:-1])
#print("Wszystkie znaki od 3 do 3 od końca włącznie:", napis[2:-2])
#print("Znaki o indeksach parzystych:", napis[::2])
#print("Napis w odwrotnej kolejności:", napis[::-1])



#Napisz program, który odwróci elementy w napisie. Napis może być pobierany przez użytkownika, lub wpisany
#na sztywno. Zadanie należy wykonać bez użycia funkcji reversed i slice’sów, a posługując się pętlą
#i indeksowaniem. Do zamiany napisu na listę i z powrotem należy użyć funkcji list() i join().
#Użyteczne wyrażenia: for, range(), list(), join().
#Zabronione w tym zadaniu wyrażenia: reversed(), [start:stop:step].

# Pobranie napisu od użytkownika (lub wpisanie na sztywno)
napis = "poiuytr"

# Zamiana napisu na listę
lista = list(napis)

# Inicjalizacja pustej listy na odwrócone znaki
odwrocona_lista = []

# Iteracja od końca do początku listy
for i in range(len(lista) - 1, -1, -1):
    odwrocona_lista.append(lista[i])

# Połączenie listy w napis
odwrocony_napis = ''.join(odwrocona_lista)

# Wyświetlenie wyniku
print("Odwrócony napis:", odwrocony_napis)



#Napisz program, który pobierze od użytkownika napis (ewentualnie może być wpisany na sztywno), a następnie
#zamieni litery każdego drugiego słowa na duże litery. Pozostałe słowa mają być napisane małymi literami.
#Zakładamy że zawsze będą wprowadzone minimum 2 słowa, oddzielone spacjami.
#Użyteczne wyrażenia: split(), join(), upper(), lower().

napis14 = input("Podaj napis: ")

# Podział napisu na listę słów
slowa = napis14.split()

# Lista na wynikowe słowa
wynik = []

# Iteracja przez słowa z uwzględnieniem indeksu
for i, slowo in enumerate(slowa): #indeks, wartosc
    if i % 2 == 0:  # Indeksy parzyste (pierwsze, trzecie, itd.) - małe litery
        wynik.append(slowo.lower())
    else:  # Indeksy nieparzyste (drugie, czwarte, itd.) - duże litery
        wynik.append(slowo.upper())

# Połączenie słów w jeden napis
wynikowy_napis = ' '.join(wynik)

# Wyświetlenie wyniku
print("Wynik:", wynikowy_napis)


#Dane są dwie listy, zawierające liczby. Należy napisać program, który przeiteruje po obu listach jednocześnie
#i wyświetli w oddzielnych wierszach elementy z obu list, stojące na tej samej pozycji i ich sumę, formatując
#tak, jak to jest pokazane w przykładzie. Należy użyć funkcji zip() i formatowania napisów.
#Użyteczne wyrażenia: for, zip(), if, else.
#Zabronione w tym zadaniu wyrażenia: range().
