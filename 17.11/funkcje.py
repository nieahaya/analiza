#Wypełnij brakujące fragmenty ____ funkcji count_even_numbers
#Można założyć, że argument numbers jest listą liczb całkowitych

def count_even_numbers(numbers):
    count = 0
    for num in numbers:
        if num %2==0:
            count +=1
    return count
# Sprawdźmy czy otrzymaliśmy poprawny wynik
assert count_even_numbers([1, 2, 3, 4, 5, 6]) == 3
assert count_even_numbers([1, 3, 5, 7]) == 0
assert count_even_numbers([-2, 2, -10, 8]) == 4


#Znalezienie poszukiwanych osób - Zaimplementuj funkcję find_wanted_people, która jako argument przyjmuje
#listę nazw (ciągów znaków). Funkcja powinna zwrócić listę nazw, które występują zarówno w WANTED_PEOPLE,
#jak i na liście nazw podanej jako argument funkcji
#Przydatne: .append(), if x in y

WANTED_PEOPLE = ["John Doe", "Clint Eastwood", "Chuck Norris"]
# Twoja implementacja
def find_wanted_people(names):
    result = []
    for name in names:
        if name in WANTED_PEOPLE:
            result.append(name)
    return result

# Sprawdźmy czy otrzymaliśmy poprawny wynik
people_to_check1 = ["Donald Duck", "Clint Eastwood", "John Doe", "Barack Obama"]
wanted1 = find_wanted_people(people_to_check1)
assert len(wanted1) == 2
assert "John Doe" in wanted1
assert "Clint Eastwood" in wanted1
people_to_check2 = ["Donald Duck", "Mickey Mouse", "Zorro", "Superman", "Robin Hood"]
wanted2 = find_wanted_people(people_to_check2)
assert wanted2 == []

#Liczenie średniej długości słów w zdaniu - Utwórz funkcję average_length_of_words,
#która przyjmuje ciąg znaków jako argument i zwraca średnią długość słów w ciągu.
#Można założyć, że pomiędzy każdym słowem występuje pojedyncza spacja i że dane wejściowe
#nie zawierają znaków interpunkcyjnych. Wynik należy zaokrąglić do jednego miejsca po przecinku.
#Przydatne: len(), round(), .split()

# Twoja implementacja
def average_length_of_words(sentence):
    if not sentence:
        return 0
    
    words = sentence.split()
    total_length = sum(len(word) for word in words)
    average_length = total_length/len(words)
    return round(average_length,1)

# Sprawdźmy czy otrzymaliśmy poprawny wynik
assert average_length_of_words("only four lett erwo rdss") == 4
assert average_length_of_words("one two three") == 3.7
assert average_length_of_words("one two three four") == 3.8
assert average_length_of_words("") == 0

