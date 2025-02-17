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

import matplotlib.pyplot as plt

def simple_plot(a, b):
    plt.plot(a, 'r--', label="Wektor a")
    plt.plot(b, 'b-', label="Wektor b")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc="upper right")
    plt.title("Zadanie 3")
    plt.grid(color="green", linestyle="--", linewidth=1.15, alpha=0.5)
    plt.show()

a = np.array([1, 3, 5, 7, 9])
b = np.array([2, 4, 6, 8, 10])

#simple_plot(a, b)


#Napisz funkcje func_plot(vmin, vmax, step), która wykona wykres funkcji f(x) = x^2 − x ∗ 4 + 8.
#Argument vmin oznacza wartość początkową wektora x, vmax oznacza wartość końcową wektora x, step
#oznacza krok w wektorze x.

def func_plot(vmin, vmax, step):
    x = np.arange(vmin, vmax, step)
    y = x ** 2 - x * 4 + 8
    plt.plot(x, y, 'b-')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Wykres funkcji f(x) = x^2 - 4x + 8')
    plt.grid(True)
    plt.show()

#func_plot(-10, 10, 0.1)


#Napisz funkcję multi_plot(sizes, labels), która w jednym oknie wyświetli dwa wykresy: wykres kołowy dla
#podanych rozmiarów w wektorze sizes oraz podpisów labels, oraz wykres słupkowy dla podanych rozmiarów
#w wektorze sizes oraz podpisów labels. Jako przykładowe dane można wziąć na przykład liczbę mieszkańców
#4-5 polskich miast oraz nazwy tych miast.

def multi_plot(sizes, labels):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

    # Wykres kołowy
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax1.set_title('Wykres kołowy')

    # Wykres słupkowy
    ax2.bar(labels, sizes, color='blue')
    ax2.set_title('Wykres słupkowy')
    ax2.set_ylabel('Liczba mieszkańców')

    plt.show()

sizes = [1790658, 783969, 698410, 619936, 564035]
labels = ['Warszawa', 'Kraków', 'Łódź', 'Wrocław', 'Poznań']

#multi_plot(sizes, labels)


#Napisz funkcję scatter_plot(), która wyświetli wykres punktowy dwóch zestawów danych (po 100 punktów każdy):
#współrzędne x i y punktów w pierwszym zestawie ma być wygenerowane za pomocą funkcji np.random.rand(), a
#współrzędne drugiego zestawu danych mają być wygenerowane za pomocą funkcji np.random.randn(). Pierwszy zestaw
#punktów ma być wizualizowany w kolorze niebieskim, a drugi w kolorze zielonym. Punkty drugiego zestawu danych
#muszą być w postaci gwiazdek (marker). Na wykresie ma być pokazana legenda i siatka.

def scatter_plot():
    x1 = np.random.rand(100)
    y1 = np.random.rand(100)
    x2 = np.random.randn(100)
    y2 = np.random.randn(100)
    plt.scatter(x1, y1, color='blue', label='Dataset 1')
    plt.scatter(x2, y2, color="green", marker="*", label='Dataset 2')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Wykres punktowy dwóch zestawów danych')
    plt.legend()
    plt.grid(True)
    plt.show()

#scatter_plot()


#Napisz funkcję make_3D(x, y), która wyświetli wykres powierzchni 3D funkcji funkcji f(x, y) = sqrt (x^2+y^2).
#Oś x powinna być podpisana x, oś y powinna być podpisana y, oś z powinna być podpisana jako z.

from mpl_toolkits.mplot3d import Axes3D

def make_3D(x,y):

    # Make data.
    X, Y = np.meshgrid(x, y)
    Z = np.sqrt(X ** 2 + Y ** 2)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    plt.show()

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

make_3D(x, y)