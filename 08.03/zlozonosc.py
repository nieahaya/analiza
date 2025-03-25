#Zaimplementować algorytm wyszukiwania liniowego w liście (nie ma założenia że lista zawiera
#wartości posortowane). Przetestować działanie tego algorytmu i oszacować jego złożoność obliczeniową.
#Krótko (1-2 zdania) opisać dlaczego ten algorytm ma taką złożoność obliczeniową.

lista1 = [1,5,4,7]


def linear_search(lst, target):
    for i, val in enumerate(lst):
        if val == target and type(val) == type(target):
            return i
    return -1

print(linear_search(lista1, 4))

# Złożoność obliczeniowa:
# - Czasowa: O(n)
# - Pamięciowa: O(1)


#Zaimplementować iteracyjny algorytm wyszukiwania binarnego (binary search). Przetestować
#jego działanie i oszacować złożoność obliczeniową tego algorytmu. Krótko (1-2 zdania) opisać
#dlaczego ten algorytm ma taką złożoność obliczeniową

def binary_search(lst, target):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        print(low, mid, high)
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    print(low, mid, high)
    return -1

lst = [1, 2, 3, 4, 6]
print(binary_search(lst, 5))

# Złożoność obliczeniowa:
# - Czasowa: O(log n)
# - Pamięciowa: O(1)


#Zaimplementować algorytm który sprawdzi czy w dwóch zadanych listach o różnych długościach
#występuje taka sama liczba. Poniżej jest podany przykład działania takiego algorytmu. Następnie
#należy oszacować złożoność obliczeniową tego algorytmu i krótko (1-2 zdania) opisać dlaczego
#ten algorytm ma taką złożoność obliczeniową.
#Przykład:

def check(a, b):
    for elem_a in a:
        for elem_b in b:
            if elem_a == elem_b:
                return True
        # if elem_a in b:
        #     return True
    return False
    # Złożoność obliczeniowa Czasowa: O(n^2); Pamięciowa: O(1)

def fast_check(a, b):
    set1 = set(a)
    for elem_b in b:
        if elem_b in set1:
            return True
    return False
    # Złożoność obliczeniowa Czasowa: O(n + m); Pamięciowa: O(n)

a = [1, 2, 3]
b = [4, 5]
print(fast_check(a, b))


#Zaimplementować algorytm sortowania bąbelkowego (bubble sort). Przetestować jego działanie
#i oszacować złożoność obliczeniową tego algorytmu. Krótko (1-2 zdania) opisać dlaczego ten
#algorytm ma taką złożoność obliczeniową.

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

lst = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(lst)
print(lst)

# Złożoność obliczeniowa
# - Czasowa: O(n^2)
# - Pamięciowa: O(1)


#Zaimplementować wyszukiwanie największej liczby w nieposortowanej liście liczb. Przetestować
#działanie i oszacować złożoność obliczeniową tego algorytmu. Krótko (1-2 zdania) opisać dlaczego
#ten algorytm ma taką złożoność obliczeniową

def find_max(lst):
    if not len(lst):
        return None
    
    max_val = lst[0]
    for val in lst[1:]:
        if val > max_val:
            max_val = val

    return max_val

# Złożoność czasowa O(n)
# Złożoność pamięciowa O(1)


#Zaimplementować algorytm sortowania przez wstawianie (insertion sort). Przetestować jego działanie
#i oszacować złożoność obliczeniową tego algorytmu. Krótko (1-2 zdania) opisać dlaczego ten algorytm
#ma taką złożoność obliczeniową


def insertion_sort(lst):
    for i in range(1, len(lst)):
        value = lst[i]
        j = i - 1
        while j >= 0 and value < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = value

lst = [4, 3, 2, 10, 12, 1, 5, 6]
insertion_sort(lst)
print(lst)

# Złożoność czasowa: O(n^2)


#Zaimplementować opisany poniżej algorytm i oszacować jego złożoność obliczeniową. Krótko (1-2
#zdania) opisać dlaczego ten algorytm ma taką złożoność obliczeniową.

#Algorytm: na wejściu funkcja dostaje dwa ciągi znaków o różnych długościach s1 i s2. Algorytm ma
#zliczyć ile razy w ciągu s1 występują znaki zawierające się w ciągu s2. W poniższym przykładzie
#zliczamy ile samogłosek występuje w zadanym ciągu.

def count_chars(s1, s2):
    count = 0
    
    s2_set = set(s2)
    for char in s1:
        if char in s2_set:
            count += 1

    return count

s1 = 'ala ma kota'
s2 = 'aeiouy'
wynik = count_chars(s1, s2)
print(wynik)

# Złożoność czasowa: bez zastosowania set O(n^2) -> z zastosowaniem set O(n + m)
# Złożoność pamięciowa: bez zastosowania set O(1) -> z zastosowaniem set O(m)


#Zaimplementować algorytm obliczający sumę cyfr wprowadzanej przez użytkownika liczby. Przykładowo,
#dla liczby 1234 wynik działania algorytmu ma wynosić 1 + 2 + 3 + 4 = 10. Oszacować złożoność
#obliczeniową tego algorytmu oraz krótko (1-2 zdania) opisać dlaczego ten algorytm ma taką złożoność.

#Podpowiedź : Wykonujemy pętle tyle razy ile jest cyfr w liczbie. Jak matematycznie znaleźć liczbę
#cyfr w liczbie?

def fun(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x //= 10

    return sum

x = 1234
fun(x)

# Złożoność czasowa: O(n)
# Złożoność pamięciowa: O(1)