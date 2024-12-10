#if-elif-else - Uzupełnij brakujące elementy ____ w poniższym kodzie tak, aby uzyskać poprawny wynik
#Przydatne: len(), range()

name = "John Doe"
if len(name)>20:
    print(f'Name "{name}" is more than 20 chars long')
    length_description = "long"
elif len(name)>15:
    print(f'Name "{name}" is more than 15 chars long')
    length_description = "semi long"
elif len(name)>10:
    print(f'Name "{name}" is more than 10 chars long')
    length_description = "semi long"
elif len(name) in range(8, 11):
    print(f'Name "{name}" is 8, 9 or 10 chars long')
    length_description = "semi short"
else:
    print(f'Name "{name}" is a short name')
    length_description = "short"
# Sprawdźmy czy otrzymaliśmy poprawny wynik
assert length_description == "semi short"

#Pętla for - Uzupełnij brakujące elementy ____ w poniższym kodzie tak, aby uzyskać poprawny wynik

words = ["PYTHON", "JOHN", "chEEse", "hAm", "DOE", "123"]
upper_case_words = []

for word in words:
    if word.isupper():
        upper_case_words.append(word)
# Sprawdźmy czy otrzymaliśmy poprawny wynik
assert upper_case_words == ["PYTHON", "JOHN", "DOE"]

#Oblicz sumę wartości w słowniku - Oblicz sumę wartości w magic_dict, biorąc pod uwagę tylko wartości numeryczne
#Przydatne: isinstance()

magic_dict = dict(val1=44, val2="secret value", val3=55.0, val4=1)
# Twoja implementacja
sum_of_values = 0
for key in magic_dict.keys():
     if isinstance(magic_dict[key], (int,float)):
         sum_of_values += magic_dict[key]

# Sprawdźmy czy otrzymaliśmy poprawny wynik
assert sum_of_values == 100
