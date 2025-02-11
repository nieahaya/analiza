#Punkt i Prosta

#Utwórz dwie klasy: jedna klasa ma reprezentować punkt na płaszczyźnie i posiadać współrzędne x,y tego punktu
#jak atrybuty i argumenty konstruktora. Druga klasa ma reprezentować prostą i posiada takie atrybuty jak a i b,
#definiujące przebieg prostej o równaniu y = ax + b.

#Dodaj do klasy Punkt metodę, która przyjmuje jako argument obiekt klasy Prosta i zwraca True albo False w
#zależności od tego leży nasz punkt na tej prostej czy nie.

#Dodaj do klasy Prosta metodę która znajdzie miejsce w którym ta prosta przecina oś X albo wypisze informacje
#że taki punkt nie istnieje.

class Pkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def nalezy_do(self, prosta):
        if (prosta.a * self.x + prosta.b) == self.y:
            print("Punkt należy do prostej")
        else:
            print("Punkt nie należy do prostej")


class Prosta:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def miejsce_zerowe(self, ):
        if -self.b/self.a !=0:
            print("Funkcja ma miejsce zerowe")
        else:
            print("Funkcja nie posiada miejsca zerowego")

p = Pkt(3, 6)
pr = Prosta(2, 0)
p.nalezy_do(pr)
pr.miejsce_zerowe()

#Prostokąt
 
#Utwórz klasę reprezentującą prostokąt. Konstruktor tej klasy musi przyjmować dwa obiekty klasy Punkt jako
#argumenty. Dwa punkty definiujące prostokąt muszą leżeć na przekątnej. Należy zaimplementować metodę, która
#obliczy boki prostokąta na podstawie punktów podanych do konstruktora. Klasa ma posiadać metody do obliczenia
#pola i obwodu prostokąta. Klasa ma także posiadać metodę która narysuje zdefiniowany prostokąt za pomocą
#biblioteki matplotlib i zaznaczy punkty którymi został zdefiniowany (patrz Rysunek 1).

import matplotlib.pyplot as plt

class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Prostokat:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.bok1 = abs(a.x - b.x)
        self.bok2 = abs(a.y - b.y)

    def pole(self):
        return self.bok1 * self.bok2

    def obwod(self):
        return 2 * self.bok1 + 2 * self.bok2

    def rysuj(self):
        plt.plot(self.a.x, self.a.y, color='blue', marker='.', markersize=16)        
        plt.plot(self.b.x, self.b.y, color='blue', marker='.', markersize=16)        
        plt.plot([self.a.x, self.a.x, self.b.x, self.b.x, self.a.x], [self.a.y, self.b.y, self.b.y, self.a.y, self.a.y], color='blue')        
        plt.xlim([0, 6])        
        plt.ylim([0, 4])        
        plt.grid(axis='both', linestyle='--', color='grey', alpha=0.7)        
        plt.show()
    

p1 = Punkt(1, 1)
p2 = Punkt(2, 3)
prost = Prostokat(p1, p2)
print(prost.pole())
print(prost.obwod())  
#prost.rysuj()


#Notatka i Notatnik

#Utworzyć klasy Notatka (Note) i Notatnik (Notebook). Klas notatki przechowuje autora, treść i czas stworzenia
#(autor i treść są podawane jako argumenty konstruktora, a czas jest pobierany i zapisywany przy tworzeniu obiektu).
#Konstruktor klasy Notatnik nie przyjmuje żadnych argumentów, lecz tworzy pustą listę do której będą dodawane
#obiekty klasy Notatka. Klasa Notatnika musi posiadać implementacje metod, pozwalających: dodać nową notatkę,
#dodać istniejącą notatkę, sprawdzić ile jest dodanych notatek, wyświetlić wszystkie dodane notatki. Dodatkowo
#musi być obsłużona sytuacja kiedy notatnik jest pusty.

import datetime

class Note:
    def __init__(self, autor, tresc):
        self.autor = autor
        self.tresc = tresc
        self.czas_utworzenia = datetime.datetime.now()

class Notebook:
    def __init__(self):
        self.notatki = []

    def dodaj_nowa(self, autor, tresc):
        notatka = Note(autor, tresc)
        self.notatki.append(notatka)

    def dodaj(self, notatka):
        self.notatki.append(notatka)

    def wyswietl_wszystko(self):
        if self.notatki:
            print("Masz takie notatki")
            for i, notatka in enumerate(self.notatki): 
                print(f'{i + 1}. {notatka.autor}: "{notatka.tresc}" o godzinie {notatka.czas_utworzenia.hour}:{notatka.czas_utworzenia.minute}')
        else:
            print('Brak notatek')

