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

#print(person.get_info())
#print(student.get_info())


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

#duck = Duck.swim()
#duck = Duck.fly()
#duck = Duck.quack()



#Dziedziczenie z atrybutami chronionymi:
#- Stwórz klasę bazową BankAccount z chronionymi atrybutami _account_number i _balance.
#-  Dodaj metody deposit i withdraw do klasy BankAccount, które będą odpowiednio zwiększać i zmniejszać saldo.
#- Stwórz klasę pochodną SavingsAccount, która będzie miała dodatkowy atrybut _interest_rate oraz 
#metodę apply_interest, która będzie zwiększać saldo o wartość odsetek.
#- Przetestuj działanie obu klas poprzez utworzenie instancji i wykonanie operacji na nich.

class BankAccount():
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Niewystarczająca ilość środków na koncie")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self._interest_rate = interest_rate

    def apply_interest(self):
        self._balance += self._balance * self._interest_rate

savings = SavingsAccount("SA12345", 1000, 0.05)
savings.deposit(500)
print(savings._balance)  # Output: 1500

savings.withdraw(200)
print(savings._balance)  # Output: 1300

savings.apply_interest()
print(savings._balance)  # Output: 1365.0


#Polimorfizm z metodą opisową:
#- Stwórz klasę bazową Shape z metodą abstrakcyjną area.
#- Zaimplementuj klasy pochodne Circle i Rectangle, które będą dziedziczyć po klasie Shape i implementować
#metodę area (dla Circle wzór na pole koła, a dla Rectangle wzór na pole prostokąta).
#- Utwórz listę obiektów różnych kształtów i napisz funkcję, która iteruje przez tę listę i wyświetla pole każdego kształtu.

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"Pole koła o promieniu {self.radius} to {3.14 * self.radius * self.radius}cm^2"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return f"Pole prostokąta o wysokości {self.height} i szerokości {self.width} to {self.width * self.height}cm^2"


shapes = [Circle(5), Rectangle(3, 4), Circle(2)]

def print_areas(shapes):
    for shape in shapes:
        print(f"Area: {shape.area()}")

#print_areas(shapes)


#Polimorfizm z interfejsem:
#- Stwórz klasę Payable z metodą calculate_pay.
#- Zaimplementuj klasy Employee i Contractor, które będą dziedziczyć po klasie Payable i implementować
#metodę calculate_pay (dla Employee będzie to stała pensja miesięczna, a dla Contractor będzie to stawka
#godzinowa pomnożona przez liczbę godzin).
#- Utwórz listę obiektów różnych typów i napisz funkcję process_payments, która iteruje przez tę listę
#i wyświetla wynagrodzenie każdego obiektu, korzystając z metody calculate_pay.

class Payable:
    def calculate_pay(self):
        pass

class Employee(Payable):
    def __init__(self, salary):
        self.salary = salary

    def calculate_pay(self):
        return self.salary

class Contractor(Payable):
    def __init__(self, rate, hours):
        self.rate = rate
        self.hours = hours

    def calculate_pay(self):
        return self.rate * self.hours

employee = Employee(3000)
contractor = Contractor(50, 160)

def process_payments(payables):
    for payable in payables:
        print(f"Pay: {payable.calculate_pay()}")

#process_payments([employee, contractor])

#Biblioteka i książki:
#- Stwórz klasę bazową Book z prywatnym atrybutem __title i chronionym atrybutem _author.
#- Dodaj metodę get_info, która zwraca informacje o książce.
#- Stwórz klasy pochodne EBook i PrintedBook. EBook będzie miała dodatkowy atrybut __file_size,
#a PrintedBook - __page_count.
#- Nadpisz metodę get_info w klasach pochodnych, aby zwracała pełne informacje o danym typie książki.
#- Utwórz instancje obu klas i przetestuj działanie metod.

class Book:
    def __init__(self, title, author):
        self. __title = title
        self._author = author

    def get_info(self):
        return f"Title: {self.__title}, Author: {self._author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.__file_size = file_size

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, File Size: {self.__file_size}MB"

class PrintedBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.__page_count = page_count

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Page count: {self.__page_count}"
    
# Testowanie
ebook = EBook("E-Book Title", "Author Name", 5)
printed_book = PrintedBook("Printed Book Title", "Author Name", 300)

#print(ebook.get_info())       # Output: Title: E-Book Title, Author: Author Name, File Size: 5MB
#print(printed_book.get_info())  # Output: Title: Printed Book Title, Author: Author Name, Page Count: 300

#Firma i pracownicy:
#- Stwórz klasę bazową Employee z chronionym atrybutem _name i metodą get_details.
#- Stwórz klasy pochodne Manager i Worker, gdzie Manager będzie miał dodatkowy atrybut
#__department, a Worker - __shift.
#- Nadpisz metodę get_details w klasach pochodnych, aby zawierała również specyficzne informacje o pracowniku.
#- Utwórz instancje obu klas i przetestuj działanie metod.

class Employee:
    def __init__(self, name):
        self._name = name
    
    def get_details(self):
        return f"Name: {self._name}"

class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name)
        self.__department = department

    def get_details(self):
        info = super().get_details()
        return f"{info}, Department: {self.__department}"

class Worker(Employee):
    def __init__(self, name, shift):
        super().__init__(name)
        self.__shift = shift

    def get_details(self):
        info = super().get_details()
        return f"{info}, Shift: {self.__shift}"
    
manager = Manager("Alice", "HR")
worker = Worker("Bob", "Night")

#print(manager.get_details())  # Output: Name: Alice, Department: HR
#print(worker.get_details())   # Output: Name: Bob, Shift: Night

#Urządzenia elektroniczne:
#- Stwórz klasę bazową Device z prywatnym atrybutem __serial_number i chronionym atrybutem _brand.
#- Dodaj metodę get_info, która zwraca informacje o urządzeniu.
#- Stwórz klasy pochodne Phone i Laptop. Phone będzie miała dodatkowy atrybut __screen_size, a Laptop - __battery_life.
#- Nadpisz metodę get_info w klasach pochodnych, aby zawierała również specyficzne informacje o urządzeniu.
#- Utwórz instancje obu klas i przetestuj działanie metod.

class Device:
    def __init__(self, serial_number, brand):
        self.__serial_number = serial_number
        self._brand = brand
    
    def get_info(self):
        return f"Serial Number: {self.__serial_number}, Brand: {self._brand}"
    
class Phone(Device):
    def __init__(self, serial_number, brand, screen_size):
        super().__init__(serial_number, brand)
        self.__screen_size = screen_size

    def get_info(self):
        return f"{super().get_info()}, Screen Size: {self.__screen_size} inches"

class Laptop(Device):
    def __init__(self, serial_number, brand, battery_life):
        super().__init__(serial_number, brand)
        self.__battery_life = battery_life
    
    def get_info(self):
        return f"{super().get_info()}, Battery Life: {self.__battery_life} hours"

phone = Phone("SN12345", "Apple", 6.1)
laptop = Laptop("SN54321", "Dell", 10)

print(phone.get_info())  # Output: Brand: Apple, Serial Number: SN12345, Screen Size: 6.1 inches
print(laptop.get_info())  # Output: Brand: Dell, Serial Number: SN54321, Battery Life: 10 hours
