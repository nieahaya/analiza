#Stwórz klasę o nazwie "Samochod", która będzie miała atrybuty takie jak marka, model, rok produkcji oraz prędkość
#maksymalna. Dodaj konstruktor, który będzie przyjmował wartości tych atrybutów, a także destruktor, który będzie
#wyświetlał informację o zniszczeniu obiektu.

#Stwórz klasę o nazwie "Droga", która będzie miała atrybuty takie jak rodzaj oraz maksymalna prędkość. Dodaj
#konstruktor, który będzie przyjmował wartości tych atrybutów.

#Dodatkowo do klasy "Samochod", dodaj metodę o nazwie "jedź", która będzie przyjmowała wartość prędkości
#oraz obiekt klasy "Droga"i wypisywała komunikat o tym, że samochód jedzie z podaną prędkością oraz o ile km/h
#przekracza maksymalną prędkość w zależności od obiektu "Droga".

class Samochod:
  def __init__(self, marka, model, rok_produkcji, predkosc_maksymalna):
    self.marka = marka
    self.model = model
    self.rok_produkcji = rok_produkcji
    self.predkosc_maksymalna = predkosc_maksymalna
 
  def __del__(self):
    print('Obiekt klasy Samochod jest niszczony.')
 
  def jedz(self, predkosc, droga):
    print(f'Samochód marki {self.marka}, model {self.model} z roku {self.rok_produkcji} jedzie z prędkością {predkosc} km/h.')
    if predkosc > droga.predkosc_maksymalna: 
      print(f'Samochód przekracza prędkość o {predkosc - droga.predkosc_maksymalna} km/h na drodze rodzaju {droga.rodzaj}.')
    else:
      print('Samochód nie przekracza dozwolonej prędkości.')
 
class Droga:
  def __init__(self, rodzaj, predkosc_maksymalna):
    self.rodzaj = rodzaj
    self.predkosc_maksymalna = predkosc_maksymalna
 
samochod = Samochod("Ferrari", "250 GTO", 2019, 200)
droga = Droga("Autostrada", 140)
samochod.jedz(180, droga)

#Stwórz klasę o nazwie "KontoBankowe", która będzie miała atrybuty takie jak numer konta, imię właściciela,
#nazwisko właściciela oraz saldo. Dodaj konstruktor, który będzie przyjmował wartości tych atrybutów oraz destruktor,
#który będzie wyświetlał informację o usunięciu obiektu.

#Dodatkowo, dodaj metody o nazwach "wpłata"i "wypłata", które będą dodawać lub odejmować od salda odpowiednią kwotę.
#Metoda "wpłata"powinna przyjmować kwotę wpłaty, a metoda "wypłata"powinna sprawdzać, czy na koncie jest wystarczająca
#ilość środków, aby dokonać wypłaty i wypłacać tylko wtedy, gdy saldo na koncie jest większe niż kwota wypłaty.

class KontoBankowe:
    def __init__(self, numer_konta, imię_właściciela, nazwisko_właściciela, saldo):
      self.numer_konta = numer_konta
      self.imię_właściciela = imię_właściciela
      self.nazwisko_właściciela = nazwisko_właściciela
      self.saldo = saldo

    def __del__(self):
        print(f"Konto o numerze {self.numer_konta} należące do {self.imię_właściciela} {self.nazwisko_właściciela} zostało usunięte.")

    def wpłata(self, kwota):
        self.saldo += kwota
        print(f"Wpłata na konto o numerze {self.numer_konta} została wykonana. Aktualne saldo: {self.saldo}")
    
    def wypłata(self, kwota):
        if self.saldo >=kwota:
            self.saldo-=kwota
            print(f"Wypłata z konta o numerze {self.numer_konta} została wykonana. Aktualne saldo: {self.saldo}")
        else:
            print(f"Brak wystarczających środków na koncie")

moje_konto = KontoBankowe("123456789", "Jan", "Kowalski", 1000.0)
moje_konto.wpłata(500.0)
print(moje_konto.saldo)
moje_konto.wypłata(1500.0)
print(moje_konto.saldo)

#Stwórz klasę "EnergiaOdnawialna", która będzie reprezentować źródło energii odnawialnej. Klasa powinna mieć
#atrybuty nazwa (nazwa źródła), moc (moc w megawatach) oraz lokacja (lokalizacja źródła). Klasa powinna także
#mieć konstruktor, który przyjmuje argumenty nazwa, moc i lokacja i ustawia je jako atrybuty obiektu

class EnergiaOdnawialna:
    def __init__(self, nazwa, moc, lokalizacja):
        self.nazwa = nazwa
        self.moc = moc
        self.lokalizacja = lokalizacja

    def get_info(self):
        print(f"Zródło: {self.nazwa}, Moc: {self.moc}, Lokalizacja: {self.lokalizacja}")

    def __add__(self, other):
        self.nazwa = self.nazwa + ", " + other.nazwa
        self.moc += other.moc
        self.lokalizacja = self.lokalizacja + ", " + other.lokalizacja
        return EnergiaOdnawialna(self.nazwa, self.moc, self.lokalizacja)

    def __str__(self):
        return f'Źródlo: {self.nazwa}, Moc: {self.moc}'
   
    def __eq__(self, other):
        return (self.nazwa == other.nazwa) and (self.moc == other.moc) and (self.lokalizacja == other.lokalizacja)


