#"Uczę się Pythona, aby móc tworzyć aplikacje. Dużą zaletą Pythona jest to że jest bardzo zbliżony
#do języka angielskiego. Posiada prostą składnię, ale czasami potrafi być skomplikowany przez wysoki
#poziom abstracji. Jednak dobrze jest się nauczyć Pythona, aby dalej rozwijać się w stronę programowania."
#Ile unikalnych słów zostało użytych w zdaniu, a ile słów jest w zdaniu? Wyświetl odpowiedź.
#Przydatne: .split(), set(), .casefold(), .lower()

tekst = "Uczę się Pythona, aby móc tworzyć aplikacje. Dużą zaletą Pythona jest to że jest bardzo zbliżony do języka angielskiego. Posiada prostą składnię, ale czasami potrafi być skomplikowany przez wysoki poziom abstracji. Jednak dobrze jest się nauczyć Pythona, aby dalej rozwijać się w stronę programowania."
zdanienowe = tekst.split()
unikalnasuma=0
wyrazysuma=0
unikalny = set(zdanienowe)
for x in unikalny:
    unikalnasuma+=1

for y in zdanienowe:
    wyrazysuma+=1

print(unikalnasuma)
print(wyrazysuma)


#Dodawanie macierzy.
#Przydatne: for’y można zagnieżdżać, jak również i listy, po zagnieżdżonych listach można
#się poruszać w następujący sposób: macierz[i][j], gdzie i to indeks wiersza, a j kolumny

X = [[12,9,3],
     [4,5,6],
     [7,8,3]]
Y = [[9,8,1],
     [6,7,3],
     [4,5,9]]

result = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

assert result == [[21, 17, 4], [10, 12, 9], [11, 13, 12]]

#Transponowanie macierzy.
X = [[12,9],
     [7 ,3],
     [5 ,6]]

result = [[0, 0, 0],
          [0, 0, 0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        result[j][i]=X[i][j]

assert result == [[12, 7, 5], [9, 3, 6]]


#Sprawdź czy podany wyraz jest palindromem (Palindrom to ciąg znaków, który jest taki sam
#czytany do przodu i do tyłu). Wyświetl stosowny komunikat, a następnie przekształć program
#tak, aby przyjmował wyraz od użytkownika.
#Przydatne: ::-1, reversed(), .lower(), .casefold()

my_str = "aIbohPhoBiA"
normalized_str = my_str.casefold()
if normalized_str == normalized_str[::-1]: #SLICING
    print(f"'{my_str}' jest palindromem.")
else:
    print(f"'{my_str}' nie jest palindromem.")


#Pobierz dwie wartości od użytkownika, pierwsze jest słowem, drugie znakiem, a następnie zlicz
#wystąpienia podanego znaku w zadanym słowie.
#Przydatne: for char in word,

#slowo=str(input("Podaj słowo: "))
#litera=input("Podaj literę: ")
#wystapienie=0
#for x in slowo:
#    if x==litera:
#        wystapienie+=1
#print(wystapienie)


#Sprawdź czy rok jest rokiem przestępnym oraz wyświetl stosowny komunikat (sprawdzić rok 1900).
#Przydatne: instrukcje warunkowe, operator modulo

rok=1900
if rok%4==0:
    print(f"{rok} jest rokiem przestępnym")
else:
    print(f"{rok} nie")


#Pobierz trzy liczby od użytkownika, następnie sprawdź która jest największa i wyświetl stosowny komunikat.
#Przydatne: input(), instrukcje warunkowe

# Przykładowy input
#a = input("Podaj pierwszą liczbę: ")
#b = input("Podaj drugą liczbę: ")
#c = input("Podaj trzecią liczbę: ")

#if a>b and a>c:
#    print(f"Liczba pierwsza jest największa, a jej wartość to {a}")
#elif b>a and b>c:
#    print(f"Liczba druga jest największa, a jej wartość to {b}")
#else:
#    print(f"Liczba trzecia jest największa, a jej wartość to {c}")
# Przykładowy output
#Liczba trzecia jest największa, a jej wartość to: 3


#Sprawdź czy dwa słowa są anagramem (mówi się, że dwa ciągi są anagramami, jeśli możemy
#utworzyć jeden ciąg poprzez ułożenie znaków innego ciągu). Wyświetl stosowny komunikat.
#Przydatne: .lower(), .casefold(), .sort, sorted(), len()

#a=input("Wprowadź pierwsze słowo: ").casefold()
#b=input("wprowadź drugie słowo: ").casefold()

#if len(a) != len(b):
#    print("Wyrazy nie są anagramami")
#else:
#    if sorted(a) == sorted(b):
#        print("Wyrazy są anagramami")



#Pobierz zdanie od użytkownika, a następnie sprawdź liczbę samogłosek w zdaniu i wyświetl je.
#Przydatne: {}, for char in word, if char in vowels

#zdanie=input("Podaj zdanie: ")
#vowels = 'aeiouy'
#liczba = 0

#for char in zdanie:
#    if char in vowels:
#        liczba+=1

#print(liczba)


#Zainicjalizuj poniższy słownik (wartości w słowniku możesz zmienić według uznania). Sprawdź, czy słownik osoby zawiera
#klucz skills, jeśli tak, wypisz środkową umiejętność z listy umiejętności. Sprawdź, czy słownik osoby ma klucz umiejętności,
#jeśli tak, sprawdź, czy osoba ma umiejętność "Python" i wypisz wynik. Jeśli dana osoba ma tylko umiejętności Python i Matlab,
#wyświetl ’Zna uczenie maszynowe’, jeśli dana osoba ma umiejętności Python i R, wyświetl ’Zna statystykę’, jeśli dana osoba
#ma umiejętności C i C++, wyświetl ’Zna tworzenie oprogramowania’, w przeciwnym wypadku wyświetl ’nieznany zestaw umiejętności’
# - dla dokładniejszych wyników można zagnieżdżać więcej warunków. Wyświetl stosowną informację, na temat stanu cywilnego oraz
#w jakim kraju mieszka osoba, wynik możesz przedstawić jako "Imię Nazwisko mieszka w Kraju i jest Stan cywilny.

person={
'first_name': 'Jan',
'last_name': 'Kowalski',
'age': 44,
'country': 'Polska',
'is_married': True,
'skills': ['Python', 'Matlab', 'R', 'C', 'C++'],
'address': {
'street': 'Ulica',
'postalcode': '22-210'
}
}

if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print(f"Środkowa umiejętność: {skills[middle_index]}")
    
    # Sprawdzenie, czy osoba zna 'Python'
    if 'Python' in skills:
        print("Osoba zna umiejętność: Python")
    
    # Sprawdzenie zestawu umiejętności
    if 'Python' in skills and 'Matlab' in skills:
        print("Zna uczenie maszynowe")
    elif 'Python' in skills and 'R' in skills:
        print("Zna statystykę")
    elif 'C' in skills and 'C++' in skills:
        print("Zna tworzenie oprogramowania")
    else:
        print("Nieznany zestaw umiejętności")
else:
    print("Słownik nie zawiera klucza 'skills'")

# Informacje o stanie cywilnym i kraju zamieszkania
first_name = person['first_name']
last_name = person['last_name']
country = person['country']
marital_status = "żonaty/zamężna" if person['is_married'] else "nieżonaty/niezamężna"

print(f"{first_name} {last_name} mieszka w {country} i jest {marital_status}.")






