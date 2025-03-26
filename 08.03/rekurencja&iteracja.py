#Zaimplementować wzór na obliczenie n-tego wyrazu ciągu Fibonacciego (wzór poniżej) na dwa
#sposoby: iteracyjnie i rekurencyjnie. W komentarzach proszę podać która implementacja jest
#lepsza i dlaczego. Która implementacja jest bardziej czytelna? W celach badawczych można
#również spróbować zmierzyć czas wykonania obu funkcji dla dużych wartości n.

def fibonacci_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n = 10
print(fibonacci_iterative(n))
print(fibonacci_recursive(n))

# Iteracyjna wersja: Ma złożoność czasową O(n) i przestrzenną O(1). Jest szybsza i bardziej efektywna dla dużych n.
# Rekurencyjna wersja: Ma złożoność czasową O(2^2) i przestrzenną O(n) (ze względu na stos wywołań). Dla dużych n staje się niepraktyczna.
# Czytelność: Rekurencyjna implementacja jest bardziej czytelna, ale mniej wydajna.


#Zaimplementować rekurencyjny algorytm sortowania przez wstawianie (insertion sort).

def insertion_sort_r(lst, n=None):
    if n is None:
        n = len(lst)-1
    if n <= 0:
        return
    insertion_sort_r(lst, n-1)

    value = lst[n]
    j = n - 1
    while j >= 0 and value < lst[j]:
        lst[j + 1] = lst[j]
        j -= 1
    lst[j + 1] = value

lst = [4, 3, 2, 10, 12, 1, 5, 6]
insertion_sort_r(lst)
print(lst)



#Zaimplementować rekurencyjny algorytm sortowania przez scalanie (merge sort). Przetestować
#jego działanie i oszacować złożoność obliczeniową tego algorytmu.

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

lst = [4, 3, 2, 10, 12, 1, 5, 6]
print(merge_sort(lst))


#Zaimplementować rekurencyjny algorytm rozwiązujący problem wieży Hanoi. Algorytm ma wypisywać
#kolejne kroki konieczne do przeniesienia N krążków ze słupka A na słupek C. Przykład działania
#niżej. Jaką złożoność obliczeniową ma ten algorytm (Jaką liczbę kroków musimy wykonać żeby
#przenieść N krążków)? Uzasadnij odpowiedź.

def hanoi(n, source, aux, target):
    if n == 1:
        print(f'Move (1) from {source} to {target}')
        return
    hanoi(n - 1, source, target, aux)
    print(f'Move ({n}) from {source} to {target}')
    hanoi(n - 1, aux, source, target)

hanoi(3, 'A', 'B', 'C')


#Zaimplementować funkcję obliczającą silnię podanej jako argument funkcji liczby n. Funkcja powinna
#używać rekurencji do obliczenia silni. Rekurencyjnie wzór na silnie możemy zdefiniować jako:
#n! = 1 gdy n = 0 albo n * (n-1)!

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(0))
print(factorial(1))
print(factorial(5))
print(factorial(10))


#Zaimplementować funkcję który obliczy i wypisze kolejne elementy sekwencji Collatza (wzór
#poniżej) używając rekurencji. Algorytm ma wystartować od podawanej jako argument funkcji
#liczby cn i działać do momentu aż osiągniemy wartości cn+1 = 1.
#cn+1 = 1/2cn, gdy cn jest parzysta
#cn+1 = 3cn + 1, gdy cn jest nieparzysta

def collatz(c_n):
    print(c_n)
    if c_n == 1:
        return
    if c_n % 2 == 0:
        collatz(c_n // 2)
    else:
        collatz(3 * c_n + 1)

#collatz(5)
#collatz(7)


#Zaimplementuj funkcje obliczającą największy wspólny dzielnik dwóch liczb a i b za pomocą
#rekurencji. Liczby a i b powinny być argumentami funkcji. Rekurencyjny wzór na obliczenia
#NWD można przedstawić następująco:
#NWD(a, b) = a, gdy b = 0
#NWD(a, b) = NW D(b, a mod b)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))
print(gcd(101, 103))


#Zaimplementować rekurencyjny algorytm szybkiego sortowania (quicksort) i przetestować jego
#działanie.

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(quicksort([3, 6, 8, 10, 1, 2, 1]))
print(quicksort([5, 3, 7, 4, 2]))

