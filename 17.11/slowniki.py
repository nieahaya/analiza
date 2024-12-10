#Zapełnianie słownika - utwórz słownik, korzystając ze wszystkich podanych zmiennych
#Może się przydać formatowanie stringa z wykorzystaniem f"", lub .format()

first_name = "John"
last_name = "Doe"
favorite_hobby = "Python"
sports_hobby = "gym"
age = 82

# Twoja implementacja
my_dict = {"name": f"{first_name} {last_name}", "age": age, "hobbies": [favorite_hobby, sports_hobby]}

# Sprawdźmy czy otrzymaliśmy poprawny wynik
assert my_dict == {"name": "John Doe", "age": 82, "hobbies": ["Python", "gym"]}



#Korzystanie ze słowników i ich łączenie
#Wykorzystaj dict1, dict2 i dict3, aby utworzyć my_dict. Dodatkowo pobierz wartość special_key
#z my_dict do zmiennej special_value. Pamiętaj, że oryginalne słowniki powinny pozostać niezmienione, a klucz specjalny powinien zostać usunięty z my_dict

dict1 = dict(key1="This is not that hard", key2="Python is still cool")
dict2 = {"key1": 123, "special_key": "secret"}
# Można również zainicjalizować słownik przez wykorzystanie listy krotek
dict3 = dict([("key2", 456), ("keyX", "X")])
# Twoja implementacja
my_dict = {"key1": dict2.get("key1"),
           "key2": dict3.get("key2"),
           "keyX": dict3.get("keyX")}
special_value = dict2.get("special_key")
# Sprawdźmy czy otrzymaliśmy poprawny wynik
assert my_dict == {"key1": 123, "key2": 456, "keyX": "X"}
assert special_value == "secret"
# Sprawdźmy czy słowniki początkowe nie zostały zmienione
assert dict1 == {"key1": "This is not that hard", "key2": "Python is still cool"}
assert dict2 == {"key1": 123, "special_key": "secret"}
assert dict3 == {"key2": 456, "keyX": "X"}
