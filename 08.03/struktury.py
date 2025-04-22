#Napisz kod algorytmu który oblicza pierwiastek kwadratowy podanej poprzez użytkownika liczby S za pomocą metody babilońskiej.
#Opis metody: x0 = S/2, xn+1 = 1/2(xn + s/xn)
#W powyższych równaniach x0 to przybliżenie początkowe (przyjmujemy połowę liczby), xn+1 jest kolejnym przybliżeniem wartości
#√S (liczymy w pętli kolejne przybliżenia). Kończymy działanie algorytmu i zwracamy ostatnie przybliżenie jeżeli |xn − xn+1| ≤ 0.1.

def sqrt(S, tolerance=1e-6):
    if S < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    if S == 0:
        return 0
    x = S / 2 # Pierwsze przybliżenie (x0 / xn)
    while True:
        next_x = 0.5 * (x + S / x) # Kolejne przybliżenie (x1 / x(n+1))
        if abs(next_x - x) < tolerance:
            return next_x
        x = next_x

print(sqrt(2))
print(sqrt(16))
print(sqrt(100))


#Napisz funkcję, sprawdzającą czy wszystkie otwarte nawiasy okrągłe w napisie zostały zamknięte prawidłowo.
#Funkcja ma wykorzystywać do tego celu stos.
#Następnie rozszerz tą funkcję tak, by wspierała wszystkie 3 rodzaje nawiasów (okrągłe, kwadratowe i klamrowe).

from collections import deque

def isvalid(napis):
    S = deque()
    for sym in napis:
        if sym == "(":
            S.append(sym)
        elif sym == ")":
            if not S:
                return False
            sym2 = S.pop()
            if sym2 != "(":
                return False
    return not S


print(isvalid('(())'))
#True
print(isvalid('((2 + 5) * (2 + 3)) / 2'))
#True
print(isvalid('(()'))
#False
print(isvalid('))(('))
#False


#Napisz funkcję która obliczy wartość wyrażenia matematycznego zapisanego
#w postfiksowej postaci (odwrotna notacja polska). Do obliczeń należy
#wykorzystać stos

def onp(napis):
    s = deque()
    for sym in napis.split():
        if sym.isnumeric():
            s.append(int(sym))
        else:
            a = s.pop()
            b = s.pop()
            if sym == "+":
                s.append(b + a)
            if sym == "-":
                s.append(b - a)
            if sym == "*":
                s.append(b * a)
            if sym == "/":
                s.append(b / a)
    return s.pop()

print(onp('2 3 + 5 *'))
print(onp('2 7 + 3 / 14 3 - 4 * + 2 /'))



#Napisać funkcje, symulującą działanie placówki „Poczta Polska”. Funkcja
#ta ma otrzymać na wejściu listę krotek, zawierających po kolei imię
#klienta oraz zmienną True/False która oznacza czy klient będzie musiał
#wrócić do okienka po raz drugi (by np. wypełnić potwierdzenie nadania
#i wrócić wysłać list). Na końcu działania funkcja powinna zwrócić listę
#osób wychodzących z poczty w tej kolejności w której one będą wychodzić.
#Funkcja powinna używać kolejki.

#Kolejka powinna być obsługiwana następująco:
#(a) Pobierz osobę na początku kolejki.
#(b) Sprawdź czy osoba musi coś wysłać.
#(c) Jeżeli tak to dopisz na koniec kolejki.
#(d) Jeżeli nie to dopisz do listy osób wychodzących z poczty

def pocztapolska(line):
    kolejka = deque(line)
    leaving_clients = []

    while kolejka:
        name, sending = kolejka.popleft()
        if sending:
            kolejka.append((name, False))
        else:
            leaving_clients.append(name)
    return leaving_clients


line = [
    ('Grażyna', True),
    ('Laura', False),
    ('Bartek', False),
    ('Andrzej', True),
    ('Wiesiek', False)
]

print(pocztapolska(line))


#Zaimplementować rekurencyjną funkcję obliczającą n-ty wyraz ciągu
#Fibonacciego (wzór poniżej). Funkcja ma używać mechanizmu cache w celu
#przyspieszenia obliczeń.

#an = 0, n = 0, an = 1, n = 1, an = an−2 + an−1, n > 1

#Cache należy zaimplementować w postaci globalnie zadeklarowanego słownika
#- w ten sposób każde wywołanie funkcji będzie miało dostęp do tego
#słownika. Następnie, porównaj czas wykonania tej funkcji dla dużych liczb
#n z funkcją rekurencyjną i rekurencyjną implementowanymi w ramach
#poprzednich zajęć - jaka jest różnica?

fiboc_cache = {} #pusty słownik przechowujący już obliczone liczby

def fiboc(n):
    if n in fiboc_cache:
        return fiboc_cache[n]

    if n in (0, 1):
        res = n
    else:
        res = fiboc(n - 2) + fiboc(n - 1)
    fiboc_cache[n] = res #zapisanie wyniku w cache
    return res

f = print([fiboc(i) for i in range(32)])

#Napisz prosty program z interfejsem tekstowym, który będzie imitował
#system logowania do pewnego systemu. Po uruchomieniu program ma
#wyświetlić menu składające się z trzech punktów:
#(a) Utwórz konto
#(b) Zaloguj się
#(c) Zakończ program
#Użytkownik ma wprowadzić literę/cyfrę (zależy od implementacji)
#odpowiadającą opcji w menu. W przypadku wprowadzenie błędnej opcji
#użytkownik ma być o tym poinformowany i ponownie poproszony o dokonanie
#wyboru.

#W przypadku wyboru Utwórz konta program ma poprosić użytkownika o login
#i hasło, a następnie zapisać parę login - hash hasła w słowniku
#reprezentującym bazę danych użytkowników. W przypadku wyboru Zaloguj się
#program powinien poprosić użytkownika najpierw o podanie loginu, a potem
#hasła. Następie program powinien zweryfikować czy użytkownik z takim
#loginem istnieje i czy hash podanego przez niego hasła odpowiada temu
#przechowywanemu w bazie danych. Należy wyświetlić stosowny komunikat
#w zależności od wyniku weryfikacji.

users = {}

while True:
    print("\menu")
    print("\(a) utwórz konto")
    print("\(b) zaloguj się")
    print("\(c) zakończ program")

    operation = input('Wybierz opcję: ')
    
    if operation == 'a':
        print("tworzenie konta")
        nazwa = input("podaj nazwę użytkownika: ")
        hasło = input("podaj hasło: ")
        users[nazwa] = hash(hasło)
    elif operation == 'b':
        nazwa = input("podaj nazwę użytkownika: ")
        hasło = input("podaj hasło: ")
        if nazwa in users and users[nazwa] == hash(hasło):
            print("logowanie powiodło się")
        else:
            print("błędne dane logowania")
    elif operation == 'c':
        break
    else:
        print("Nieznana operacja")
        
print(users)
        








