import math

#Napisz program w Pythonie, który przyjmuje od użytkownika imię i nazwisko, a następnie wyświetla je
#w odwrotnej kolejności ze spacją między nimi i powitaniem, przydatne: input(), formatowanie wyświetlania

#imie=input("Podaj imię")
#nazwisko=input("Podaj nazwisko")
#print(f"Cześć {nazwisko} {imie}")


#Napisz program w Pythonie, który przyjmuje nazwę pliku od użytkownika i wypisuje jego rozszerzenie.
#Przydatne: input(), .split()

#plik=input("Wprowadź nazwę pliku ")
#print(f"Rozszerzenie pliku to '{plik.split(".")[1]}'")


#Napisz program, który pobierze trzy wartości od użytkownika, a następnie wyświetli datę wydarzenia w formacie "DD/MM/YYYY"
#Przydatne: input(), formatowanie wyświetlania

#dd=input("podaj dzień ")
#mm=input("podaj miesiąc ")
#yyyy=input("podaj rok ")
#print(f'{dd}/{mm}/{yyyy}')


#Pobierz od użytkownika dwie liczby całkowite, dodaj je do siebie i wyświetl wynik.
#Wynik powinien zostać wyświetlony w postaci "Suma 6 oraz 2 to 8".
#Przydatne: operatory arytmetyczne, formatowanie wyświetlania, input(), print()

#x=int(input("Podaj pierwszą liczbę "))
#y=int(input("Podaj drugą liczbę "))
#suma=x+y
#print(f"Suma {x} oraz {y} to {suma}")


#Pobierz od użytkownika cztery liczby, dwie całkowite i dwie zmiennoprzecinkowe. Dodaj pierwszą
#i trzecią do siebie, odejmij drugą od czwartej, a następnie dodaj do siebie liczby wynikowe z
#poprzednich operacji. Wyświetl poszczególne operacje oraz typy tych zmiennych (pobranych od
#użytkownika oraz przejściowych, tj. tych po każdej z operacji).
#Przydatne: operatory arytmetyczne, formatowanie wyświetlania, input(), print()

#a=int(input("Podaj liczbę całkowitą "))
#b=int(input("Podaj kolejną liczbę całkowitą "))
#c=float(input("Podaj liczbę zmiennoprzecinkową "))
#d=float(input("Podaj liczbę zmiennoprzecinkową "))

#wynik1 = a+c
#wynik2 = d-b
 
#print(f"Wynik operacji 1: {wynik1}")
#print(type(wynik1))
#print(f"Wynik operacji 2: {wynik2}")
#print(type(wynik2))
 
#suma = wynik1 + wynik2
 
#print(f"Suma to: {suma}")
#print(type(suma))

#Pobierz od użytkownika dwie wartości, liczbę oraz stopień pierwiastka, następnie oblicz i wyświetl sformatowany wynik.
#Przydatne: operatory arytmetyczne, formatowanie wyświetlania, input(), print()
#Pierwiastek 2 stopnia z 4 to 2

#a=int((input("Podaj liczbę ")))
#b=int((input("Podaj stopień pierwiastka ")))
#wynik=a**(1/b)
#print(wynik)

#Pobierz od użytkownika trzy boki trójkąta, a następnie oblicz pole trójkąta korzystając ze wzoru
#Herona, który został podany poniżej. Program powinien działać w następujący sposób.
#Przydatne: operatory arytmetyczne, formatowanie wyświetlania

#a=int((input("Wprowadź pierwszy bok: ")))
#b=int((input("Wprowadź drugi bok: ")))
#c=int((input("Wprowadź trzeci bok: ")))

#p=((a+b+c)/2)
#pole=(p*(p-a)*(p-b)*(p-c))**0.5

#print(pole)

#Pobierz od użytkownika odległość w kilometrach, a następnie dokonaj konwersji na mile. Wynik wyświetl w poniszy sposób.

#a=float(input("Wprowadź wartość w kilometrach: "))
#print(a*0.6214)

#Pobierz od użytkownika temperaturę w stopniach Celsjusza, a następnie dokonaj konwersji na Fahrenheita. Wynik wyświetl w poniższy sposób.

b=float(input("Wprowadź temperaturę w stopniach Celsjusza: "))
print((b*9/5)+32)