elektrownia_wiatrowa = EnergiaOdnawialna("Wiatr", 50, "Niemcy")
elektrowania_sloneczna = EnergiaOdnawialna("Slonce", 30, "Polska")
elektrownia_wiatrowa.get_info()
elektrowania_sloneczna.get_info()
elektrowania_hybrydowa = elektrownia_wiatrowa + elektrowania_sloneczna
elektrowania_hybrydowa.get_info()
print(elektrownia_wiatrowa)
print(elektrownia_wiatrowa == elektrowania_sloneczna)


#Napisać klase, reprezentującą ułamek (fraction) w postaci a/b, gdzie a jest licznikiem, b mianownikiem. W wyniku
#ma powstać kod klasy spełniający poniższe warunku oraz kod demonstrujący działanie zaimplementowanej klasy.

#Powstała klasa ma spełniać następujące warunki:

#• Tworzymy obiekt z dwóch liczb (licznik i mianownik). Przy tworzeniu klasy ułamek ma zostać skrócony (można
#użyć metody gcd z modułu math). Przy próbie podania mianowniku 0, wyrzucamy wyjątek ZeroDivisionError.

#• Dwie metody do wypisywania obiektów naszej klasy: __repr__ i __str__. Reprezentacja musi zwracać polecenia 
#którym można utworzyć nasz obiekt, a zamiana na string pokazywać postać ułamkową (patrz przykład).

#• Obiekty klasy muszą wspierać podstawowe operacje arytmetyczne (przeciążenia operatorów): dodawanie,
#odejmowanie, mnożenie, dzielenie, wartość bezwzględna. Przy wykonaniu operacji ma powstać nowy obiekt.
#Wszystkie operacje wykonujemy tylko na obiektach naszej klasy (nie trzeba implementować mnożenia przez
#liczbę i t.d.).

#• Obiekty tej klasy można porównywać (6 operatorów do przeciążenia).

#• Klasa musi mieć zaimplementowane metody rzutowania na inne typy danych (float, int, bool).

#• Klasa musi posiadać implementacje metody __round__, żeby umożliwić zaokrąglanie jednocześnie z rzutowaniem na float.

import math
class Fraction:    
    def __init__(self, a, b):        
        if b == 0:            
            raise ZeroDivisionError('Mianownik nie może być 0')                
            
        # skracanie ułamka
        f_gcd = math.gcd(a, b)
        self.a = int(a / f_gcd)
        self.b = int(b / f_gcd)
        self.value = self.a / self.b


    def __repr__(self):        
        return f'Fraction({self.a}, {self.b})'    
        
    def __str__(self):        
        return f'{self.a // self.b} {self.a % self.b}/{self.b}' if self.value > 1 else  f'{self.a}/{self.b}'    
        
    # operatory arytmetyczne    
    def __add__(self, other):        
        return Fraction(self.a * other.b + other.a * self.b, self.b * other.b)    
        
    def __sub__(self, other):        
        return Fraction(self.a * other.b - other.a * self.b, self.b * other.b)            
        
    def __mul__(self, other):        
        return Fraction(self.a * other.a, self.b * other.b)        
        
    def __truediv__(self, other):        
        return Fraction(self.a * other.b, self.b * other.a)    
                            
    def __abs__(self):        
        return Fraction(abs(self.a), abs(self.b))    
        
    # operatory porównania
    def __eq__(self, other): # ==        
        return self.a == other.a and self.b == other.b    
        
    def __neq__(self, other): # !=        
        return self.a != other.a or self.b != other.b    
                                        
    def __gt__(self, other): # >        
        return self.value > other.value        
                                            
    def __ge__(self, other): # >=        
        return self.value >= other.value    
                                                
    def __lt__(self, other): # <        
        return self.value < other.value        
                                                    
    def __le__(self, other): # <=        
        return self.value <= other.value    
        
    # metody rzutowania   
    def __float__(self):        
        return self.value    
    def __int__(self):        
        return int(self.value)        
    def __bool__(self):        
        return self.value > 0    
        
    # zaokrąglanie    
    def __round__(self, round_val=0):        
        return round(float(self.value), round_val)        
                                                                       
fraction1 = Fraction(3, 6)
print(repr(fraction1))
print(str(fraction1))

fraction2 = Fraction(7, 4)
print(repr(fraction2))
print(str(fraction2))

# operatory arytmetyczne
print('Działania artymetyczne')
print(Fraction(1, 4) + Fraction(2, 4))
print(Fraction(3, 4) - Fraction(2, 4))
print(Fraction(2, 4) * Fraction(2, 4))
print(Fraction(1, 4) / Fraction(2, 4))
print(abs(Fraction(-3, 4)))

# operatory porównania
print('Porówanie')
print(Fraction(1, 4) == Fraction(2, 4))
print(Fraction(3, 4) != Fraction(2, 4))
print(Fraction(2, 4) > Fraction(2, 4))
print(Fraction(1, 4) >= Fraction(2, 4))
print(Fraction(1, 4) < Fraction(2, 4))
print(Fraction(1, 4) <= Fraction(2, 4))

# metody rzutowania
print('Rzutowanie')
print(float(Fraction(1, 2)))
print(int(Fraction(1, 2)))
print(int(Fraction(3, 2)))
print(bool(Fraction(1, 2)))
print(bool(Fraction(0, 2)))
print(round(Fraction(3, 4), 1))