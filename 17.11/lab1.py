#Napisz program, który utworzy 3 zmienne: zmienną typu int, zmienną typu float i zmienną typu str.
#Zmienne muszą przechowywać wartości adekwatne do typu. Następnie, należy skonwertować zmienną typu
#float na int i wyświetlić te 3 zmienne za pomocą funkcji print().
#Użyteczne wyrażenia: int(), float(), str(), input(), print().

a = int(1)
b = float(1.5)
c = str("bro")

d = int(b)
print(a,d,c)

#Pobierz od użytkownika dwie liczby całkowite za pomocą funkcji input(). Następnie, wyświetl sumę i różnicę
#tych liczb w osobnych wierszach. Użyteczne wyrażenia: int(), input(), print().

#liczba1 = int(input("Podaj pierwszą liczbę całkowitą: "))
#liczba2 = int(input("Podaj drugą liczbę całkowitą: "))

#print(liczba1+liczba2, "\n",liczba1-liczba2)

#Napisz program, który pobierze od użytkownika liczbę całkowitą. Jeżeli pobrana liczba jest parzysta, należy
#podnieść ją do kwadratu i wyświetlić wynik tej operacji. Jeżeli liczba jest nieparzysta, należy podnieść ją do
#trzeciej potęgi i wyświetlić wynik tej operacji. Użyteczne wyrażenia: int(), **, %, input(), print()

#zadanie3=int(input("Podaj liczbę całkowitą: "))
#if zadanie3%2==0:
#    print(zadanie3**2)
#else:
#    print(zadanie3**3)

#Napisz program, który zapyta użytkownika jak on ma na imię, a następnie wyświetli powitanie "Hello, imie.".
#Użyteczne wyrażenia: f”, input(), print().

#imie = input("Podaj swoje imię: ")
#print(f"Hello, {imie}")

#Napisz program, który pobierze od użytkownika liczbę zmiennoprzecinkową, będącą promieniem kuli,
#a następnie obliczy objętość kuli o takim promieniu. Zakładamy że wprowadzona liczba zawsze będzie większa od zera.
#Wzór na objętość kuli: Vk = 4/3πR^3. Niżej podany też przykład wypisania wartości liczby π w Python.
#Ewentualnie, można zdefiniować zmienną o przybliżonej wartości π = 3.14.
#Użyteczne wyrażenia: m.pi, float(), input(), print().

#import math as m

#promien=float(input("Podaj promień kuli: "))
#objetosc=(4/3)*(m.pi*(promien**3))
#print(objetosc)

#Napisz program, który używając tylko pętli for i range() wypisze na ekran:
#• Liczby naturalne od 0 do 10 (bez 10),
#• Liczby naturalne od 10 do 20 (z 20),
#• Liczby naturalne od 0 do 20 z krokiem 2,
#• Liczby całkowite od 0 do -10 z krokiem -1.
#Użyteczne wyrażenia: for, range(), print()

#for x in range(0,10):
#    print(x)

#for x in range(10,21):
#    print(x)

#for x in range(0,21,2):
#    print(x)

for x in range(0,-11,-1):
    print(x)

#Napisz program który będzie pobierał od użytkownika liczby do momentu wprowadzenia liczby ujemnej, a
#następnie wyświetli wszystkie wprowadzone liczby razem (w jednej linii (w postaci listy)).

#lista = []
#while True:
#    liczby = int(input("Wprowadź liczbę: "))
#    if liczby >= 0:
#        lista.append(liczby)
#    else:
#        break
#print("Wprowadzone liczby:", lista)

