#Napisz program, który będzie służył pomocą osobom, które chcą podróżować po Szczecinie tramwajem. Program powinien używać
#algorytmu Breadth First Search do znajdowania najkrótszej ścieżki od przystanku początkowego do przystanku docelowego, oraz
#podawać wynik w postaci listy przystanków do przejechania oraz przesiadek, które należy dokonać. Program także powinien mieć
#funkcję wyświetlania przystanków określonej linii tramwajowej.

#Implementacje należy wykonać przy użyciu dwóch plików, załączonych do zadania na Moodle.

#Plik stops_connections.csv w pierwszej linii zawiera nagłówki, a w kolejnych liniach zawiera połączenia pomiędzy przystankami,
#które należy potraktować jako krawędzie grafu. Na przykład, wiersz ”Antosiewicza,Dubois” oznacza, że można przejechać z przystanku
# Antosiewicza do przystanku Dubois. Przy pliku proszę zwrócić uwagę, że krawędzie nie mają kierunków i są powtórzone dwa razy
#(czyli linie ”Antosiewicza,Dubois” i ”Dubois,Antosiewicza” to ta sama krawędź).

#Plik lines_on_stops.csv w pierwszej linii zawiera nagłówki, a w kolejnych liniach zawiera informacje, które tramwaje zatrzymują
#się na tym czy innym przystanku. Przykładowo, linia ”Kołł ˛ataja,2 3 10 11” informuje nas o tym, że na przystanku Kołłątaja
#zatrzymują się linie 2, 3, 10 oraz 11. Numery linii są oddzielone od nazwy przystanku przecinkiem, a od siebie są oddzielone spacjami.

#Po uruchomieniu program powinien zapytać użytkownika, czy (1) chce uzyskać informacje o linii tramwajowej, czy (2) chce zbudować
#trasę do określonego przystanku.

# • W przypadku (1) program prosi użytkownika o podanie interesującej go linii tramwajowej, a następnie wyświetlamy wiersz po
#wierszu przystanki, na których zatrzymuje się ten tramwaj (kolejność nie gra roli), oraz na koniec liczbę wypisanych przystanków
#(np. Linia 21 zatrzymuje si˛e na 10 przystankach.). W przypadku gdy numer linii nie jest prawidłowy, program powinien wyświetlić
#komunikat, który informuje o tym użytkownika i zakończyć swoje działanie.

# • W przypadku (2) program pyta użytkownika, na którym przystanku on się znajduje, oraz do którego przystanku chce dojechać.
#W przypadku gdy przystanek początkowy lub końcowy nie jest wpisany poprawnie, program informuje użytkownika o tym i prosi o ponowne
#wpisanie nazwy przystanku. Następnie program używa algorytmu Breadth First Search do wyznaczenia najkrótszej ścieżki od przystanku
#początkowego do przystanku końcowego (o ile istnieje). Jeżeli ścieżka istnieje, należy wyświetlić użytkownikowi listę przystanków,
#które powinien przejechać, oraz informacje o tym, jakimi tramwajami. W przypadku, gdy trasę tą można przejechać na kilka sposób
#różnymi tramwajami wystarczy że podamy jeden dowolny sposób. W przypadku braku połączenia, taka informacja też powinna być wyświetlona.

#Po zaimplementowaniu programu, należy uzyskać odpowiedzi na następujące pytania i umieścić odpowiedzi na te pytania na końcu
#przesyłanego pliku z kodem (odpowiedzi proszę ponumerować zgodnie z pytaniami). Jeżeli na jakieś pytanie nie można podać odpowiedzi,
#należy wyjaśnić dlaczego.

# 1. Podaj numer linii oraz liczbę przystanków dla najkrótszej linii tramwajowej w Szczecinie.
# 2. Podaj trasę i przesiadki dla przejazdu: Kołłątaja - Plac Kościuszki.
# 3. Podaj trasę i przesiadki dla przejazdu: Szafera - Turkusowa.
# 4. Podaj trasę i przesiadki dla przejazdu: Unii Lubelskiej - Szczanieckiej.
# 5. Podaj trasę i przesiadki dla przejazdu: Karola Miarki - Antosiewicza.



