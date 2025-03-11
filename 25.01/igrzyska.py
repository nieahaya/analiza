import pandas as pd
import numpy as np
import sqlite3

#Lista zadań do wykonania:

#1. Wczytać dane dotyczące zawodników do ramki danych

athletes = pd.read_csv('athlete_events.csv')

#2. Wylistować dostępne kolumny

print(athletes.columns)

#3. Wypisać miejsca, w których organizowane były igrzyska (bez powtórzeń)

print(athletes['City'].unique())

#4. Wypisać miejsca, w których były organizowane letnie igrzyska (bez powtórzeń)

print(athletes[athletes['Season']=='Summer']['City'].unique())

#5. Sprawdzić ile konkurencji było rozgrywanych na letnich igrzyskach w roku 2012

print(len(athletes[athletes['Year']==2012]['Sport'].unique()))

#6. Wypisać wszystkich złotych medalistów z letnich igrzysk w roku 2016

print(athletes[(athletes['Medal']=='Gold')&(athletes['Year']==2016)])

#7. Dla igrzysk z zimowych z roku 1994 sprawdzić w którym sporcie startowało najwięcej osób

print(athletes[athletes['Year']==1994].groupby(by=['Sport']).count().sort_values(by='ID', ascending=False))

#    * Dla najbardziej licznego sportu stworzyć ramkę danych z zawodnikami biorącymi udział w tym sporcie w 1994 roku

athletes_1994 = athletes[(athletes['Year']==1994) & (athletes['Sport'] == 'Cross Country Skiing')]
print(athletes_1994)

#8. Stworzyć ramkę danych zawierających samych medalistów igrzysk olimpijskich
#    * Usunąć wiersze w których wzrost i waga są wartościami nienumerycznymi
#    * Wyznaczyć średni wzrost medalistów
#    * Dodać kolumnę typu bool, w której będzie przechowywana informacja o tym czy wzrost danego medalisty jest większy niż średnia
#    * Dodać kolumnę z wartością różnicy pomiędzy wagą zawodnika a średnią wagą medalistów
#    * Sprawdzić z którego kraju pochodzi największa i najmniejsza ilość medalistów
#    * Zapisać dane do pliku excel 'athletes_medalist.xlsx', gdzie jeden arkusz 'Winter' będzie zawierał medalistów zimowych igrzysk olimpijskich, a 'Summer' medalistów letnich igrzysk olimpijskich
#9. Na wykresie wykreśl przebieg liczności zawodników w zależności od roku organizacji igrzysk
#    * oś X ma przedstawiać rok organizacji igrzysk
#    * oś Y ma pokazywać ilość zawodników
#    * do wykresu dodać siatkę
#   * podpisać osie
#10. Wyświetlić wykres kołowy, który będzie pokazywał rozkłąd ilości startów zanotowanych przez mężczyzn i przez kobiety.
#    * Pogrupować dane po kolumnie 'Sex'
#    * Zliczyć ilość wystąpień
#    * Wyświetlić na wykresie typu 'pie chart'
#    * Dodać czarne obramowanie na wykresie
#    * Ustawić rozmiar czcionki na 16
#    * Wyświetlić na wykresie procentowy rozkład danych w postaci tekstowej 
#11. Napisać skrypt, który wygeneruje plik xlsx, w którym w zależności od podanych parametrów znajdą się odpowiednie dane w osobnych arkuszach
#    * Parametry wejściowe
#        * kraj
#        * płeć
#        * rok igrzysk
#    * Działanie skryptu
#        * Gdy podane są wszystkie parametry, skrypt wyszukuje w tabeli athletes wiersze zgodne z podanymi wartościami, a następnie dane dotyczące każdego z zawodników zapisuje do osobnych arkuszy nazwanych ich imieniem i nazwiskiem (kolumna 'Name')
#        * Wersja zaawansowana: Jeśli któryś z parametrów nie został podany, wtedy uwzględniamy wszystkie dane dla pozostałych filtrów
#            * Przykładowo jeśli nie został podany parametr dla kraju, uwzględniamy zawodników wszystkich narodowości
#    * Nazwa generowanych plików: kraj_płeć_rok.xlsx
#        * Jeśli brak wszystkich parametrów, plik nazywamy 'athletes.xlsx'
