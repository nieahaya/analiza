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
        self.name = name
        self.age = age
        self.species = species
        self.weight = weight

    @staticmethod
    def oldest_animal(list):
        if not animals:
            return None
        oldest = max(animals, key=lambda animal: animal.age)
        return oldest.name, oldest.age

    def is_endangered(self):
        return self.species.lower() == "tiger"
    
    def calculate_bmi(self):
        height = 1
        bmi = self.weight / (height * height)
        return bmi
    
    def feed(self, food):
        return f"{self.name} the {self.species} is being fed."
    
    def __repr__(self):
        return f"Animal(name=\"{self.name}\", age={self.age}, species=\"{self.species}\", weight={self.weight})"

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


#Utwórz klasę Farm, która będzie posiadała pole animals - listę, w której będą przechowywane wszystkie zwierzęta
#na farmie. Zwierzęta, które będą dodawane do listy muszę być obiektami klasy Animal. Klasa ta powinna posiadać
#również następujące trzy metody:
#1. Metodę instancji add_animal, która będzie dodawać nowe zwierzę na farmę.
#2. Metodę instancji feed_all, która będzie symulować karmienie wszystkich zwierząt na karmie i zwracać informację
#o tym jakie jedzenie zostało im podane.
#3. Metodę klasową create_farm_with_animals, która będzie tworzyć obiekt klasy Farm i dodawać do niego określoną
#listę zwierząt. Metoda ta powinna przyjmować jeden argument - listę zwierząt, które mają zostać dodane na farmę.

class Farm:

    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
        else:
            raise ValueError("Only objects of class Animal can be added to the farm.")

    def feed_all(self, food):
        print(f"Feeding all animals on farm with {food}:")
        for animal in self.animals:
            print(animal.feed(food))
        print("All animals have been fed.")

    @classmethod
    def create_farm_with_animals(cls, animals):
        farm = cls()
        for animal in animals:
            farm.add_animal(animal)
        return farm


farm = Farm()
cow = Animal("Berta", 5, "cow", 400)
farm.add_animal(cow)
chicken1 = Animal("Chirpy", 1, "chicken", 1)
farm.add_animal(chicken1)
chicken2 = Animal("Cluck", 2, "chicken", 1.2)
farm.add_animal(chicken2)
print(farm.animals)
#[Animal(name="Berta", age=5, species="cow", weight=400),
#Animal(name="Chirpy", age=1, species="chicken", weight=1),
#Animal(name="Cluck", age=2, species="chicken", weight=1.2)]
print(farm.feed_all("corn"))
#Feeding all animals on farm with corn:
#Berta the cow is being fed.
#Chirpy the chicken is being fed.
#Cluck the chicken is being fed.
#All animals have been fed.
animals = [
Animal("Berta", 5, "cow", 400),
Animal("Chirpy", 1, "chicken", 1),
Animal("Cluck", 2, "chicken", 1.2)
]
farm1 = Farm.create_farm_with_animals(animals)
print(farm1.animals)
#[Animal(name=’Berta’, age=5, species="cow", weight=400),
#Animal(name=’Chirpy’, age=1, species="chicken", weight=1),
#Animal(name=’Cluck’, age=2, species="chicken", weight=1.2)]


#Stwórz klasę Student, która będzie reprezentowała studenta na uczelni. Klasa powinna posiadać następujące pola:
#first_name, last_name, age, gpa (średnia ocen) oraz year. Klasa ta powinna posiadać również następujące trzy metody:
#1. Metodę instancji get_full_name, która będzie zwracać pełne imię i nazwisko studenta
#2. Metodę instancji is_on_probation, która zwraca wartość logiczną True lub False, w zależności od tego, czy
#student jest na warunkowym zawieszeniu (w zależności od średniej ocen).
#3. Metodę statyczną get_average_age, która przyjmuje listę studentów jako argument i zwraca średnią wieku
#studentów na liście.
#4. Metodę statyczną get_students_by_year, która przyjmuje listę obiektów klasy Student i zwraca słownik,
#którego kluczami są lata studiów (od 1 do 5), a wartościami są listy studentów należących do danego roku.
#5. Metodę statyczną print_students_by_year, która wykorzystuje funkcjonalność metody get_students_by_year
#i wyświetla studentów według zadanego roku. Tak jak w przypadku metody get_students_by_year przyjmuje
#ona jako argument listę studentów. UWAGA! Nie kopiować kodu z metody get_students_by_year do
#metody print_students_by_year!

class Student:
    def __init__(self, first_name, last_name, age, year, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gpa = gpa
        self.year = year

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_on_probation(self):
        if self.gpa <= 3.0:
            return True
        else:
            return False
    
    @staticmethod
    def get_average_age(lista):
        if not list:
            return 0
        else:
            return sum(student.age for student in lista) / len(lista)

    @staticmethod
    def get_students_by_year(lista):
        students_by_year = {year: [] for year in range(1, 6)}
        for student in lista:
            students_by_year[student.year].append(student)
        return students_by_year
    
    @staticmethod
    def print_students_by_year(lista):
        students_by_year = Student.get_students_by_year(lista)
        for year, students in students_by_year.items():
            print(f"{year} rok:")
            if students:
                for student in students:
                    print(f"- {student.get_full_name()} ({student.age} lat, średnia ocen: {student.gpa})")
            else:
                print("Brak")


s1 = Student("Jan", "Kowalski", 20, 2, 3.5)
s2 = Student("Anna", "Nowak", 22, 3, 2.8)
s3 = Student("Piotr", "Czerwinski", 19, 1, 2.1)
s4 = Student("Katarzyna", "Wójcik", 21, 4, 4.0)
print(s1.is_on_probation())
#False
print(s2.is_on_probation())
#True
students = [s1, s2, s3, s4]
print(Student.get_average_age(students))
#20.5
students_by_year = Student.get_students_by_year(students)
Student.print_students_by_year(students)
#1 rok:
#- Piotr Czerwinski (19 lat, średnia ocen: 2.8)
#2 rok:
#- Jan Kowalski (20 lat, średnia ocen: 3.5)
#3 rok:
#- Anna Nowak (22 lat, średnia ocen: 2.8)
#4 rok:
#- Katarzyna Wójcik (21 lat, średnia ocen: 4.0)
#5 rok:
#Brak
