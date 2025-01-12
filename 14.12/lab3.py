#Napisz program, który wygeneruje listę składającą się z 50 losowych liczb całkowitych z zakresu od 0 do 10,
#a następnie wyświetli 5 najczęściej spotykanych liczb. Do wykonania zadania należy użyć funkcji Counter(),
#z modułu collections.
#Użyteczne wyrażenia: collections.Counter(), most_common(), random.randrange().

import random
import collections

def zad1():
    lista = [random.randrange(0, 11) for _ in range(50)]
    print(lista)
    return collections.Counter(lista).most_common(5)

print(f"5 najczęściej spotykanych liczb: {zad1()}")


#Zastosuj funkcje z modułu itertools, żeby wypisać na ekran permutacje i kombinacje dwusymbolowe, które
#można złożyć z liter napisu podanego przez użytkownika.
#Napis pobrany od użytkownika: "ABCD"
#Permutacje: AB AC AD BA BC BD CA CB CD DA DB DC
#Kombinacje: AB AC AD BC BD CD
#Użyteczne wyrażenia: itertools.permutations(), itertools.combinations(), input().

import itertools

napis2=input("Podaj napis: ")
permutacje=itertools.permutations(napis2, 2)
kombinacje=itertools.combinations(napis2, 2)
print("Permutacje:", " ".join([''.join(p) for p in permutacje]))
print("Kombinacje:", " ".join([''.join(c) for c in kombinacje]))


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
## Wynik mnożenia macierzy a przez pionowy wektor b:
#[20, 56, 92]
#Użyteczne wyrażenia: def, return, for, range(), ValueError()