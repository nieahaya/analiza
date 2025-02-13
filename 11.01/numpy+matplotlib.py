#Stwórz wektor (np.array) składający się z pięciu dowolnych wartości liczbowych. Wyświetl utworzony wektor.
#Następnie, zmień liczbę na drugiej pozycji (nie pod indeksem 2, tylko na drugiej pozycji) na -1, a liczbę
#znajdującą się na pozycji czwartej powiększ dwa razy.

import numpy as np

a = np.array([5, 10, 15, 20, 25])
#print(a)

a[1] = -1
a[3] = a[3] * 2

#print(a)


#Stwórz macierz dwuwymiarową o wymiarach 3 na 4 (3 wiersze, 4 kolumny) składającą się z losowych wartości
#za pomocą polecenia np.random.randint. Przedział wartości może być dowolny. Następnie, wyświetl wygenerowaną macierz.

#Wykonaj następujące polecenia:
#• Wyświetl drugi wiersz macierzy (tutaj i dalej to są pozycje, nie indeksy. Chyba że jest powiedziane pod indeksem);
#• Wyświetl drugą kolumnę macierzy;
#• Pomnóż cały pierwszy wiersz razy dwa.
#• Wyświetl kwadratową macierz 2x2 składającą się z wycinku macierzy zawierającego pierwsze 2 elementy pierwszego
#i drugiego wiersza.

b = np.random.randint(1,21, size=(3, 4))
print(b)
print("Drugi wierz macierzy: ", b[1])
print("Druga kolumna macierzy: ", b[:, 1])
mnozenie = b[0] * 2
print("Pierwszy wiersz x2: ", mnozenie)
print("Macierz 2x2: ", b[:2, :2])


#Napisz funkcję simple_plot(a, b), która wyświetli wykres, dwóch podanych wektorów a oraz b. Wektor a będzie
#określony przerywaną linią czerwoną, natomiast wektor b będzie określony ciągłą linią niebieską. Legenda do
#wykresu pojawi się w prawym górnym rogu. Oś x powinna być podpisana x, oś y powinna być podpisana y.
#Dodatkowo należy dodać podpis wykresu oraz siatkę. Siatka powinna być zdefiniowana zieloną linią przerywaną
#z przezroczystością 0.5 i grubością linii 1.15.

#Pomoc: Chodzi o to żeby utworzyć dwa wektory wartości (np.array lub lista z dowolnymi liczbami) i wrzucić
#je do funkcji plt.plot() (każdy osobno do innej).