#Zaimplementować wzór na obliczenie n-tego wyrazu ciągu Fibonacciego (wzór poniżej) na dwa
#sposoby: iteracyjnie i rekurencyjnie. W komentarzach proszę podać która implementacja jest
#lepsza i dlaczego. Która implementacja jest bardziej czytelna? W celach badawczych można
#również spróbować zmierzyć czas wykonania obu funkcji dla dużych wartości n.

def fib_re(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
