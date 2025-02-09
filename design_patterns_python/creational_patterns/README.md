# Creational Design Patterns

Creational design patterns are design patterns that deal with object creation mechanisms, trying to create objects in a manner suitable to the situation. The basic form of object creation could result in design problems or added complexity to the design. Creational design patterns solve this problem by controlling the object creation process.

## Examples of Creational Design Patterns

### 1. Singleton Pattern
The Singleton Pattern ensures that a class has only one instance and provides a global point of access to it. This is useful when exactly one object is needed to coordinate actions across the system.

**Example:**
```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance
```

### 2. Factory Method Pattern
The Factory Method Pattern defines an interface for creating an object, but lets subclasses alter the type of objects that will be created. This pattern is useful when a class cannot anticipate the class of objects it must create.

**Example:**
```python
class Product:
    def operation(self):
        pass

class ConcreteProductA(Product):
    def operation(self):
        return "Result of ConcreteProductA"

class ConcreteProductB(Product):
    def operation(self):
        return "Result of ConcreteProductB"

class Creator:
    def factory_method(self):
        pass

    def some_operation(self):
        product = self.factory_method()
        return product.operation()

class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()
```

### 3. Abstract Factory Pattern
The Abstract Factory Pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes. This pattern is useful when a system needs to be independent of how its objects are created.

**Example:**
```python
class AbstractFactory:
    def create_product_a(self):
        pass

    def create_product_b(self):
        pass

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ProductA1()

    def create_product_b(self):
        return ProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ProductA2()

    def create_product_b(self):
        return ProductB2()

class ProductA1:
    def operation(self):
        return "Result of ProductA1"

class ProductB1:
    def operation(self):
        return "Result of ProductB1"

class ProductA2:
    def operation(self):
        return "Result of ProductA2"

class ProductB2:
    def operation(self):
        return "Result of ProductB2"
```

### 4. Builder Pattern
The Builder Pattern separates the construction of a complex object from its representation so that the same construction process can create different representations. This pattern is useful when creating complex objects step by step.

**Example:**
```python
class Builder:
    def build_part(self):
        pass

class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part(self):
        self.product.add("Part")

    def get_result(self):
        return self.product

class Product:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def show(self):
        return self.parts

class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_part()
```

### 5. Prototype Pattern
The Prototype Pattern specifies the kinds of objects to create using a prototypical instance, and creates new objects by copying this prototype. This pattern is useful when the cost of creating a new object is expensive.

**Example:**
```python
import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class ConcretePrototype(Prototype):
    def __init__(self, field):
        self.field = field

    def __str__(self):
        return f"ConcretePrototype with field: {self.field}"
```

These are some of the common creational design patterns used in software development to manage object creation in a flexible and reusable manner.