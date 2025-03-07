#2.1 Zwierzęta
#Utwórz klasę Animal, która będzie posiadała pola name, age, species oraz weight. Klasa ta powinna posiadać
#również następujące trzy metody:
#1. Metodę statyczną o nazwie oldest_animal, która będzie przyjmować listę obiektów klasy Animal i zwróci
#nazwę i wiek najstarszego zwierzęcia na liście.
#2. Metodę instancji o nazwie is_endangered, która będzie zwracać wartość True lub False, w zależności od tego,
#czy gatunek zwierzęcia jest zagrożony wyginięciem (przyjmijmy, że tylko gatunek "tiger" jest zagrożony wyginięciem).
#3. Metodę instancji o nazwie calculate_bmi, która będzie zwracać wartość współczynnika BMI (Body Mass Index) dla
#danego zwierzęcia na podstawie jego masy ciała i wzrostu. Przyjmij, że wzrost zwierzęcia to 1 metr, a BMI obliczamy
#ze wzoru: waga / (wzrostˆ2).

class Animal:
    def __init__(self, name, age, species, weight):
        pass

    @staticmethod
    def oldest_animal(zwierze):
        pass

lion = Animal("Simba", 5, "lion", 200)
tiger = Animal("Shere Khan", 8, "tiger", 150)
elephant = Animal("Dumbo", 3, "elephant", 400)
animals = [lion, tiger, elephant]

print(Animal.oldest_animal(animals))
#Shere Khan is the oldest animal at 8 years old
print(lion.is_endangered())
#False
print(tiger.is_endangered())
#True
print(lion.calculate_bmi())
#200.0
print(tiger.calculate_bmi())
#150.0