# • Funkcje do wczytywania plików z danymi: oba pliki najlepiej wczytać do słownika list, gdzie jeden będzie grafem przystanków,
#a drugi słownikiem prechowującym przystanki na których te linie zatrzymują się
# • Funkcja BFS zgodnie z wytycznymi z wykładu, ma przyjmować graf (słownik list), oraz przystanek startowy i końcowy.
# • Funkcje do wyświetlania wszystkich przystanków wybranej linii
# • Funkcje do wyświetlania wyników BFS
# • Funkcje do wyświetlania menu (+ ewentualnie funkcje do obsługi input)
# • Funkcje główną, która łączy wszystkie powyższe (o ile funkcja z menu tego nie robi)


from collections import defaultdict, deque
#defaultdict: słownik, który automatycznie tworzy domyślną wartość
#(np. pustą listę), jeśli klucz jeszcze nie istnieje.
#deque: FIFO
from itertools import pairwise
#pairwise: pozwala iterować po parach elementów np. z listy [1,2,3]
#zrobi [(1,2), (2,3)].

def read_lines():
    with open('lines_on_stop.csv', encoding='utf-8') as f:
        lines = f.read().splitlines()[1:] #pomijanie nagłówka
        lines = [line.strip().split(',') for line in lines]
        #^^^Każda linia zawiera przystanek i numery linii rozdzielone spacjami.
        res = {stop: set(map(int, l.split(' '))) for stop, l in lines}
        #^^^słownik: {przystanek: {linie}}
    return res

def read_graph():
    with open('stops_connections.csv', encoding='utf-8') as f:
        lines = f.read().splitlines()[1:]
        lines = [line.strip().split(',') for line in lines]

    stops = defaultdict(list)
    for s1, s2 in lines:
        stops[s1].append(s2)
        #Każdy wiersz to para przystanków s1,s2

    return stops

def bfs(G, vs, vk): #G: graf, czyli słownik {przystanek: [połączone_przystanki]}.
                    #vs: v_start – przystanek początkowy. vk: v_koniec – przystanek docelowy.
    Q = deque([vs]) # kolejka do przeszukiwania
    visited = set([vs]) # odwiedzone przystanki
    P = {vs: -1} # rodzic danego wierzchołka - do odtworzenia trasy

    while Q:
        v = Q.popleft()
        if v == vk:
            break
        for u in G[v]: #dla każdego sąsiada przystanku v
            if u not in visited:
                visited.add(u) # oznaczamy go jako odwiedzonego
                Q.append(u) # dodajemy do kolejki
                P[u] = v # zapisujemy, że dotarliśmy tam z v
    if v != vk:
        return [] #Jeśli zakończyliśmy przeszukiwanie, ale nie odwiedziliśmy vk, to znaczy, że
                  #nie ma połączenia między przystankami → zwracamy pustą ścieżkę.

    path = [v]
    while P[v] != -1: #Teraz mając końcowy przystanek v (czyli vk), cofamy się przez słownik
                      #rodziców P, aż dojdziemy do vs (tam P[vs] == -1).
        v = P[v]
        path.append(v) #Zbieramy przystanki po drodze.

    return path[::-1] #Ścieżka była budowana od końca do początku, więc odwracamy ją.

def find_lines(path, los): #skrót od lines_on_stops
    lines = []
    for s1, s2 in pairwise(path):
        lines.append(los[s1].intersection(los[s2]))
        #Dla każdej pary przystanków z trasy znajduje wspólne linie tramwajowe.
    return lines #listę zbiorów – każda pozycja to wspólne linie dla jednej pary przystanków.

def dfs_lines(rides, i, lines): #rides: np. [(2, 3)] → jedziemy linią 2 przez 3 przystanki.
    #i: indeks w lines → na którym etapie trasy jesteśmy.
    #lines: wynik z find_lines → lista zbiorów wspólnych linii dla kolejnych przystanków.
    if i == len(lines):
        return rides
    #Jeśli przeanalizowaliśmy wszystkie pary przystanków – zwracamy trasę (czyli listę rides).

    line, count = rides[-1]
    if line in lines[i]:
        return dfs_lines(rides[:-1] + [(line, count + 1)], i + 1, lines)
    #Jeśli bieżąca linia (line) pasuje do następnej pary przystanków (lines[i]), to:
    #Przedłużamy ostatni przejazd o 1 przystanek (count + 1) i przechodzimy dalej (i + 1)

    return max((dfs_lines(rides + [(l, 1)], i + 1, lines)
                for l in lines[i]),
               key=lambda x: x[-1][1])

    #Jeśli linia się nie zgadza, musimy wypróbować wszystkie możliwe linie dla danego fragmentu trasy.
    #Dla każdej tworzymy nową gałąź:
    #Dodajemy nową linię l z licznikiem 1 ([(l, 1)]), bo to początek nowego odcinka.
    #max(..., key=lambda x: x[-1][1]) wybiera opcję, która ma najdłuższy ostatni przejazd
    #– czyli najmniej przesiadek na końcu trasy.


