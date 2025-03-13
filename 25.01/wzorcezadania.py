#1. Zadanie oparte na wzoru Singleton
#Stwórz klasę Logger, która będzie używać wzorca Singleton do gromadzenia i logowania komunikatów.
#Każda instancja klasy Logger powinna mieć dostęp do jednego wspólnego dziennika logów.

class Logger:
    _instance = None

    def __new__(cls): #1 z 2 konstruktorów, tworzy instancję
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.log_messages = []
        return cls._instance
    
    def log(self, message):
        self.log_messages.append(message)

logger1 = Logger()
logger1.log("Log message from logger1")

logger2 = Logger()
logger2.log("Log message from logger2")

print(logger1.log_messages)  # ['Log message from logger1', 'Log message from logger2']
print(logger1 is logger2)  # True



#2. Zadanie oparte na wzorcu Factory Method
#Stwórz fabrykę do generowania różnych rodzajów kształtów (np. prostokąt, koło). Każdy kształt powinien
#implementować metodę area do obliczania pola powierzchni. Implementacja powinna zawierać klasy
#reprezentujące wybrany kształt oraz klasy fabryk tworzące obiekt danego kształtu.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
class ShapeFactory(ABC):
    @abstractmethod
    def create_shape(self):
        pass

class RectangleFactory(ShapeFactory):
    def create_shape(self):
        return Rectangle(4, 5)

class CircleFactory(ShapeFactory):
    def create_shape(self):
        return Circle(3)

# Przykład użycia
rectangle_factory = RectangleFactory()
rectangle = rectangle_factory.create_shape()
print(rectangle.area())  # 20

circle_factory = CircleFactory()
circle = circle_factory.create_shape()
print(circle.area())  # 28.274333882308138


#3. Zadanie oparte na wzoru Observer
#Stwórz system do monitorowania temperatury. Zaimplementuj klasę TemperatureSensor zbierającą
#dane o temperaturze, a następnie stwórz klasę TemperatureDisplay, która będzie obserwatorem
#i będzie wyświetlać aktualną temperaturę.

class TemperatureSensor:
    def __init__(self):
        self._temperature = 0
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def set_temperature(self, temperature):
        self._temperature = temperature
        self.notify_observers()

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

class TemperatureDisplay:
    def update(self, temperature):
        print(f"Current temperature: {temperature} degrees Celsius)")

# Przykład użycia
sensor = TemperatureSensor()

display1 = TemperatureDisplay()
display2 = TemperatureDisplay()

sensor.add_observer(display1)
sensor.add_observer(display2)

sensor.set_temperature(25)

# Output:
# Current temperature: 25 degrees Celsius
# Current temperature: 25 degrees Celsius


#4. Zadanie oparte na wzoru Decorator
#Stwórz system do generowania raportów finansowych. Zaimplementuj klasę Report generującą
#podstawowy raport, a następnie stwórz dekoratory, które dodają dodatkowe informacje do
#raportu, takie jak nagłówek i stopka.

class Report:
    def generate(self):
        return "Basic financial report"

class HeaderDecorator:
    def __init__(self, report):
        self._report = report

    def generate(self):
        return "Header\n" + self._report.generate()

class FooterDecorator:
    def __init__(self, report):
        self._report = report

    def generate(self):
        return self._report.generate() + "\nFooter"

# Przykład użycia
basic_report = Report()
decorated_report = FooterDecorator(HeaderDecorator(basic_report))

result = decorated_report.generate()
print(result)
# Output:
# Header
# Basic financial report
# Footer


#5. Zadanie oparte na wzoru State
#Stwórz automat do sprzedaży napojów. Zaimplementuj klasy VendingMachine oraz różne stany,
#takie jak ReadyState, DispenseState, OutOfStockState. Automat powinien zmieniać stany
#w zależności od akcji użytkownika.

class VendingMachine:
    def __init__(self, initial_state):
        self._state = initial_state

    def set_state(self, state):
        self._state = state

    def request_item(self):
        self._state.request_item()

    def dispense_item(self):
        self._state.dispense_item()

class State:
    def request_item(self):
        pass

    def dispense_item(self):
        pass

class ReadyState(State):
    def request_item(self):
        print("Item selected. Ready to dispense.")

    def dispense_item(self):
        print("Please select an item first.")

class DispenseState(State):
    def request_item(self):
        print("Item already selected. Dispensing now.")

    def dispense_item(self):
        print("Item dispensed. Thank you!")

class OutOfStockState(State):
    def request_item(self):
        print("Sorry, the machine is out of stock.")

    def dispense_item(self):
        print("Out of stock. Please select another item.")

# Przykład użycia
ready_state = ReadyState()
dispense_state = DispenseState()
out_of_stock_state = OutOfStockState()

vending_machine = VendingMachine(ready_state)

vending_machine.request_item()  # Item selected. Ready to dispense.
vending_machine.dispense_item()  # Please select an item first.

vending_machine.set_state




