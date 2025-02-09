# SOLID Principles in Python

The SOLID principles are a set of design principles that help developers create more maintainable, understandable, and flexible software. These principles were introduced by Robert C. Martin and are widely accepted in the object-oriented programming community. The SOLID acronym stands for:

- **S**ingle Responsibility Principle
- **O**pen/Closed Principle
- **L**iskov Substitution Principle
- **I**nterface Segregation Principle
- **D**ependency Inversion Principle

## Single Responsibility Principle (SRP)

A class should have only one reason to change, meaning it should have only one job or responsibility.

### Example:
```python
class Invoice:
    def __init__(self, items):
        self.items = items

    def calculate_total(self):
        return sum(item.price for item in self.items)

class InvoicePrinter:
    def print_invoice(self, invoice):
        for item in invoice.items:
            print(f'{item.name}: {item.price}')
        print(f'Total: {invoice.calculate_total()}')
```

## Open/Closed Principle (OCP)

Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification.

### Example:
```python
from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def apply(self, total):
        pass

class NoDiscount(Discount):
    def apply(self, total):
        return total

class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply(self, total):
        return total - (total * self.percentage / 100)

class Invoice:
    def __init__(self, items, discount: Discount):
        self.items = items
        self.discount = discount

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return self.discount.apply(total)
```

## Liskov Substitution Principle (LSP)

Objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program.

### Example:
```python
class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flying")

class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError("Ostriches can't fly")

def make_bird_fly(bird: Bird):
    bird.fly()

sparrow = Sparrow()
ostrich = Ostrich()

make_bird_fly(sparrow)  # Works fine
make_bird_fly(ostrich)  # Raises an error
```

## Interface Segregation Principle (ISP)

Clients should not be forced to depend on interfaces they do not use.

### Example:
```python
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self, document):
        pass

class MultiFunctionPrinter(Printer, Scanner):
    def print_document(self, document):
        print(f'Printing: {document}')

    def scan_document(self, document):
        print(f'Scanning: {document}')

class SimplePrinter(Printer):
    def print_document(self, document):
        print(f'Printing: {document}')
```

## Dependency Inversion Principle (DIP)

High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions.

### Example:
```python
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass

class MySQLDatabase(Database):
    def save(self, data):
        print(f'Saving {data} to MySQL database')

class UserService:
    def __init__(self, database: Database):
        self.database = database

    def save_user(self, user):
        self.database.save(user)

database = MySQLDatabase()
service = UserService(database)
service.save_user('John Doe')
```

These principles help in creating a robust and maintainable codebase. By adhering to these principles, you can ensure that your code is easier to understand, extend, and maintain.