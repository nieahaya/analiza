#https://www.algorytm.edu.pl/matura-informatyka/algorytm/pseudokod

#Napisz pseudokod algorytmu który sprawdzi czy podane poprzez użytkownika 3 liczby mogą być bokami
#trójkąta (Możemy zbudować trójkąt z 3 odcinków jeżeli każde 2 z nich są większe od trzeciego).

#jeżeli a + b > c i b + c > a i a + c > b to
#    wypisz(prawda)


#Narysuj schemat blokowy algorytmu który pobiera od użytkownika liczbę
#i sprawdza czy ta liczba jest parzysta. Napisz pseudokod tego algorytmu.

#jeżeli x mod 2 = 0 to
#   wypisz(prawda)


#Napisz pseudokod algorytmu obliczający sumę cyfr w podanej przez
#użytkownika liczbie n

#Wejście: liczba całkowita n
#Wyjście: suma cyfr liczby n

#1. Wczytaj n
#2. Ustaw suma ← 0
#3. Dopóki n > 0 wykonuj:
#    a. cyfra ← n mod 10
#    b. suma ← suma + cyfra
#    c. n ← n div 10
#4. Wypisz suma


#Napisz pseudokod który zliczy ile liczb naturalnych jest podzielne
#przez 3 w przedziale od 4 do 29 włącznie

#Algorytm LiczPodzielnePrzez3

#Wejście: brak (przedział jest stały: od 4 do 29)
#Wyjście: liczba liczb podzielnych przez 3 w przedziale

#1. Ustaw licznik ← 0
#2. Dla i od 4 do 29 wykonuj:
#    a. Jeżeli i mod 3 = 0, to:
#        i. licznik ← licznik + 1
#3. Wypisz licznik

#Koniec algorytmu

