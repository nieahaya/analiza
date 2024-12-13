#Napisz kod który ocenia studentów według poniższych wartości, a następnie wyświetl czy student
#zdał, czy nie oraz jaką ocenę uzyskał. Na wejściu programu powinna być wartość pobrana od użytkownika.

#punkty=int((input("Podaj liczbę punktów ")))
#if punkty > 89:
#  ocena = 5.0
#elif punkty > 74:
#  ocena = 4.5
#elif punkty > 64:
#  ocena = 4.0
#elif punkty > 59:
#  ocena = 3.5
#elif punkty > 49:
#  ocena = 3.0
#else:
#  ocena = 2.0

#print(f"Liczba punktów: {punkty} Uzyskana ocena: {ocena}")
#if ocena > 3.0:
#    print("Student zaliczył zadanie")

# Przykładowy output
#Liczba punktów: 53
#Uzyskana ocena: 3.5
#Student zaliczył zadanie


#Sprawdź jaka jest pora roku. Pobierz od użytkownika miesiąc, a następnie wyświetl jaka to pora roku.

#miesiac = input("Wprowadź miesiąc: ")

#if miesiac == "grudzień" or miesiac == "styczeń" or miesiac == "luty":
#    pora_roku = "zima"
#elif miesiac == "marzec" or miesiac == "kwiecień" or miesiac == "maj":
#    pora_roku = "wiosna"
#elif miesiac == "czerwiec" or miesiac == "lipiec" or miesiac == "sierpień":
#    pora_roku = "lato"
#elif miesiac == "wrzesień" or miesiac == "październik" or miesiac == "listopad":
#    pora_roku = "jesień"
#else:
#    pora_roku = "nieznana"  # Na wypadek, gdy użytkownik wprowadzi nieprawidłową wartość

#print(f"Pora roku dla miesiąca {miesiac}: {pora_roku}")

# Przykładowy input
#Wprowadź miesiąc: październik
# Przykładowy output
#Pora roku dla miesiąca październik: jesień


#Zainicjalizuj listę zawierającą więcej niż 5 elementów z różnymi typami danych. Następnie wyświetl jej długość
#pierwszy, środkowy oraz ostatni element. Następnie dodaj jeden element na początku oraz na końcu listy oraz
#wyświetl listę przed i po modyfikacji.
#Przydatne: len(), .append(), .insert()


#lista = [1, 2, 3, 4, 5, 6, "jabłko"]
#mid=int(len(lista)/2)
#print(lista[0])
#print(lista[mid])
#print(lista[-1])
#lista.insert(0,0)
#lista.append("gruszka")
#print(lista[0])
#print(lista[mid])
#print(lista[-1])


#Stwórz listę liczb od 1 do 10 włącznie, następnie posortuj ją malejąco. Pierwsze pięć elementów
#przypisz do nowej listy, następnie usuń z nowej listy element środkowy oraz posortuj rosnąco.
#Wyświetl listę po każdej modyfikacji. Dodatkowo sprawdź czy istnieje element o wartości 8, w
#jednej i drugiej liście, wyświetlając stosowny komunikat w przypadku jego istnienia, bądź braku.
#Na końcu usuń obie listy.
#Przydatne: .sort(), sorted(), instrukcje warunkowe, len(), range(), del

#lista=[1,2,3,4,5,6,7,8,9,10]
#print(lista)
#if 8 in lista:
#    print("element 8 istnieje")
#else:
#    print("element 8 nie istnieje")
#lista.reverse()
#print(lista)
#if 8 in lista:
#    print("element 8 istnieje")
#else:
#    print("element 8 nie istnieje")
#nowaLista=lista[0:5]
#print(nowaLista)
#if 8 in nowaLista:
#    print("element 8 istnieje")
#else:
#    print("element 8 nie istnieje")
#mid=int(len(nowaLista)/2)
#nowaLista.pop(mid)
#print(nowaLista)
#if 8 in nowaLista:
#    print("element 8 istnieje")
#else:
#    print("element 8 nie istnieje")
#nowaLista.sort()
#print(nowaLista)
#if 8 in nowaLista:
#    print("element 8 istnieje")
#else:
#    print("element 8 nie istnieje")


#Pobierz od użytkownika trzy wartości, dwie liczbowe oraz trzecią w formie string. Następnie stwórz prosty kalkulator,
#który będzie przyjmował podstawowe operacje arytmetyczne to jest dodawanie, odejmowanie, możenie oraz dzielenie (+, -, *, /).
#Program powinien wyświetlać wynik w poniższej postaci.
#Działanie: 2 + 4
#Wynik: 6
#Przydatne: input(), wykorzystaj: if-elif

#x=float(input("Podaj pierwszą liczbę: "))
#y=float(input("Podaj drugą liczbę: "))
#operator=str(input("Podaj znak arytmetyczny z listy (+, -, *, /): "))

#if operator == '+':
#     wynik = x+y
#elif operator == '-':
#     wynik = x-y
#elif operator == '*':
#     wynik = x*y
#elif operator == '/':
#     wynik = x/y
#else:
#     wynik="Nieznany operator"

#print(f"Działanie: {x} {operator} {y}")
#print(f"Wynik: {wynik}")




#Przerób powyższy program tak, aby zamiast pobierać od użytkownika trzy wartości, pobierać
#całe działanie w jednej linii. Program powinien wyświetlać wynik w poniższej postaci.
#Przydatne: .split()

z= input("Podaj pełne działanie: ")
lis=z.split()
 
x=float(lis[0])
y=float(lis[2])
k=lis[1]
 
 
dzialania = {
    "+": x + y,
    "*": x*y,
    "-": x - y,
    "/": x/y,
}
 
wynik = [value for key, value in dzialania.items() if k in key][0]
print(f"Działanie {z}")
print(f"Wynik {wynik}")