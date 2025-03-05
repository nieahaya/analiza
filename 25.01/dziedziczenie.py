#Klasyczne dziedziczenie i konstruktor klasy bazowej:
#- Stwórz klasę bazową Person, która będzie miała atrybuty chronione _name i _age.
#- Zaimplementuj konstruktor inicjujący te atrybuty oraz metodę get_info, która zwraca informacje o osobie.
#- Następnie stwórz klasę pochodną Student, która będzie miała dodatkowy atrybut prywatny __student_id.
#- Dodaj metodę get_info do klasy Student, która będzie nadpisywać metodę klasy bazowej, aby zwrócić również identyfikator studenta.

class Person():
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def get_info(self):
        return f"Name: {self._name}, Age: {self._age}"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.__student_id = student_id

    def get_info(self):
        return f"{super().get_info()}, Student ID: {self.__student_id}"

person = Person("Jan", 30)
student = Student("Anna", 22, "S12345")

print(person.get_info())
print(student.get_info())


#Dziedziczenie wielokrotne:
#- Stwórz klasę Flying z metodą fly, która będzie wyświetlać komunikat "I can fly!".
#- Stwórz klasę Swimming z metodą swim, która będzie wyświetlać komunikat "I can swim!".
#- Stwórz klasę Duck, która będzie dziedziczyć po obu tych klasach i zawierać metodę quack, która wyświetla "Quack! Quack!".
#- Utwórz instancję klasy Duck i przetestuj wszystkie metody

class Flying():
    def fly():
        print("I can fly!")

class Swimming():
    def swim():
        print("I can swim")

class Duck(Flying, Swimming):
    def quack():
        print("Quack! Quack!")

duck = Duck.swim()
duck = Duck.fly()
duck = Duck.quack()