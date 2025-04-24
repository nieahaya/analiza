#Manipulacja ciągami znaków – Napisz testy dla poniższej funkcji korzystając z unittest, aby
#zweryfikować zachowanie funkcji dla różnych danych wejściowych, w tym pustych i niepustych
#ciągów znaków.

import unittest
import pytest

def concat_strings(str1, str2):
    return str1 + str2

class TestStringMethods(unittest.TestCase):
    def test_concat_strings(self):
        self.assertEqual(concat_strings("Hello", "World"), "HelloWorld")
        self.assertEqual(concat_strings("Hello", ""), "Hello")
        self.assertEqual(concat_strings("", ""), "")

#if __name__ == '__main__':
    #unittest.main()


#Operacje na liście – Napisz testy dla poniższej funkcji korzystając z unittest, aby zweryfikować zachowanie funkcji dla
#różnych scenariuszy, w tym list z dodatnimi liczbami całkowitymi, ujemnymi liczbami całkowitymi i pustymi listami.

def find_max(lst):
    return max(lst)

class TestFindMax(unittest.TestCase):
    def test_liczby_calkowite(self):
        self.assertEqual(find_max([1, 3, 5]), 5)

    def test_liczby_ujemne_calkowite(self):
        self.assertEqual(find_max([-1, -3, -5]), -1)

    def test_pusta_lista(self):
        with self.assertRaises(ValueError):
            find_max([])


#if __name__ == '__main__':
    #unittest.main()

#Operacje na plikach – Napisz testy dla poniższej funkcji korzystając z unittest, aby zweryfikować
#zachowanie funkcji podczas odczytu istniejących plików, nieistniejących plików i pustych plików.

import os

def read_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return file.read()
    else:
        return None

class TestReadFile(unittest.TestCase):

    def setUp(self):
        # Przygotowanie nazw plików
        self.test_file = "test_plik.txt"
        self.empty_file = "pusty_plik.txt"
        self.nonexistent_file = "nieistniejacy_plik.txt"

        # Utworzenie testowego pliku z zawartością
        with open(self.test_file, 'w') as f:
            f.write("To jest zawartość pliku.")

        # Utworzenie pustego pliku
        open(self.empty_file, 'w').close()

    def tearDown(self):
        # Czyszczenie po testach
        for filename in [self.test_file, self.empty_file]:
            if os.path.exists(filename):
                os.remove(filename)

    def test_istniejacy_plik(self):
        content = read_file(self.test_file)
        self.assertEqual(content, "To jest zawartość pliku.")

    def test_pusty_plik(self):
        content = read_file(self.empty_file)
        self.assertEqual(content, "")

    def test_nieistniejacy_plik(self):
        content = read_file(self.nonexistent_file)
        self.assertIsNone(content)


#Operacje matematyczne – Napisz testy dla poniższej funkcji korzystając z unittest weryfikujące
#zachowanie funkcji dla list zawierających liczby całkowite, zmiennoprzecinkowe i puste.

def calculate_average(numbers):
    if numbers:
        return sum(numbers) / len(numbers)
    else:
        return None
    
class TestCalculateAverage(unittest.TestCase):
    def test_liczby_calkowite(self):
        self.assertEqual(calculate_average([2,4,8,12]), 6.5)

    def test_liczby_zmiennoprzecinkowe(self):
        self.assertEqual(calculate_average([1.5,2.5,3.5,4.5]), 3)

    def test_pusta_lista(self):
        self.assertIsNone(calculate_average([]))


#Manipulacja datami – Napisz testy dla poniższej funkcji korzystając z unittest, aby zweryfikować zachowanie funkcji
#dla lat przestępnych, lat nieprzestępnych i przypadków brzegowych, takich jak lata ujemne lub lata z nieprawidłowymi
#typami danych.

import datetime

def is_leap_year(year):
    if year < 0:
        raise ValueError('Nieprawidłowy rok')
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_current_year():
    return datetime.datetime.now().year

class TestIsLeapYear(unittest.TestCase):
    def test_lata_przestepne(self):
        self.assertTrue(is_leap_year(2024))

    def test_lata_nieprzestepne(self):
        self.assertFalse(is_leap_year(2023))

    def test_lata_ujemne(self):
        with self.assertRaises(ValueError):
            is_leap_year(-39)

    def test_zly_typ_danych(self):
        with self.assertRaises(TypeError):
            is_leap_year("abc")

if __name__ == '__main__':
    unittest.main()