nb = Notebook()
nb.dodaj_nowa("Bartek", "Dokończyć instrukcje")
nb.wyswietl_wszystko()
n1 = Note("Andrii", "Sprawdzić instrukcje")
nb.dodaj(n1)
nb.wyswietl_wszystko()

#Pracownik

#Stwórz klasę "Pracownik" w Pythonie, która będzie posiadać atrybuty "imie", "nazwisko" oraz "stanowisko". Klasa
#powinna zawierać publiczną metodę "przedstaw_sie()", która wyświetli imię i nazwisko pracownika oraz jego stanowisko.
#Dodatkowo, klasa powinna posiadać atrybut chroniony "_id_pracownika", który będzie nadawany automatycznie przy
#tworzeniu nowego obiektu i będzie unikalny dla każdego pracownika.

#Podpowiedź: użyć id(self): https://www.programiz.com/python-programming/methods/built-in/id

#Ostatecznie, klasa powinna mieć prywatne pole "__pensja", które będzie przechowywać informację o wynagrodzeniu
#pracownika oraz prywatną metodę "__zmien_pensje(self, nowa_pensja)", która będzie umożliwiała zmianę
#wynagrodzenia tylko z poziomu klasy.

class Pracownik:
    def __init__(self, imie, nazwisko, stanowisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stanowisko = stanowisko
        self._id_pracownika = id(imie)
        self.__pensja = 0

    def przedstaw_sie(self):
        print(f"Cześć, nazywam się {self.imie} {self.nazwisko} i pracuję na stanowisku {self.stanowisko}.")

    def __zmien_pensje(self, nowa_pensja):
        self.__pensja = nowa_pensja

    def podwyzka(self, pensja):
        self.__zmien_pensje(pensja)

    def get_pensja(self):
        return self.__pensja
        

pracownik1 = Pracownik("Jan", "Kowalski", "Inżynier")
pracownik1.przedstaw_sie()

pracownik2 = Pracownik("Anna", "Nowak", "Specjalista ds. marketingu")
pracownik2.przedstaw_sie()

print(f"ID pracownika 1: {pracownik1._id_pracownika}")
print(f"ID pracownika 2: {pracownik2._id_pracownika}")

pracownik1.podwyzka(1000)
print(f"Wynagrodzenie pracownika 1: {pracownik1.get_pensja()}")



#Player

#Stwórz klasę "Player" w Pythonie, która będzie przechowywać informacje o graczach w grze. Klasa powinna mieć
#pola publiczne "nick" oraz chronione "_health"oraz "_score". Klasa powinna zawierać metody publiczne "attack(enemy)"
#oraz "heal()", które będą umożliwiać odpowiednio atakowanie przeciwnika oraz leczenie siebie. Metoda ataku powinna
#zmniejszać zdrowie przeciwnika, a metoda leczenia zwiększać zdrowie gracza.

#Pole "_health" powinno być prywatne, aby uniemożliwić bezpośrednią zmianę wartości z zewnątrz klasy. Do odczytu
#wartości pola "_health" powinna zostać utworzona metoda prywatna o nazwie "_get_health()", która będzie zwracać
#wartość pola "_health". Do zapisu wartości pola "_health"powinna zostać utworzona metoda prywatna o nazwie "_set_health()",
#która będzie zapisywać wartość pola "_health".

#Aby ułatwić odczyt wartości pola "_health", powinna zostać utworzona właściwość o nazwie "health", dekoratorem @property
#oraz @health.setter. Właściwość ta powinna korzystać z metod prywatnych "_get_health()" oraz "_set_health()".

#Dodatkowo, klasa "Player" powinna mieć pole publiczne "level", które będzie przechowywać poziom gracza. Pole to powinno
#zostać utworzone za pomocą dekoratora @property, w taki sposób, że poziom gracza będzie wyznaczany na podstawie wartości
#pola "_score". Np. jeśli "_score" będzie większe od 100, to poziom gracza będzie równy 2, a jeśli "_score" będzie większe
#od 200, to poziom gracza będzie równy 3, itd.
