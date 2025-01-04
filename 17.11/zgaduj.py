#Napisz program, który który wygeneruje 4 cyfrowy kod, a następnie poprosi użytkownika o odgadnięcie tego kodu.
#W kolejnych próbach użytkownik podaje 4 cyfrowe kody, a program wyświetla informacje o tym które cyfry z tej
#próby zawierają się w wygenerowanym kodzie, a które są ustawione na dobrych pozycjach (patrz przykład). Jeżeli
#użytkownik zgadnie dobrze wszystkie 4 cyfry, należy wyświetlić informacje o tym i zakończyć działanie programu.
 
import random

losowa = str(random.randrange(1000, 10000))  # Konwersja na string, aby operować na znakach
attempts = 0

while True:
    attempts += 1
    uzytkownik = input("Zgadnij 4-cyfrowy kod: ")
    print(f"Próba {attempts}: {uzytkownik}")

    if len(uzytkownik) != 4 or not uzytkownik.isdigit():
        print("Kod musi składać się z dokładnie 4 cyfr.")
        continue
    if uzytkownik == losowa:
        print("Zgadłeś! Gratulacje!")
        break

    # Porównanie cyfr użytkownika z wygenerowanym kodem
    for i, (cyfra_uzytkownika, cyfra_losowa) in enumerate(zip(uzytkownik, losowa)):
        if cyfra_uzytkownika == cyfra_losowa:
            print(f"{cyfra_uzytkownika} jest na swoim miejscu.")
        elif cyfra_uzytkownika in losowa:
            print(f"{cyfra_uzytkownika} nie jest na swoim miejscu.")