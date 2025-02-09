# Structural Design Patterns

Structural design patterns are design patterns that ease the design by identifying a simple way to realize relationships between entities. These patterns help ensure that if one part of a system changes, the entire system doesn't need to change along with it.

## Examples of Structural Design Patterns

### 1. Adapter Pattern
The Adapter Pattern allows incompatible interfaces to work together. It acts as a bridge between two incompatible interfaces by converting the interface of a class into another interface that a client expects.

**Example:**
```python
class EuropeanSocket:
    def voltage(self):
        return 230

class USASocket:
    def voltage(self):
        return 120

class Adapter:
    def __init__(self, socket):
        self.socket = socket

    def voltage(self):
        return self.socket.voltage()

# Usage
european_socket = EuropeanSocket()
adapter = Adapter(european_socket)
print(adapter.voltage())  # Output: 230
```

### 2. Bridge Pattern
The Bridge Pattern decouples an abstraction from its implementation so that the two can vary independently. It involves an interface which acts as a bridge, making the functionality of concrete classes independent from interface implementer classes.

**Example:**
```python
class DrawingAPI:
    def draw_circle(self, x, y, radius):
        pass

class DrawingAPI1(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"API1.circle at {x}:{y} radius {radius}")

class DrawingAPI2(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"API2.circle at {x}:{y} radius {radius}")

class Circle:
    def __init__(self, x, y, radius, drawing_api):
        self.x = x
        self.y = y
        self.radius = radius
        self.drawing_api = drawing_api

    def draw(self):
        self.drawing_api.draw_circle(self.x, self.y, self.radius)

# Usage
circle1 = Circle(1, 2, 3, DrawingAPI1())
circle2 = Circle(5, 7, 11, DrawingAPI2())
circle1.draw()  # Output: API1.circle at 1:2 radius 3
circle2.draw()  # Output: API2.circle at 5:7 radius 11
```

### 3. Composite Pattern
The Composite Pattern allows you to compose objects into tree structures to represent part-whole hierarchies. It lets clients treat individual objects and compositions of objects uniformly.

**Example:**
```python
class Component:
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        print("Leaf")

class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def operation(self):
        for child in self.children:
            child.operation()

# Usage
leaf1 = Leaf()
leaf2 = Leaf()
composite = Composite()
composite.add(leaf1)
composite.add(leaf2)
composite.operation()  # Output: Leaf Leaf
```

### 4. Decorator Pattern
The Decorator Pattern allows behavior to be added to an individual object, dynamically, without affecting the behavior of other objects from the same class. It is typically used to extend the functionalities of classes in a flexible and reusable way.

**Example:**
```python
class Component:
    def operation(self):
        pass

class ConcreteComponent(Component):
    def operation(self):
        print("ConcreteComponent")

class Decorator(Component):
    def __init__(self, component):
        self.component = component

    def operation(self):
        self.component.operation()

class ConcreteDecorator(Decorator):
    def operation(self):
        super().operation()
        print("ConcreteDecorator")

# Usage
component = ConcreteComponent()
decorator = ConcreteDecorator(component)
decorator.operation()  # Output: ConcreteComponent ConcreteDecorator
```

### 5. Facade Pattern
The Facade Pattern provides a simplified interface to a complex subsystem. It defines a higher-level interface that makes the subsystem easier to use.

**Example:**
```python
class Subsystem1:
    def operation1(self):
        print("Subsystem1: operation1")

class Subsystem2:
    def operation2(self):
        print("Subsystem2: operation2")

class Facade:
    def __init__(self):
        self.subsystem1 = Subsystem1()
        self.subsystem2 = Subsystem2()

    def operation(self):
        self.subsystem1.operation1()
        self.subsystem2.operation2()

# Usage
facade = Facade()
facade.operation()  # Output: Subsystem1: operation1 Subsystem2: operation2
```

### 6. Flyweight Pattern
The Flyweight Pattern reduces the cost of creating and manipulating a large number of similar objects. It achieves this by sharing as much data as possible with other similar objects.

**Example:**
```python
class Flyweight:
    def __init__(self, intrinsic_state):
        self.intrinsic_state = intrinsic_state

    def operation(self, extrinsic_state):
        print(f"Intrinsic: {self.intrinsic_state}, Extrinsic: {extrinsic_state}")

class FlyweightFactory:
    def __init__(self):
        self.flyweights = {}

    def get_flyweight(self, key):
        if key not in self.flyweights:
            self.flyweights[key] = Flyweight(key)
        return self.flyweights[key]

# Usage
factory = FlyweightFactory()
flyweight1 = factory.get_flyweight("state1")
flyweight2 = factory.get_flyweight("state1")
flyweight1.operation("extrinsic1")  # Output: Intrinsic: state1, Extrinsic: extrinsic1
flyweight2.operation("extrinsic2")  # Output: Intrinsic: state1, Extrinsic: extrinsic2
```

### 7. Proxy Pattern
The Proxy Pattern provides a surrogate or placeholder for another object to control access to it. It is used to create a representative object that controls access to another object.

**Example:**
```python
class RealSubject:
    def request(self):
        print("RealSubject: Handling request")

class Proxy:
    def __init__(self, real_subject):
        self.real_subject = real_subject

    def request(self):
        print("Proxy: Checking access prior to firing a real request")
        self.real_subject.request()

# Usage
real_subject = RealSubject()
proxy = Proxy(real_subject)
proxy.request()  # Output: Proxy: Checking access prior to firing a real request RealSubject: Handling request
```

These are some of the common structural design patterns used in software development to create flexible and reusable code.