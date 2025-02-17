import pandas as pd
import matplotlib.pyplot as plt

#Napisz program, który wczyta zbiór danych. Indeks musi być dopasowany względem pierwszej kolumny z pliku.
#Wyświetl 5 pierwszych i ostatnich rekordów z ramki danych.
#Użyteczne wyrażenia: head(), read_csv().

df = pd.read_csv('pokemon_data.csv', index_col=0)
#print(df.head(5))
#print(df.tail(5)) # lub df.head(-5)


#Na podstawie dostarczonej ramki danych stwórz dwie nowe ramki danych. Pierwsza ramka danych będzie
#zawierała rekordy, w których kolumna Type 2 ma wartość brakującą. Druga ramka danych nie będzie zawierała
#żadnych wartości brakujących. Następnie wyświetl liczbę rekordów w każdej z tych nowych ramek danych.
#Użyteczne wyrażenia: isnull(), dropna().

df_type2_missing = df[df['Type 2'].isnull()]
df_no_missing = df.dropna()
print(f'Liczba rekordów z brakującą wartością w kolumnie "Type 2": {len(df_type2_missing)}')
print(f'Liczba rekordów bez brakujących wartości: {len(df_no_missing)}')


#Na podstawie dostarczonej ramki danych posortuj dane według malejących wartości kolumn związanych ze
#statystkami defensywnymi (tj. HP, Defense, Sp. Def) i według rosnących wartości kolumn ze statystykami
#ofensywnymi (tj. Attack, Sp. Atk, Speed). Stwórz kolumny o nazwach Total def. oraz Total off., które
#będą posiadać sumaryczną wartość kolejno kolumn defensywnych i ofensywnych. Utwórz kolumny Rank def.
#oraz Rank off. posiadające ranking wartości z powstałych kolumn według wartości najwyższych. Wyświetl
#Top 5 rekordów według Rank def. oraz Rank off.
#Użyteczne wyrażenia: sort_values(), rank().

df_sorted = df.sort_values(by=['HP', 'Defense', 'Sp. Def'], ascending=True)

df_sorted['Total def.'] = df_sorted['HP'] + df_sorted['Defense'] + df_sorted['Sp. Def']
df_sorted['Total off.'] = df_sorted['Attack'] + df_sorted['Sp. Atk'] + df_sorted['Speed']

df_sorted['Rank def.'] = df_sorted['Total def.'].rank(ascending=False)
df_sorted['Rank off.'] = df_sorted['Total off.'].rank(ascending=False)

top_def = df_sorted.sort_values(by='Rank def.').head(5)
top_off = df_sorted.sort_values(by='Rank off.').head(5)
#print(top_def[['Name', 'Rank def.', 'Total def.']])
#print(top_off[['Name', 'Rank off.', 'Total off.']])


#Na podstawie dostarczonej ramki danych, utwórz filtr, który wybierze rekordy zawierające w kolumnie Name
#ciągi znaków Mega oraz os. Następnie wyświetl liczbę rekordów spełniających ten warunek. Dla każdego z
#tych rekordów stwórz wykres słupkowy przedstawiający statystyki ofensywne i defensywne. Wykres ma być
#stworzony na jednym obiekcie Figure, a słupki nie powinny nachodzić na siebie.
#Użyteczne wyrażenia: contains(), bar().

