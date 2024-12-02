#Uzupełnij brakujące elementy - Wypełnij ____ poniżej, aby uzyskać prawidłowe wartości zmiennych
#small_cased, stripped i stripped_lower_case, przydatne: .lower(), .strip()

original = " Python strings are COOL! "

lower_cased = original.lower()
stripped = original.strip()
stripped_lower_cased = original.lower().strip()

assert lower_cased == " python strings are cool! "
assert stripped == "Python strings are COOL!"
assert stripped_lower_cased == "python strings are cool!"

#Prettify - zmodyfikuj podane ciągi wyrazów, aby wyglądały lepiej i zarazem zgadzały się
#z oczekiwanym wynikiem, przydatne: .title(), .strip()

ugly = " tiTle of MY new Book\n\n"
# Twoja implementacja:
pretty = ugly.title().strip()
assert pretty == "Title Of My New Book"

#Sformatuj ciąg znaków w oparciu o istniejące zmienne, przydatne: f""

verb = "is"
language = "Python"
punctuation = "!"
# Twoja implementacja
sentence = f"Learning {language} {verb} fun{punctuation}"

assert sentence == "Learning Python is fun!"

#Tworzenie formuł
#Napisz następującą formułę matematyczną w Pythonie: result = 6a^3 − (8b^2/4c) + 11

a = 2
b = 3
c = 2
# Twoja implementacja:
result = (6*a**b)-((8*b**a)/(4*c))+11
# Sprawdźmy czy otrzymaliśmy poprawny wynik
assert result == 50

#Pobieranie danych od użytkownika - wykonaj obliczenia na wprowadzonej przez użytkownika
#liczbie, dla przedstawionego przykładu zakładamy że użytkownik zawsze wprowadza liczbę 20, przydatne: input(), int()

x =input("podaj liczbę")
result = int(x) / 2 + 4
# Sprawdźmy czy otrzymaliśmy poprawny wynik
assert result == 14
