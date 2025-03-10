#Zadanie 1 - kalkulator
#Stwórz klasę Calculator, która będzie miała metodę statyczną add, dodającą dwie liczby

class Calculator:
    @staticmethod
    def add(x,y):
        return x + y

#print(Calculator.add(3, 5))


#Zadanie 2 – manipulacja tekstu
#Stwórz klasę StringUtils, która będzie miała metodę statyczną reverse, odwracającą podany tekst

class StringUtils:
    @staticmethod
    def reverse(text):
        return text[::-1]
    
reversed_text = StringUtils.reverse("Hello, World!")
#print(reversed_text)


#Zadanie 3 – walidacja danych
#Stwórz klasę Validator, która będzie miała metodę statyczną is_valid_email, sprawdzającą, czy
#podany ciąg znaków jest poprawnym adresem e-mail.
#Wyrażenie regularne jakiego można użyć to:
#r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
#Można skorzystać z klasy re oraz funkcji compile i match

import re

class Validator:
    @staticmethod
    def is_valid_email(email):
        pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        return bool(re.match(pattern, email))

is_valid = Validator.is_valid_email(email="example@email.com")
#print(is_valid)  # True


#Zadanie 4 – data i czas
#Stwórz klasę DateUtils, która będzie miała metodę statyczną current_date, zwracającą
#aktualną datę w formacie "YYYY-MM-DD"

from datetime import datetime

class DateUtils:
    @staticmethod
    def current_date():
        return datetime.now().strftime("%Y-%m-%d")
    
#from datetime import date
#print(str(date.today()))

#print(DateUtils.current_date())

#Zadanie 5 – identyfikatory
#Stwórz klasę IDGenerator, która będzie miała metodę statyczną generate_id, generującą
#unikatowy identyfikator na podstawie bieżącego czasu

import uuid

class IDGenerator:
    @staticmethod
    def generate_id():
        return str(uuid.uuid4())

#print(IDGenerator.generate_id())


#Zadanie 6 – obsługa plików
#Stwórz klasę FileManager, która będzie miała metodę statyczną read_file, wczytującą zawartość
#pliku tekstowego i metodę statyczną write_file, zapisującą podany tekst do pliku o określonej nazwie

class FileManager:
    @staticmethod
    def read_file(file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "File not found."
        
    @staticmethod
    def write_file(file_path, text):
        f = open(file_path, "w")
        return f.write(text)
    

FileManager.write_file("output.txt", "Hello, FileWriter!")

file_content = FileManager.read_file("output.txt")
#print(file_content)

#Zadanie 7 – obsługa formatu danych
#Stwórz klasę DataFormatter, która będzie miała metodę statyczną format_json, formatującą
#podany słownik do formatu JSON

import json

class DataFormatter:
    @staticmethod
    def format_json(dict):
        return json.dumps(dict, indent=2)
    
data_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

json_result = DataFormatter.format_json(data_dict)
#print(json_result)

#Zadanie 8 – operacje na kolekcjach
#Stwórz klasę ListProcessor, która będzie miała metodę statyczną filter_even_numbers,
#filtrować parzyste liczby z listy, oraz metodę statyczną calculate_average, obliczającą średnią
#arytmetyczną z listy liczb.

class ListProcessor:

    @staticmethod
    def filter_even_numbers(list):
        for number in list:
            if number %2 != 0:
                list.remove(number)
            #return [num for num in numbers if num % 2 == 0]
        return list

    @staticmethod
    def calculate_average(list):
        if not list:
            return 0
        return sum(list) / len(list)

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_numbers = ListProcessor.filter_even_numbers(number_list)
#print(even_numbers)

average = ListProcessor.calculate_average(number_list)
#print(average)


#Zadanie 9 – operacje na tekście
#Stwórz klasę TextUtils, która będzie miała metodę statyczną count_words, zliczającą ilość
#słów w podanym tekście, oraz metodę statyczną capitalize_first_letter, zamieniającą pierwszą
#literę każdego słowa na wielką

class TextUtils:
    @staticmethod
    def count_words(text):
        return len(text.split())

    @staticmethod
    def capitalize_first_letter(text):
        words = text.split()
        capitalized_words = [word.capitalize() for word in words]
        return ' '.join(capitalized_words)

sample_text = "hello world, how are you?"

word_count = TextUtils.count_words(sample_text)
print(word_count)

capitalized_text = TextUtils.capitalize_first_letter(sample_text)
print(capitalized_text)


from collections import Counter

def count_letters(text):
    text = text.replace(" ", "")  # Usunięcie spacji
    letter_counts = Counter(text)  # Zliczanie liter
    
    for letter, count in sorted(letter_counts.items()):
        print(f"{letter}: {count}")

# Przykładowe użycie
text = "interrogation education"
count_letters(text)