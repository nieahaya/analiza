#Napisz testy korzystając z pytest w celu sprawdzenia poprawności funkcji sprawdzającej siłę
#hasła. Zadanie polega na testowaniu poprawności kategoryzacji haseł jako słabych, średnich lub
#silnych na podstawie długości i typów znaków. Uwzględnij przypadki brzegowe, takie jak puste
#hasła i znaki specjalne.

import pytest

class Haslo:
    @staticmethod
    def check_password_strength(password):
        if len(password) < 8:
            return "Weak"
        elif any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
            return "Strong"
        else:
            return "Medium"

def test_slabe_haslo():
    assert Haslo.check_password_strength("haslo") == "Weak"

def test_silne_haslo():
    assert Haslo.check_password_strength("Hasło123$") == "Strong"

def test_srednie_haslo():
    assert Haslo.check_password_strength("haslomaslo") == "Medium"

def test_puste_haslo():
    assert Haslo.check_password_strength("") == "Weak"




#W tym zadaniu napisz testy korzystając z pytest w celu sprawdzenia poprawności funkcji wykonujących operacje na listach.
#Poniższy kod zawiera funkcje do znajdowania maksymalnych i minimalnych wartości w liście, a także do obliczania średniej
#wartości. Twoim zadaniem jest zapewnienie poprawności tych funkcji poprzez napisanie testów obejmujących różne scenariusze:
#• Przetestuj funkcję find_max, aby sprawdzić, czy poprawnie identyfikuje maksymalną wartość na liście.
#• Przetestuj funkcję find_min, aby sprawdzić, czy poprawnie identyfikuje minimalną wartość na liście.
#• Przetestuj funkcję average, aby sprawdzić, czy poprawnie oblicza średnią wartości na liście.
#• Uwzględnij testy dla przypadków brzegowych, takich jak puste listy, listy zawierające tylko
#jeden element i listy zawierające zarówno liczby dodatnie, jak i ujemne.

class Listy:
    def find_max(lst):
        return max(lst)
    def find_min(lst):
        return min(lst)
    def average(lst):
        return sum(lst) / len(lst) if lst else 0

def test_find_max():
    assert Listy.find_max([2,5,8]) == 8
    with pytest.raises(ValueError):
        Listy.find_max([])
def test_find_min():
    assert Listy.find_min([2,5,8]) == 2
    assert Listy.find_min([-2,-4,4,2]) == -4
def test_average():
    assert Listy.average([2,4,8,10]) == 6
    assert Listy.average([5]) == 5


#W tym zadaniu podana została funkcja calculate_sum(a, b), która oblicza sumę dwóch liczb
#a i b. Twoim zadaniem jest napisanie testów przy użyciu pytest, aby sprawdzić, czy funkcja
#zwraca poprawny wynik i czy typ zwracanej wartości jest zgodny z oczekiwaniami. Napisz testy
#obejmujące następujące scenariusze:
#• Sprawdzenie, czy funkcja zwraca prawidłową sumę dla prawidłowych wartości wejściowych.
#• Sprawdzenie, czy funkcja zwraca liczbę całkowitą, gdy a i b są liczbami całkowitymi.
#• Sprawdzenie, czy funkcja zwraca liczbę zmiennoprzecinkową, gdy a lub b jest liczbą zmiennoprzecinkową.
#• Sprawdzenie, czy funkcja zwraca błąd TypeError, gdy a lub b nie jest typem liczbowym (int lub float).

class Kalkulator:
    def calculate_sum(a, b):
        return a + b
    
def test_liczby_calkowite():
    assert Kalkulator.calculate_sum
    (2,4) == 6

def test_liczby_calkowite_zmiennoprzecinkowe():
    test = 2+4
    assert isinstance(test, int)

def test_liczby_zmiennoprzecinkowe():
    test = 2.4 + 4.4
    assert isinstance(test, float)

def test_blad():
    with pytest.raises(TypeError):
        Kalkulator.calculate_sum(5,"a")


#W tym zadaniu funkcja divide(a, b) próbuje podzielić dwie liczby a i b, ale zawiera obsługę wyjątków,
#aby obsłużyć przypadek, w którym b jest zerem, co spowodowałoby błąd ZeroDivisionError.
#Korzystając z pytest przetestuj czy funkcja zachowuje się poprawnie.

class Dzielenie:
    def divide(a, b):
        try:
            result = a / b
        except ZeroDivisionError:
            return "Cannot divide by zero"
        else:
            return result
        
def test_dzielenie_przez_zero():
    assert Dzielenie.divide(5,0) == "Cannot divide by zero"


#W tym zadaniu funkcja read_file(filename) próbuje odczytać zawartość pliku o podanej
#nazwie, ale zawiera obsługę wyjątków, aby obsłużyć przypadki, w których plik nie istnieje
#(FileNotFoundError) lub wystąpił błąd odczytu pliku (IOError). Korzystając z pytest napisz
#testy sprawdzające działanie funkcji. Do przetestowania IOError najlepiej wykorzystać mockera

import pytest
from unittest.mock import mock_open, patch

class Plik:
    @staticmethod
    def read_file(filename):    
        try:
            with open(filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "File not found"
        except IOError:
                return "Error reading the file"
        
def test_file_not_found():
    # Test, kiedy plik nie istnieje
    result = Plik.read_file("non_existing_file.txt")
    assert result == "File not found"

def test_io_error(mocker):
    # Test, kiedy wystąpi IOError (np. problem z odczytem pliku)
    mocker.patch("builtins.open", side_effect=IOError)
    result = Plik.read_file("some_file.txt")
    assert result == "Error reading the file"

def test_successful_file_read(mocker):
    # Test prawidłowego odczytu pliku
    mock_file = mock_open(read_data="This is the content of the file.")
    mocker.patch("builtins.open", mock_file)
    
    result = Plik.read_file("existing_file.txt")
    assert result == "This is the content of the file."
    mock_file.assert_called_once_with("existing_file.txt", 'r')