def read_stop_name(G, prompt):
    while (ans := input(prompt)) not in G:
        print('Przytanek nie istnieje! Spróbuj jeszcze raz.')
    return ans

def show_menu():
    print('(1) Znajdź informacje o linii')
    print('(2) Znajdź przejazd między przystankami')
    print('(3) Zakończ program')

    while (ans := input('Wybierz opcje: ')) not in ('1', '2', '3'):
        pass

    print()

    return int(ans)

def line_info(lines_on_stops):
    ans = int(input('Podaj numer linii: '))
    stops = []
    for s, lines in lines_on_stops.items():
        if ans in lines:
            stops.append(s)
    #Iterujemy po każdym przystanku s i sprawdzamy, czy tramwaj ans tam się zatrzymuje.
    #Dodajemy te przystanki do listy stops.

    if not stops:
        print('Nie ma takiej linii.')
        exit(1)

    cur_stop = min(stops,
                   key=lambda s: sum(1 for s1 in G[s] if s1 in stops))
    #G to graf {przystanek: [połączone_przystanki]}.
    #Szukamy takiego przystanku, który ma najmniej połączeń z innymi przystankami tej samej linii
    ordered_stops = [cur_stop]
    while len(stops) != len(ordered_stops):
        for s in G[cur_stop]:
            if s in stops and s not in ordered_stops:
                cur_stop = s
                ordered_stops.append(s)
                continue
    #Tutaj budujemy listę przystanków w kolejności przejazdu:
    #Zaczynamy od początkowego przystanku.
    #Sprawdzamy jego sąsiadów (G[cur_stop]).
    #Jeśli jakiś sąsiad:
    #należy do tej samej linii (s in stops)
    #i nie został jeszcze dodany (not in ordered_stops) → to znaczy, że to następny przystanek na trasie.
    #Powtarzamy aż dodamy wszystkie.

    print(f'Przystanki dla linii {ans}:')
    for s in ordered_stops:
        print(s)
    print(f'\nRazem {len(stops)} przystanków.')

def path_betw_stops(G, lines_on_stops):
    vs = read_stop_name(G, 'Podaj przystanek początkowy: ')
    vk = read_stop_name(G, 'Podaj przystanek docelowy: ')
    print()
    path = bfs(G, vs, vk)
    #Funkcja bfs() przeszukuje graf, żeby znaleźć najkrótszą trasę z vs do vk (w liczbie przystanków).
    if not path:
        print('Nie można wyznaczyć trasy.')
        return

    lines = find_lines(path, lines_on_stops)
    #Dla każdej pary kolejnych przystanków z path, sprawdza jakie linie tramwajowe je łączą.
    rides = min((dfs_lines([(l, 0)], 0, lines) for l in lines[0]),
                key=len)
    #Dla każdej możliwej linii na pierwszym odcinku (lines[0]), próbujemy rekurencyjnie dobrać całą trasę.
    #dfs_lines() próbuje jechać jak najdalej jedną linią, potem przesiąść się tylko jeśli trzeba.
    #min(..., key=len) wybiera ten podział, który ma najmniej przejazdów → czyli najmniej przesiadek.
    idx = 0
    for line, count in rides:
        print(f'Wsiądź do tramwaju nr. {line} na {path[idx]}.')
        print(f'Przejedź {count} przystanków:')
        for nr, i in enumerate(range(idx, idx + count + 1)):
            print(f'    {nr}. {path[i]}')
        idx += count
    #Dla każdego przejazdu:
    #pokazuje, gdzie wsiąść (path[idx])
    #ile przystanków przejechać (count)
    #wypisuje listę przystanków po kolei.
    print(f'Wysiadasz na przystanku {path[-1]}.')
    print(f'Łącznie {len(path)} przystanków.')

if __name__ == '__main__':
    lines_on_stops = read_lines()
    G = read_graph()

    opt = show_menu()
    if opt == 1:
        line_info(lines_on_stops)

    elif opt == 2:
        path_betw_stops(G, lines_on_stops)

    else:
        print('Kończymy...')
        exit(0)