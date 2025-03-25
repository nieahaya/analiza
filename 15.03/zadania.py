#Manipulacja ciągami znaków – Napisz testy dla poniższej funkcji korzystając z unittest, aby
#zweryfikować zachowanie funkcji dla różnych danych wejściowych, w tym pustych i niepustych
#ciągów znaków.

import unittest
import pytest

class TestStringMethods(unittest.TestCase):
    def concat_strings(str1, str2):
        return str1 + str2


